from ..models import Users

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
