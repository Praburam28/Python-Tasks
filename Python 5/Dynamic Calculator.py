def calculate_total(*numbers):
    total = sum(numbers)
    avg = total / len(numbers) if numbers else 0
    return total, avg

nums = list(map(int, input("Enter numbers separated by space: ").split()))

result = calculate_total(*nums)

print("Total:", result[0])
print("Average:", result[1])
