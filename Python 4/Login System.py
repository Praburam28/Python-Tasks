users = {"Ram": "1234", "user": "pass"}

def login():
    u = input("Username: ")
    p = input("Password: ")

    if users.get(u) == p:
        print("Login Successful")
    else:
        print("Invalid Credentials")
