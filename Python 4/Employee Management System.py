employees = []

def add_employee():
    name = input("Name: ")
    age = int(input("Age: "))
    role = input("Role: ")
    salary = float(input("Salary: "))
    employees.append({"name": name, "age": age, "role": role, "salary": salary})

def display():
    for emp in employees:
        print(emp)

def update_employee(name):
    for emp in employees:
        if emp["name"] == name:
            emp["role"] = input("New Role: ")
            emp["salary"] = float(input("New Salary: "))

def delete_employee(name):
    global employees
    employees = [emp for emp in employees if emp["name"] != name]
