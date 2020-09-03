# intern modules
import re
# django modules
from django.shortcuts import render, redirect
from django.db.utils import DatabaseError, OperationalError, ProgrammingError
from django.core.cache import cache

# models
from assets_users.models import Assets
from assets_users.models import Departments
# local modules
from .local_modules.validations import validate_data
from .local_modules.hashing import hashing_password, compare_password
from .local_modules.registration_users import registration 
from .local_modules.department_list import department_list
from .local_modules.login_user import login, get_password, get_data_user, set_sessions_user
from .local_modules.database_exceptions import exception_db_response
 

# vista para registrar usuario
def user_register(request):
    
    context = {} 
    try:
        if request.method == "POST":
            post_data = { 
                'id_card':request.POST['identification_card'],
                'name':request.POST['name'], 'surnames':request.POST['surnames'],
                'phone':request.POST['phone'],'department':request.POST['department'],
                'age':request.POST['age'],'email':request.POST['email'].replace(".com", ".oo")
            }

            password_hash = hashing_password(request.POST["password"]) 

            if validate_data(post_data):  
                if registration(post_data, password_hash, department_list()):
                    context['response'] = '1'
                    return render(request, 'registration.html', context)
                else: 
                    context['response'] = '2'
                    context['departments'] = department_list()
                    context['data'] = post_data
                    return render(request, 'registration.html', context)
            else: 
                context['response'] = '0'  # contexto que se envía al html y se rescata para JS
                context['departments'] = department_list()
                context['data'] = post_data
                return render(request, 'registration.html', context)
    except DatabaseError as e:

                exception_db_response(
                '3', 
                department_list(), 
                render(request, 'registration.html', context))
    except OperationalError as e:

                exception_db_response(
                '4', 
                department_list(), 
                render(request, 'registration.html', context))
    except ProgrammingError as e:

                exception_db_response(
                '5', 
                department_list(), 
                render(request, 'registration.html', context))

# vista para validar usuario
def user_login(request):

    context = {}
    if request.method == 'POST':
            
        post_data = {'identification_card': request.POST['identification_card'],
                        'password': request.POST['password']}

        object_request = login(post_data['identification_card'])
        password_user = get_password(object_request) 

        if object_request and password_user: # si ha encontrado algo con dicha cedula
            
                if compare_password(post_data['password'], password_user):
                    try:
                        data_user = get_data_user(object_request)                
                        set_sessions_user(request, data_user)
                
                        return redirect('/boxder/')
                    
                    except:
                        context['response'] = '0'
                        return render(request, 'index.html', context)
                else:
                    print("hello")
                    context['response'] = '1'
                    return render(request, 'index.html', context)

        else:
            context['response'] = '1'
            return render(request, 'index.html', context)

# vista para formulario
def registration_form(request):

    context = {'departments': department_list()}
    return render(request, 'registration.html', context)

# vista para página principal de la app
def boxder_index(request):

    try: 
        if request.session['name'] or request.session['surnames']:
                return render(request, 'boxderindex.html')
    except KeyError as e:
        return redirect('/inicio/')
  