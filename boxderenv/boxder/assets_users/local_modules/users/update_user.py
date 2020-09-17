from ...models import Users
from django.db.utils import IntegrityError, DatabaseError, DataError
from django.core.exceptions import ValidationError
from ..department_list import departaments

def update_user(data):
    
    try:
        Users.objects.filter(identification_card=data["id"]).update(
            name=data['name'], surnames=data['surnames'],
            phone=data['phone'], department=departaments(data),
            age=data['age'], email=data['email'])
        
        return '1'

    except IntegrityError as e:
        return '2'

    except DatabaseError as e:
        return '3'

    except DataError as e:
        return '3'
    
    except ValidationError as e:
        return '3'
        