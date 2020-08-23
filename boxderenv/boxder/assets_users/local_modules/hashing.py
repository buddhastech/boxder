import bcrypt

def hashing_password(passw): # genera la contraseña hash y la une con la sal
        try:
                passw = passw.encode()
                salt = bcrypt.gensalt(rounds=16)
                hashed = bcrypt.hashpw(passw, salt)

                return hashed.decode('utf-8')
        
        except TypeError as e:
                print("Error: ", e)

def compare_password(new_password, password):

        new_password = new_password.encode()
        password = password.encode()
        
        try:
                if bcrypt.checkpw(new_password, password):
                        return 1
                else:
                        print("error")
                        return 0
        except TypeError as e:
                print("Error de chequeo: ", e)


