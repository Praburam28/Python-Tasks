students = {}

def add_student(name, courses):
    students[name] = courses

def update_courses(name, courses):
    students[name] = courses

def display():
    for s, c in students.items():
        print(s, "->", c)
