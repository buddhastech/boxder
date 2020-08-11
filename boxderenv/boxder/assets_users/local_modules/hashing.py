import os
import hashlib

salt = os.urandom(32) # forma la sal de 32 bits
key = ""
new_key = ""

def hashing_password(passw): # genera la contraseña hash y la une con la sal
        
        hashing = hashlib.pbkdf2_hmac('sha256', 
        passw.encode('utf-8'), 
        salt, 
        100000,
        dklen=64)  # realiza el hashing
                
        return hashing

def compare_password():

        if key == new_key:
                return 1
        else:
                return 0
