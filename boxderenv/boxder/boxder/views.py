from django.shortcuts import render
from django.views.defaults import page_not_found


def index(request):
    try:    
        request.session.modified = True
        
        del request.session['name']
        del request.session['surnames']

        return render(request, 'index.html')
    
    except KeyError as e:
        return render(request, 'index.html')

def login_user(request):
    
    if request.method == "POST":
        post_data = {'id_card': request.POST['identification_card'],
                    'password': request.POST['password']}

    return render(request, 'index.html')
