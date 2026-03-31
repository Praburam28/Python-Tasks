class User:

    def register(self):
        print("User Registered")

    def login(self):
        print("User Logged In")


class Student(User):

    def student_greet(self):
        print("Hello Student")


class Faculty(User):

    def faculty_greet(self):
        print("Hello Faculty")


class TempFaculty(Faculty):

    def tempFaculty_greet(self):
        print("Hello Temp Faculty")


# Objects
student = Student()
faculty = Faculty()
temp = TempFaculty()

# Parent methods
student.register()
student.login()

# Child methods
student.student_greet()
faculty.faculty_greet()

temp.tempFaculty_greet()
temp.faculty_greet()  
temp.register()       
