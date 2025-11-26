import os
from utils.csv_utils import *

PATH_USERS = os.path.join("data", "usuarios.csv")

def user_validation(user, password):
    users = read_csv(PATH_USERS)

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