#  Create a list of 5 numbers and print sum
nums = [10, 20, 30, 40, 50]
total = 0

for n in nums:
    total += n

print("Sum:", total)


# Find maximum value in list
nums = [10, 25, 5, 40, 15]
max_val = nums[0]

for n in nums:
    if n > max_val:
        max_val = n

print("Maximum:", max_val)


# Find minimum value in list
nums = [10, 25, 5, 40, 15]
min_val = nums[0]

for n in nums:
    if n < min_val:
        min_val = n

print("Minimum:", min_val)


# Count total elements in list
nums = [10, 20, 30, 40, 50]
count = 0

for n in nums:
    count += 1

print("Total elements:", count)


# Check if element exists in list
nums = [10, 20, 30, 40, 50]
x = int(input("Enter number to search: "))

found = False
for n in nums:
    if n == x:
        found = True
        break

if found:
    print("Element found",x)
else:
    print("Element not found")
