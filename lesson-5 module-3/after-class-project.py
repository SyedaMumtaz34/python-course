import random
import math

print("=== Random Fun Calculator ===")

# Step 1 & 2: Lucky Number
lucky_number = random.randint(1, 10)
print("Your lucky number is:", lucky_number)

# Step 3: Random Activity
activities = [
    "Read a book",
    "Go for a walk",
    "Listen to music",
    "Draw a picture",
    "Play a game"]

activity = random.choice(activities)
print("Today's activity:", activity)

# Step 4 & 5: Guessing Game
secret = random.randint(1, 5)

while True:
    guess = int(input("Guess the secret number (1-5): "))

    if guess == secret:
        print("Congratulations! You guessed correctly.")
        break
    else:
        print("Wrong guess! Try again.")

# Step 6: ceil() and floor()
num = float(input("Enter a decimal number: "))
print("Ceiling value:", math.ceil(num))
print("Floor value:", math.floor(num))

# Step 7: copysign() and fabs()
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("Copy Sign:", math.copysign(x, y))
print("Absolute Value of first number:", math.fabs(x))

# Step 8: gcd()
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

print("Greatest Common Divisor (GCD):", math.gcd(num1, num2))

# Final Summary
print("\n=== Final Summary ===")
print("Lucky Number:", lucky_number)
print("Random Activity:", activity)
print("Thank you for using the Random Fun Calculator!")