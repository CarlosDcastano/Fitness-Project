from services.usuarios import user_validation
from services.miembros import *

def login():
    print("===LOGIN===")
    user = input("Enter your user: ")
    password = input("Enter your password: ")

    valido, rol = user_validation(user, password)

    if valido:
        print(f"Welcome, {user}, Rol: {rol}")
        return True
    else:
        print("Wrong credentials")
        return False











if __name__ == "__main__":
    if login():
        print("Access approved")
        registrar_miembro()
        

    else:
        print("Access denied")



