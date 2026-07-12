# 1) Define a function `add(P, Q)` that returns the sum of two numbers (P + Q).
def add (P,Q):
    return P+Q
# 2) Define a function `subtract(P, Q)` that returns the difference of two numbers (P - Q).
def sub (P,Q):
    return P-Q
# 3) Define a function `multiply(P, Q)` that returns the product of two numbers (P * Q).
def mult (P,Q):
    return P*Q
# 4) Define a function `divide(P, Q)` that returns the division result of two numbers (P / Q).
def Div (P,Q):
    return P/Q
# 5) Display a menu to the user showing the available operations:
print("please select the operation ")
# a) Add
print("a.add ")
# b) Subtract
print("b.sub ")
# c) Multiply
print("c.mult ")
# d) Divide
print("d.Div")
# 6) Take the user's choice as input and store it in `choice`.
choice=input("please enter choice a/b/c/d ")
# 7) Take two integer inputs from the user:

# a) Store the first number in `num_1`
num_1=int(input("enter a 1st number "))
# b) Store the second number in `num_2`
num_2=int(input("enter a 2nd number "))
# 8) Use conditional statements to perform the chosen operation:

# a) If `choice` is 'a', call `add(num_1, num_2)` and print the result.
if choice == "a":
    print(add(num_1 ,num_2 ))
# b) Else if `choice` is 'b', call `subtract(num_1, num_2)` and print the result.
elif choice=="b":  
    print(sub(num_1 ,num_2))
# c) Else if `choice` is 'c', call `multiply(num_1, num_2)` and print the result.
elif choice=="c":
    print(mult(num_1,num_2 ))
# d) Else if `choice` is 'd', call `divide(num_1, num_2)` and print the result.
elif choice=="d":
    print(Div(num_1 ,num_2 ))
# 9) If the user enters anything other than a/b/c/d, print an invalid input message.
else:
    print("invalid input ")
