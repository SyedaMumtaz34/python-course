try:
    num=int(input("enter your number: "))
    print("the number entered is ",num)
except ValueError as ex :
    print("exception ",ex)

    