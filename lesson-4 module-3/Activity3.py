# 1) Create a boolean variable `valid = False`.
valid = False 
# (This will be used to keep asking for input until a valid number is entered.)

# 2) Start a `while not valid` loop so the program repeats until `valid` becomes True.
while not valid:
# 3) Inside the loop, use a `try` block to handle invalid (non-integer) input safely.
    try:
        n=int(input("enter a number "))
        while n%2==0:
            print("bye")
        valid=True
    except ValueError:
        print("invalid ")
# a) Print "Invalid"

# b) The outer loop continues and asks again.