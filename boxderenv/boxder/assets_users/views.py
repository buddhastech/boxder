# intern modules
import re
# django modules
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db.utils import DatabaseError, OperationalError, ProgrammingError
from django.core.cache import cache


# models
from assets_users.models import Assets
from assets_users.models import Departments
# local modules
from .local_modules.users.validations import validate_data
from .local_modules.users.hashing import hashing_password, compare_password
from .local_modules.users.registration_users import registration 
from .local_modules.department_list import department_list
from .local_modules.users.login_user import login, get_password, get_data_user, set_sessions_user
from .local_modules.database_exceptions import exception_db_response
from .local_modules.assets.register_asset import registration_asset, validate_dni

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
                        
                        administrator_auth = bool()

                        for data in object_request:
                            administrator_auth = data.administrator
                            break                

                        if not(administrator_auth):
                            set_sessions_user(request, data_user)
                            return redirect('/boxder/')
                        else:
                            set_sessions_user(request, data_user)
                            return redirect('/administrator/')    
                    except:
                        context['response'] = '0'
                        return render(request, 'index.html', context)
                else:
                    context['response'] = '1'
                    return render(request, 'index.html', context)

        else:
            context['response'] = '1'
            return render(request, 'index.html', context)

# vista para formulario
def registration_form(request):

    context = {'departments': department_list()}
    return render(request, 'registration.html', context)

# vista para registrar activos
def asset_registration(request):
    context = {}
    if request.method == "POST":
        data_asset = {'brand': request.POST['brand'],'model': request.POST['model'],
                      'cost': request.POST['cost'], 'weight': request.POST['weight'],
                      'provider': request.POST['provider'], 'util_life': request.POST['util_life'],
                      'name':request.POST['name'], 'user_id':request.POST['user_dni']}
        

        if validate_dni(data_asset['user_id']):
            
            if registration_asset(data_asset) == '1':

                context['response'] = '1'
            
            elif registration_asset(data_asset) == '2':
                
                context['response'] = '2'
            
            elif registration_asset(data_asset) == '3':

                context['response'] = '3'
        else:
            context['response'] = '4'
                
        return render(request, 'boxderindex.html', context)
        
# vista para página principal de la app
def boxder_index(request):

    context = {}
    try: 
        if request.session['name'] or request.session['surnames']:
                all_assets = Assets.objects.all();
                context['total_assets'] = all_assets.count()
                context['active_assets'] = Assets.objects.filter(actual_status="Activo").count()
                context['suspend_assets'] = Assets.objects.filter(actual_status="Suspendido").count()
                context['low_assets'] = Assets.objects.filter(actual_status="De baja").count()
                context['assets'] = Assets.objects.filter(user_id_id=request.session['id'])
                return render(request, 'boxderindex.html', context)

    except KeyError as e:
        return redirect('/inicio/')
  
# vista para página principal de administrador
def boxder_admin(request):


    context = {}
    try: 
        if request.session['name'] or request.session['surnames']:
                all_assets = Assets.objects.all();
                context['assets'] = all_assets
                context['total_assets'] = all_assets.count()
                print(context['total_assets'])
                return render(request, 'boxderAdmin.html', context)

    except KeyError as e:
        return redirect('/inicio/')

def configuration(request):

    return render(request, 'configuration_user.html')