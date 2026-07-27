import random

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"

all_characters = upper + lower + numbers

length = int(input("Enter password length: "))

password = ""

for i in range(length):
    password += random.choice(all_characters)

print("Generated password:", password)