import re

def validate_data(data):

    flag = True  # bandera para retornar el estado de la validación

    if (not(data['id_card'].isdigit()) or 
        not(data['phone'].isdigit()) or
        not(data['age'].isdigit())):
            
            flag = False

    # \d devuelve una lista con números en caso de que la cadena contenga números
    # \s devuelve coincidencias de espacios en blanco
    # \S devuelve coincidencias con caracteres diferentes a un espacio en blanco

    if((re.findall("\d", data['name']) and re.findall("\S", data['name'])) or 
        (re.findall("\d", data['name']) and re.findall("\s", data['name'])) or
        (re.findall("\d", data['surnames']) and re.findall("\S", data['surnames'])) or
        (re.findall("\d", data['surnames']) and re.findall("\s", data['surnames'])) or
        (re.findall("\d", data['department']) and re.findall("\S", data['department'])) or
        (re.findall("\d", data['department']) and re.findall("\s", data['department']))):

            flag = False

    if flag:
        return True
    else:
        return False

