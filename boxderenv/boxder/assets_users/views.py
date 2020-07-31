from django.shortcuts import render

def registration_form(request):

    return render(request, 'registration.html')