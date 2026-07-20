def calculator(a,b,operation):
    if operation =="+":
        return a+b
    elif operation =="-":
        return a-b
    elif operation =="*":
        return a*b
    elif operation=="/":
        if b!=0:
            return a/b
    else:
        print("cannot divide by zero: ")
num1=float(input("enter your first number: "))
num2=float(input("enter your second number: "))
print("operation(+,-,*,/)")
num3=(input("choose from this list: "))
print(calculator(num1,num2,num3))