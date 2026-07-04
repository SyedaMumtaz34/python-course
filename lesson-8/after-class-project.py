# Taking input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Before swapping:")
print("a =", a)
print("b =", b)
print("c =", c)

# Swapping three numbers
a, b, c = b, c, a

print("After swapping:")
print("a =", a)
print("b =", b)
print("c =", c)