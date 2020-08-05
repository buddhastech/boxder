from django.shortcuts import render, redirect
import os
import hashlib
import binascii
import re
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

def user_register(request):
    
    context = {'errors':'e'} 

    if request.method == "POST":

        post_data = {
            'id_card': request.POST['identification_card'],
            'name': request.POST['name'], 'surnames': request.POST['surnames'],
            'phone':request.POST['phone'],'department':request.POST['department'],
            'age':request.POST['age'],'email':request.POST['email']
        }

        # return redirect('/registration/')

    return render(request, 'registration.html')

def registration_form(request):

    return render(request, 'registration.html')
