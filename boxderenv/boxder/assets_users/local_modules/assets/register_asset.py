from datetime import datetime
from ...models import Assets
from django.db.utils import IntegrityError

def generate_code_asset(data, brand):

    last_code = Assets.objects.all()
    last_code = last_code[len(last_code)-1]
    brand_letters = data['brand']
    brand_code = ""
    code = ""

    for number_letter in range(len(brand_letters)):
        if brand_letters[number_letter].isalpha():
            if number_letter == 3:
                break
            else:
                brand_code += brand_letters[number_letter]
    
    if last_code is None:
        consecutive = 1
        code = brand_code + "-" + str(consecutive).zfill(4)

    else:
        numbers = ""
        for number in range(len(last_code.code)):
            if last_code.code[number].isnumeric():
                numbers += str(last_code.code[number])
        
        numbers = int(numbers)
        numbers += 1

        code = brand_code + "-" + str(numbers).zfill(4)

    return code

def generate_admision_date():
    
    return print(datetime.date(datetime.now()))

def registration_asset(data):

    try:
        Assets.objects.create(code=generate_code_asset( data, data['brand']),
        brand=data['brand'], model=data['model'], useful_life=data['util_life'],
        cost=data['cost'], weight=data['weight'], admission_date=generate_admision_date,
        actual_status="A", provider=data['provider'])

        return 1

    except IntegrityError as error:
        return False



