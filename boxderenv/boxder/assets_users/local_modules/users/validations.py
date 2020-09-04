import re

possible_regex = {
    "espetial_characters": "[\°\!\/\#\$\%\&\/\(\)\=\?\*\¡\<\>\·\@\|\~\½\¬\{\]\}\[\-\+]+",
    "numbers": "[0-9]+",
    "letters": "[a-zA-Z]+"
}

def validate_data(data):

    flag = True  # bandera para retornar el estado de la validación

 #       not(data['phone'].isdigit()) or
    if (re.findall(possible_regex['letters'], data['id_card']) or
        re.findall("\s", data['id_card']) or 
        re.findall(possible_regex['espetial_characters'], data['id_card']) or 
        re.findall("\s", data['phone']) or  
        re.findall(possible_regex['letters'], data['phone']) or
        re.findall(possible_regex['espetial_characters'], data['phone']) or 
        re.findall(possible_regex['letters'], data['age']) or 
        re.findall("\s", data['age']) or
        re.findall(possible_regex['espetial_characters'], data['age'])):
            
            flag = False

    # \d devuelve una lista con números en caso de que la cadena contenga números
    # \s devuelve coincidencias de espacios en blanco
    # \S devuelve coincidencias con caracteres diferentes a un espacio en blanco

    if((re.findall("\d", data['name']) and re.findall("\S", data['name'])) or
        re.findall(possible_regex['espetial_characters'], data['name']) or
        re.findall(possible_regex['numbers'], data['name']) or 
        (re.findall("\d", data['name']) and re.findall("\s", data['name'])) or

        (re.findall("\d", data['surnames']) and re.findall("\S", data['surnames'])) or
        re.findall(possible_regex['espetial_characters'], data['surnames']) or
        re.findall(possible_regex['numbers'], data['surnames']) or
        (re.findall("\d", data['surnames']) and re.findall("\s", data['surnames'])) or

        (re.findall("\d", data['department']) and re.findall("\S", data['department'])) or
        (re.findall("\d", data['department']) and re.findall("\s", data['department'])) or
        re.findall(possible_regex['espetial_characters'], data['department']) or
        re.findall(possible_regex['numbers'], data['department']) or
        not(re.findall("@", data['email']))):

            flag = False

    if flag:
        return True
    else:
        return False

