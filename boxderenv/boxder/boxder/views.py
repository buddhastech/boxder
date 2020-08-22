from django.shortcuts import render
from django.views.defaults import page_not_found
from django.core.cache import cache

def index(request):

    request.session.flush()
    return render(request, 'index.html')

def login_user(request):
    if request.method == "POST":
        post_data = {'id_card': request.POST['identification_card'],
                    'password': request.POST['password']}

    return render(request, 'index.html')
