from datetime import datetime
from django.db.utils import IntegrityError, DatabaseError, DataError

from ...models import Users
from ...models import Departments
from ..department_list import department_list, departaments

def registration(data, passw, departments):

    try:

        Users.objects.create(identification_card=data['id_card'], name=data['name'],
            surnames=data['surnames'], phone=data['phone'], age=data['age'], status=True, 
            admission_date=datetime.date(datetime.now()), administrator=True, email=data['email'],
            password=passw, department_id=departaments(data))

        return True

    except IntegrityError as e:

        return False

    except DatabaseError as e:
        return False

    except DataError as e:
        return False