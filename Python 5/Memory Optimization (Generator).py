def square_generator(n):
    for i in range(n):
        yield i * i

def square_list(n):
    return [i * i for i in range(n)]

gen = square_generator(5)
lst = square_list(5)

print("Generator:", gen)
print("List:", lst)

print("Generator values:")
for val in gen:
    print(val)
