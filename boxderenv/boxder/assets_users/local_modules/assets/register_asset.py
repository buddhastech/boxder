from datetime import datetime
from ...models import Assets
from django.db.utils import IntegrityError

def generate_code_asset(brand, model):
    return "hi"

def generate_admision_date():
    
    return print(datetime.date(datetime.now()))

def registration_asset(data):

    try:
        Assets.objects.create(code=generate_code_asset(data['brand'], data['model']),
        brand=data['brand'], model=data['model'], useful_life=data['util_life'],
        cost=data['cost'], weight=data['weight'], admission_date=generate_admision_date,
        actual_status="A", provider=data['provider'])

        return 1

    except IntegrityError as error:
        return False



