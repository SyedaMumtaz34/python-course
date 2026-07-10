# 1) Print a heading message for the pattern.
print("half pyramid pattern of stars ")
# 2) Take an integer input from the user and store it in `n`.
n=int(input("enter the number of rows: "))
# (This represents the number of rows in the half pyramid.)

# 3) Use an outer loop to run from 0 to `n-1` (each iteration builds one row):
for i in range(n):
# a) For each row `i`, the number of stars to print is `i + 1`.

# 4) Use an inner loop to print stars in the current row:

# a) Run `j` from 0 to `i` (total `i + 1` times)
    for j in range(i+1):
# b) Print "* " on the same line using `end=""` so it doesn’t go to the next line.
        print("*",end=" ")
# 5) After finishing the inner loop for a row, print a blank `print()`
    print()
# to move the cursor to the next line for the next row.