class User:

    def greet(self):
        print("Welcome User")


class Student(User):

    def greet(self):
        print("Welcome Student")


class Faculty(User):

    def greet(self):
        print("Welcome Faculty")


# Objects
student = Student()
faculty = Faculty()

student.greet()
faculty.greet()
