# 1) Ask the user to enter a number and store it in `num`.
num=int(input("enter a number "))
# 2) Set `sum` to 0.
sum=0
# (This will store the total of the cubes of each digit.)

# 3) Copy `num` into `temp`.
temp=num
# (We will change `temp` while checking digits, but we must keep `num` unchanged.)

# 4) Repeat while `temp` is greater than 0:
while temp >0:
# a) Find the last digit of `temp` and store it in `digit`.

# b) Add (digit × digit × digit) to `sum`.
    digit=temp%10
# c) Remove the last digit from `temp` so you can move to the next digit.
    sum=sum+digit**3
# 5) After the loop, compare `num` and `sum`:
    temp=temp//10 
# - If they are the same, print: `num` is an Armstrong number.
if num==sum:
    print(f"{num }is an Armstrong number")
# - Otherwise, print: `num` is not an Armstrong number.
else:
    print(f"{num }is not an Armstrong number ")