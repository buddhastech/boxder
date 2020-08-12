from ..models import Departments

def department_list():

    departments = Departments.objects.all()
    return departments
    
def departaments(data):
    
    for department in department_list():
        if department.name == data['department']:
            depart_id = department.department_id

    return depart_id
