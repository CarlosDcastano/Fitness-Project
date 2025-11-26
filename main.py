from services.usuarios import user_validation

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
    else:
        print("Access denied")



