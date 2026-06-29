# 1) Take the total withdrawal amount as input from the user and store it in `Amount`.
amount=int(input("please enter amount for withdrawal "))
# 2) Find how many 100-rupee notes are needed:
note_1=amount//100
# Divide `Amount` by 100 (whole number division) and store it in `note_1`.

# 3) Find the remaining amount after taking out 100-rupee notes:

# Use the remainder of `Amount` after dividing by 100.
note_2=(amount% 100)//50
# 4) From the remaining amount, find how many 50-rupee notes are needed:

# Divide the remainder by 50 (whole number division) and store it in `note_2`.

# 5) Find the remaining amount after taking out 50-rupee notes:

# Use the remainder after dividing by 50.

# 6) From the remaining amount, find how many 10-rupee notes are needed:

# Divide the remainder by 10 (whole number division) and store it in `note_3`.
note_3=((amount%100)%50)//10
# 7) Print the number of 100-rupee notes, 50-rupee notes, and 10-rupee notes.
print("notes of 100 is",note_1)
print("notes of 50 is",note_2)
print("notes of 10 is",note_3)