from django.shortcuts import render, redirect
import re

from assets_users.models import Assets
from assets_users.models import Departments
from .local_modules.validations import validate_data
from .local_modules.hashing import hashing_password, compare_password
from .local_modules.registration_users import registration 
from .local_modules.department_list import department_list
from .local_modules.login_user import login
 

# vista para registrar usuario
def user_register(request):
    
    context = {} 

    if request.method == "POST":

        # datos que llegan del cliente
        post_data = { 
            'id_card':request.POST['identification_card'],
            'name':request.POST['name'], 'surnames':request.POST['surnames'],
            'phone':request.POST['phone'],'department':request.POST['department'],
            'age':request.POST['age'],'email':request.POST['email']
        }

        password_hash = hashing_password(request.POST["password"]) 

        # valida los datos
        if validate_data(post_data):  
            if registration(post_data, password_hash, department_list()):
                # realiza la insercción de datos a la tabla users
                context['response'] = '1'
                return render(request, 'registration.html', context)

            # error al hacer la insercción (integrityError)
            else: 
                context['response'] = '2'
                context['departments'] = department_list()
                context['data'] = post_data
                return render(request, 'registration.html', context)

        # error al validar datos
        else: 
            context['response'] = '0'  # contexto que se envía al html y se rescata para JS
            context['departments'] = department_list()
            context['data'] = post_data
            return render(request, 'registration.html', context)

def user_login(request):

    if request.method == 'POST':

        post_data = {'identification_card': request.POST['identification_card'],
                    'password': request.POST['password']}

        object_request = login(post_data['identification_card'])
        password_user = ""

        if object_request:

            for object in object_request:
                password_user = object.password
        
        if compare_password(post_data['password'], password_user):
            print("Autentificación concedida")
            return render(request, 'index.html')

        else:
            return render(request, 'index.html', )
            
# vista para formulario
def registration_form(request):

    context = {'departments': department_list()}
    return render(request, 'registration.html', context)
