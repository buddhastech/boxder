from django.shortcuts import render
from django.views.defaults import page_not_found

def index(request):

    return render(request, 'index.html')

