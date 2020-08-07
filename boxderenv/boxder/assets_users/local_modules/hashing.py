import os
import hashlib

def hashing_password(passw):
        
        salt = os.urandom(32) # forma la sal de 32 bits
        key = hashlib.pbkdf2_hmac('sha256', 
        passw.encode('utf-8'), 
        salt, 
        100000,
        dklen=64)  # realiza el hashing
        storage_password = salt + key  # combina la sal con la password hash
        
        return storage_password

