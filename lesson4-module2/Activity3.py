# 1) Take an integer input from the user and store it in `num`.
num=int(input("enter a four digit number "))
# Also copy the same value into `t` for digit counting.
t=num
# 2) Initialize `numLen = 0` to count the number of digits.
numLen=0
# 3) Count the digits using a loop:
while t>0:
# a) Repeat while `t > 0`
    numLen=numLen+1
# b) Increase `numLen` by 1 each time

# c) Remove the last digit of `t` using `t = int(t/10)`
    t=int(t/10)
# 4) Check if the number has at least 4 digits:

# If `numLen >= 4`, continue to find the middle digits.
if numLen>=4:
    numLen=(numLen//2)
    chk=0
    while num>0:
        rem=num%10
        if chk==numLen:
            midone = rem
        elif chk==(numLen-1):
            midtwo = rem
        num=(num//10)
        chk=chk+1
    prod = midone * midtwo
    print(f"product of mid digit is {prod} ")
else:
    print("it is not 4 or more than 4 digit number ")
