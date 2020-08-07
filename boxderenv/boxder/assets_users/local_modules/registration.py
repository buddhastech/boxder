from ..models import Assets
from datetime import datetime

def registration(**kwargs):

    try:
        if kwargs[5] == "Informatica" or "informatica":
            kwargs[5] = '1'
            
        Assets.objects.create(identification_card=kwargs[0], name=kwargs[1],
            surnames=kwargs[2], phone=kwargs[3], age=kwargs[4], status=True, 
            admission_date=datetime.date(datetime.now()),department_id=kwargs[5],
            email=kwargs[6], password=kwargs[6])

        return True
    
    except:
        return False