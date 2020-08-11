from ..models import Users

def login(identification_card):

    id_card = Users.objects.filter(identification_card=identification_card)

    if id_card:
        print("yes")
        return id_card
    else:
        print("no")
        return 0

