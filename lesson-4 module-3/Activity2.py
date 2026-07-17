# 1) Start a `try` block to run code that may cause exceptions.
try:
    
# 2) Take two numbers from the user in a single input, separated by a comma:

# a) Use `eval(input(...))` to read and convert the input.

# b) Store the two values in `num1` and `num2`.
    num1,num2=eval(input("enter two numbers separated by comma: "))
# 3) Perform division:
    result=num1/num2
# a) Compute `result = num1 / num2`.

# b) Print the result.
    print("result is",result )
# 4) Handle possible errors using multiple `except` blocks:

# 5) If a `ZeroDivisionError` occurs (when `num2` is 0),
except ZeroDivisionError:
# print "Division by zero is error !!".
    print("Division by zero is error!!")
# 6) If a `SyntaxError` occurs (for example, the comma is missing or format is incorrect),
except SyntaxError:
# print a message explaining the correct input format: "1, 2".
    print("comma is missing.enter a number separated by comma like this 1,2 ")
# 7) If any other error occurs, use a general `except` block
except:
    print("wrong input ")
# and print "Wrong input".

# 8) If no exception occurs in the `try` block, run the `else` block
else:
    print("no exceptions ")
# and print "No exceptions".

# 9) Run the `finally` block no matter what happens (error or no error),
finally:
    print("this will eecute no matter what ")
# and print "This will execute no matter what".