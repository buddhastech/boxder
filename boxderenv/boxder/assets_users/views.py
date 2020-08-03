from django.shortcuts import render, redirect
import os
import hashlib
import binascii
from assets_users.models import Assets

def hashing_password(passw):
        salt = hashlib.sha256(os.urandom(32)).hexdigest().encode('ascii') 

        key = hashlib.pbkdf2_hmac('sha256', 
        passw.encode('utf-8'), 
        salt, 
        100000,
        dklen=128)
        storage_password = salt + key
        
        return storage_password

def validate_date(data):

    context = {'errors':[]}    
    if not(data['name'].isalpha()):
        context['errors'].append('Nombre inválido')

    if not(data['surnames'].isalpha()):
        context['errors'].append('Apellidos inválidos')

    if not(data['phone'].isdigit()):
        context['errors'].append('Número de teléfono inválido')

    return context

def user_register(request):

    if request.method == "POST":

        post_data = {'id_card': request.POST['identification_card'],
                    'name': request.POST['name'], 'surnames': request.POST['surnames'],
                    'phone':request.POST['phone'],'department':request.POST['department'],
                    'age':request.POST['age'],'email':request.POST['email']}

        return render(request, 'registration.html', context=validate_date(post_data))

def registration_form(request):

    return render(request, 'registration.html')
