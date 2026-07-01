# 1) Store values in `a`, `b`, and `c`.
a=2 
b=1
c=0
# 2) Check an AND condition using `a and b and c`:
if a and b and c:
    
# - This becomes True only if all three values are treated as True.
    print("all the numbers have boolean value as true")
# - If the condition is True, print the “all true” message.
else:
    print("atleast one is false")
# - Otherwise, print the “at least one false” message.

# 3) Re-assign (change) new values to `a`, `b`, and `c` for the next checks.
a=-1
b=2
c=0
# 4) Check an OR condition: `a > 0 or b > 0`
if a > 0 or b > 0:
    print("either is greater than 0")
# - If at least one of them is greater than 0, print the “either is greater than 0” message.

# - Otherwise, print the “no number is greater than 0” message.
else:
    print("no number is greater than 0")
# 5) Check another OR condition: `b > 0 or c > 0`
if b > 0 or c > 0:
    print("either is greater than 0")
# - If at least one of them is greater than 0, print the “either is greater than 0” message.

# - Otherwise, print the “no number is greater than 0” message.
else:
    print("either no number is greater than 0")