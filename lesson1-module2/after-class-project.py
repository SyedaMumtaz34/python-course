#Check age program (Nested Conditional Statements)

age = int(input("Enter your age: "))

if age >= 10:
    if age <= 20:
        print("You are allowed to enroll in the class.")
    else:
        print("You are NOT allowed to enroll. Age is more than 20.")
else:
    print("You are NOT allowed to enroll. Age is less than 10.")
