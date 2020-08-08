from ..models import Departments

def department_list():

    departments = Departments.objects.all()
    return departments
    