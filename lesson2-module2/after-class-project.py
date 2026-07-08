num = int(input("Enter a number: "))
power = int(input("Enter the power: "))

result = 1

for i in range(power):
    result = result * num

print("Answer =", result)