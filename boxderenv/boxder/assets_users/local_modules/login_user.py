from ..models import Users
from django.contrib.sessions.models import Session

def login(identification_card):

    id_card = Users.objects.filter(identification_card=identification_card)

    if id_card:
        return id_card
    else:
        return 0

def get_password(user):

    password_user = ""
    if user:
        print("1")
        for data in user:
            password_user = data.password
    
    return password_user

def get_data_user(user):
    
    data_user = {}
    if user:
        for data in user:

            data_user.setdefault('name', data.name)
            data_user.setdefault('surnames', data.surnames)
        
        print(data_user, "get_data_user")
        return data_user

def set_sessions_user(re, data):

    re.session['name'] = data['name']
    re.session['surnames'] = data['surnames']
    return re.session['name']