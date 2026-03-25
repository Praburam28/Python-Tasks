def report():
    name = input("Name: ")
    m1 = int(input("Marks1: "))
    m2 = int(input("Marks2: "))
    m3 = int(input("Marks3: "))

    total = m1 + m2 + m3
    avg = total / 3

    if avg >= 90: grade = "A"
    elif avg >= 75: grade = "B"
    elif avg >= 50: grade = "C"
    else: grade = "Fail"

    print(f"\n{name} Report")
    print(f"Total: {total}, Avg: {avg:.2f}, Grade: {grade}")
