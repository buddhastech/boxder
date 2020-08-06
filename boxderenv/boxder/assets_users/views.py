from django.shortcuts import render, redirect
import re
from assets_users.models import Assets
from .validations import validate_data
from .hashing import hashing_password
 

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

        if validate_data(post_data):
            context['response'] = '1'

        else:
            context['response'] = '0'

        context['data'] = post_data
        return render(request, 'registration.html', context)


# vista para formulario
def registration_form(request):

    return render(request, 'registration.html')
