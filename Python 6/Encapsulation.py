class User:
    def __init__(self):
        self.__user_name = None
        self.__pwd = None

    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name   # password hidden

    def register(self):
        print("Registering user:", self.__user_name)

    def login(self):
        print("Logging in:", self.__user_name)


# Test
user = User()
user.set_user("john", "1234")

user.register()
user.login()
