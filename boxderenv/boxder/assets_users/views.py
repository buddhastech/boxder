from django.shortcuts import render, redirect
import re
from assets_users.models import Assets
from assets_users.models import Departments


from .local_modules.validations import validate_data
from .local_modules.hashing import hashing_password
from .local_modules.registration import registration
 
def department_list():

    departments = Departments.objects.all()
    return departments
    

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
            context['departments'] = department_list()
            
        else:
            context['response'] = '0'
            context['departments'] = department_list()

        context['data'] = post_data
        print(post_data)
        return render(request, 'registration.html', context)


# vista para formulario
def registration_form(request):

    departments = Departments.objects.all()
    context = {'departments': departments}

    return render(request, 'registration.html', context)
