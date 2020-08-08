from ..models import Users
from ..models import Departments
from datetime import datetime
from django.db.utils import IntegrityError
def registration(data, passw, departments):

    try:
        
        depart_id = int() # id del departamento a asignar
        departments = Departments.objects.all()

        for department in departments:
            if department.name == data['department']:
                depart_id = department.department_id

        Users.objects.create(identification_card=data['id_card'], name=data['name'],
            surnames=data['surnames'], phone=data['phone'], age=data['age'], status=True, 
            admission_date=datetime.date(datetime.now()), email=data['email'],
            password=passw, department_id=depart_id)

        return True

    except IntegrityError as e:

        return False