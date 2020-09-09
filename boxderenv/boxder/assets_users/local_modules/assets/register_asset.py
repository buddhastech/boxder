from datetime import datetime
from ...models import Assets, Users
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

def generate_code_asset(data):

    last_code = Assets.objects.all()
    brand_letters = data['brand']
    brand_code = ""
    code = ""

    for number_letter in range(len(brand_letters)):
        if brand_letters[number_letter].isalpha():
            if number_letter == 3:
                break
            else:
                brand_code += brand_letters[number_letter]
    
    if last_code:
        last_code = last_code[len(last_code)-1]
        numbers = ""
        for number in range(len(last_code.code)):
            if last_code.code[number].isnumeric():
                numbers += str(last_code.code[number])
        
        numbers = int(numbers)
        numbers += 1

        code = brand_code + "-" + str(numbers).zfill(4)

    else:
        consecutive = 1
        code = brand_code + "-" + str(consecutive).zfill(4)

    return code

def generate_admision_date():
    
    return print(datetime.date(datetime.now()))

def validate_dni(dni):
        try:
            user = Users.objects.get(identification_card=dni)
            return 1
        except Exception as e:
            return 0

def registration_asset(data):

    try:
        Assets.objects.create(code=generate_code_asset(data),
        brand=data['brand'], name=data['name'], model=data['model'], useful_life=data['util_life'],
        cost=data['cost'], weight=data['weight'], admission_date=generate_admision_date,
        actual_status="Activo", provider=data['provider'], user_id_id=data['user_id'])
    
        return '1'

    except IntegrityError as error:
        return '2'

    except ValidationError as error:
        return '3'



