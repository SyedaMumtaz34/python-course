# 1) Store the given values:

# `mean1` (wrong mean), `wrong_number`, `correct_number`, and `total_number`.
mean1=38
Wrong_number=36
Correct_number=56
total_number=40
# 2) Calculate the total sum using the wrong mean:
sum=mean1*total_number
print("the sum of Totalnumber",sum)
# - Multiply `mean1` by `total_number`

# - Store it in `sum`

# - Print the sum.

# 3) Fix the sum to get the correct total:
num2=sum-((Wrong_number)-(Correct_number))
# - Remove the wrong number (subtract `wrong_number`)

# - Add the correct number (add `correct_number`)

# - Store the corrected total in `num2`

# - Print the corrected sum.
print("The correct sum of these numbers",num2)
# 4) Find the correct mean:

# - Divide `num2` by `total_number`
mean2=num2/total_number
# - Store it in `mean2`

# - Print `mean2`.
print("The correct mean ",mean2)