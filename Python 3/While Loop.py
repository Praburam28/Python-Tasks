#Print numbers from 1 to 20
i = 1
while i <= 20:
    print(i)
    i += 1


#Factorial of a number
n = int(input("Enter a number: "))
fact = 1

while n > 0:
    fact *= n
    n -= 1

print("Factorial:", fact)


#Reverse a number
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reversed number:", rev)


#Count digits in a number
num = int(input("Enter a number: "))
count = 0

while num > 0:
    num //= 10
    count += 1

print("Number of digits:", count)


#Keep asking input until user enters "stop"
text = ""

while text != "stop":
    text = input("Enter something: ")
