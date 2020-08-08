from django.shortcuts import render, redirect
import re

from assets_users.models import Assets
from assets_users.models import Departments
from .local_modules.validations import validate_data
from .local_modules.hashing import hashing_password
from .local_modules.registration_users import registration 
from .local_modules.department_list import department_list
 

# vista para registrar usuario
def user_register(request):
    
    context = {} 

    if request.method == "POST":

        post_data = {
            'id_card':request.POST['identification_card'],
            'name':request.POST['name'], 'surnames':request.POST['surnames'],
            'phone':request.POST['phone'],'department':request.POST['department'],
            'age':request.POST['age'],'email':request.POST['email']
        }

        if validate_data(post_data):  # valida los datos
            if registration(post_data, hashing_password(request.POST['password']), department_list()):
                # realiza la insercción de datos a la tabla users
                context['response'] = '1'
                return render(request, 'registration.html', context)

            else: # error al hacer la insercción
                context['response'] = '2'
                context['departments'] = department_list()
                context['data'] = post_data
                return render(request, 'registration.html', context)

        else: # error al validar datos
            context['response'] = '0'  # contexto que se envía al html y se rescata para JS
            context['departments'] = department_list()
            context['data'] = post_data
            return render(request, 'registration.html', context)


# vista para formulario
def registration_form(request):

    context = {'departments': department_list()}
    return render(request, 'registration.html', context)
