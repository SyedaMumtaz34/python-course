#1) Display a menu asking the user to select a ride:
print("select a ride 1.bike and 2.car")
# - 1 for Bike

# - 2 for Car

# 2) Take the user’s input and store it in `choice`.
choice=int(input("Enter a number "))
# 3) If `choice` is 1 (Bike):
if choice == 1:
    print("1. scooty 2.scooter")
    choice2=int(input("Enter a number "))
    if choice2 == 1:
        print("your choice is scooty")
    else:
        print("your choice is scooter")
# a) Show bike options (Scooty / Scooter)

# b) Take the user’s input for bike type and store it in `choice2`

# c) If `choice2` is 1, print "you have selected scooty"

# Else, print "you have selected scooter"

# 4) Else if `choice` is 2 (Car):
elif choice==2:
    print("1.sedan 2.XUV")
    choice3=int(input("Enter a number "))
    if choice3==1:
     print("you have selected sedan")
    else: 
        print("you have selected XUV")
# a) Show car options (Sedan / XUV)

# b) Take the user’s input for car type and store it in `choice3`

# c) If `choice3` is 1, print "you have selected sedan"

# Else, print "you have selected XUV"

# 5) Else (if `choice` is not 1 or 2):
else:
    if choice not in(1,2):
        print("Wrong choice!")
# Print "Wrong choice!"