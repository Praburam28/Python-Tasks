class User:

    users_count = 0

    def __init__(self, name, pwd):
        self.__name = name
        self.__pwd = pwd
        User.users_count += 1

    def login(self):
        print("User logged in:", self.__name)
        return self

    def greet(self):
        print("Welcome User")
        return self

    def register(self):
        print("User registered:", self.__name)
        return self


class Student(User):

    def greet(self):
        print("Welcome Student")
        return self


class Faculty(User):

    def greet(self):
        print("Welcome Faculty")
        return self


# Objects
student = Student("Ram", "123")
faculty = Faculty("John", "456")

# Method Chaining
student.login().greet().register()

faculty.login().greet().register()

print("Total Users:", User.users_count)
