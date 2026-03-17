#  Add 3 elements using append()
nums = []

nums.append(10)
nums.append(20)
nums.append(30)

print(nums)


# Insert element at specific index
nums = [10, 20, 30, 40]

nums.insert(2, 25)

print(nums)


# Remove element using remove()
nums = [10, 20, 30, 40]

nums.remove(30)

print(nums)


# Reverse list without using .reverse()
nums = [10, 20, 30, 40]
rev = []

for i in range(len(nums)-1, -1, -1):
    rev.append(nums[i])

print("Reversed list:", rev)


# Sort list without using .sort()
nums = [40, 10, 30, 20]

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j]:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

print("Sorted list:", nums)
