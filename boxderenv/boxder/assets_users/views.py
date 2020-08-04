from django.shortcuts import render, redirect
import os
import hashlib
import binascii
import re
from assets_users.models import Assets

context = {'errors':[], 'corrects':[]}  

def hashing_password(passw):
        salt = hashlib.sha256(os.urandom(32)).hexdigest().encode('ascii') 

        key = hashlib.pbkdf2_hmac('sha256', 
        passw.encode('utf-8'), 
        salt, 
        100000,
        dklen=128)
        storage_password = salt + key
        
        return storage_password

"""def validate_data(data):

    global context

    if not(data['name'].isalpha()):
        context['errors'].append('Nombre inválido')

    if not(data['surnames'].isalpha()):
        context['errors'].append('Apellidos inválidos')

    if not(data['phone'].isdigit()):
        context['errors'].append('Número de teléfono inválido')
    
    if not(data['department'].isalpha()):
        context['errors'].append('Departamento inválido')

    if not(data['age'].isdigit()):
        context['errors'].append('Edad inválida')
    
    if not(re.findall('\S+@\S+', data['email'])):
        context['errors'].append('Correo inválido')
    

    return context
"""
def user_register(request):

    global context

    if request.method == "POST":

        post_data = {
            'id_card': request.POST['identification_card'],
            'name': request.POST['name'], 'surnames': request.POST['surnames'],
            'phone':request.POST['phone'],'department':request.POST['department'],
            'age':request.POST['age'],'email':request.POST['email']
        }

        return redirect('/registration/')

def registration_form(request):

    return render(request, 'registration.html')
