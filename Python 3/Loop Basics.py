#Print numbers from 1 to 50
for i in range(1, 51):
    print(i)
    
#Print even numbers from 1 to 100
for i in range(1, 101):
    if i % 2 == 0:
        print(i)
        
#Print odd numbers from 1 to 100
for i in range(1, 101):
    if i % 2 != 0:
        print(i)
        
#Multiplication table of 7
for i in range(1, 11):
    print("7 x", i, "=", 7 * i)
    
#Sum of numbers from 1 to 100
total = 0
for i in range(1, 101):
    total += i
print("Sum:", total)

#Print numbers from 50 to 1 (reverse)
for i in range(50, 0, -1):
    print(i)

#Count numbers divisible by 3 (1–100)
count = 0
for i in range(1, 101):
    if i % 3 == 0:
        count += 1
print("Count:", count)

#Print squares of numbers from 1 to 10
for i in range(1, 11):
    print(i, "=>", i * i)
    
#Print cubes of first 10 numbers
for i in range(1, 11):
    print(i, "=>", i ** 3)
    
#Take input n and print 1 to n
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(i)
