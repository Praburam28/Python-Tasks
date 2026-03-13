age = int(input())
height = int(input())
weight = int(input())

if age >= 18:
    if height >= 160:
        if weight >= 60:
            print("Selected")
        else:
            print("Rejected")
    else:
        print("Rejected")
else:
    print("Rejected")


    
marks = int(input())
age = int(input())

if marks >= 60:
    if age >= 17:
        print("Admission Granted")
    else:
        print("Rejected")
else:
    print("Rejected")



    
age = int(input())
height = int(input())
weight = int(input())

if age >= 16:
    if height >= 150:
        if weight >= 50:
            print("Selected")
        else:
            print("Rejected")
    else:
        print("Rejected")
else:
    print("Rejected")
