import os
from utils.csv_utils import *

RUTA_USUARIOS = os.path.join("data", "usuarios.csv")

def user_validation(user, password):
    users = leer_csv(RUTA_USUARIOS)

    for u in users:
        if u["user"] == user and u["password"] == password:
            return True, u["rol"]
        
    return False, None



user = [
    {"user": "admin",
     "password":"Password123",
     "rol":"administrador"},

    {"user": "JenMiAmor",
     "password":"MiMuñeca",
     "rol":"administrador"}
]