users = []

def create_user(name, age, role):
    user = {
        "name": name.title(),
        "age": age,
        "role": role
    }
    return user

users.append(create_user("ram", 22, "developer"))
users.append(create_user("priya", 21, "tester"))
users.append(create_user("arun", 23, "manager"))

for user in users:
    print(user)
