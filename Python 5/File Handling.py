file = open("team_data.txt", "w")

file.write("Ram, 22, Developer\n")
file.write("Priya, 21, Tester\n")
file.write("Arun, 23, Manager\n")

print("File closed before closing?:", file.closed)

file.close()

print("File closed after closing?:", file.closed)



file = open("team_data.txt", "r")

content = file.read()
print("\nFile Content:\n", content)

file.close()
