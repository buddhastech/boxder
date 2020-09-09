from ...models import Users
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
        try:
            for data in user:
                password_user = data.password
            return password_user
            
        except ValueError as e:
            return 0
        
def get_data_user(user):
    
    data_user = {}
    if user:
        for data in user:
            
            data_user.setdefault('identification_card', data.identification_card)
            data_user.setdefault('name', data.name)
            data_user.setdefault('surnames', data.surnames)
        
        return data_user

def set_sessions_user(re, data):

    re.session['id'] = data['identification_card']
    re.session['name'] = data['name']
    re.session['surnames'] = data['surnames']
    