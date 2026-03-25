account = {}

def create(name, balance):
    account[name] = balance

def deposit(name, amt):
    account[name] += amt

def withdraw(name, amt):
    if account[name] >= amt:
        account[name] -= amt
    else:
        print("Insufficient balance")

def check(name):
    print("Balance:", account.get(name))
