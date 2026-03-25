cart = []

def add_item():
    name = input("Product: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    cart.append({"name": name, "price": price, "qty": qty})

def total_bill():
    total = sum(item["price"] * item["qty"] for item in cart)
    print("Total Bill:", total)

def remove_item(name):
    global cart
    cart = [i for i in cart if i["name"] != name]

def display_cart():
    for item in cart:
        print(item)
