# 1) Import the `random` module to generate random numbers.
import random 
# 2) Create a variable `playing = True` to control the game loop.
playing=True 
# 3) Generate a random number between 0 and 9 using `random.randint(0, 9)`
number=str(random.randint(0,9))
# and convert it to a string, then store it in `number`.

# (This is the secret number the user must guess.)

# 4) Print instructions explaining the guessing game.
print("I will generate a number from 0 to 9 and you have to guess the number one at time ")
# 5) Start a `while` loop that runs as long as `playing` is True:
while playing :
    guess=input("give me your best guess: \n")
# a) Take a guess from the user and store it in `guess`.

# 6) Check if the user's guess matches the secret number:
    if number==guess :
        print("You win the game ")
        print("the number was ",number)
        break
    else:
        print("your guess is not right try again ")
# a) If `number == guess`:

# i) Print a winning message.

# ii) Display the secret number.

# iii) Stop the loop using `break` (game ends).

# 7) Otherwise (if the guess is incorrect):

# a) Print a message telling the user to try again.

# b) The loop continues and asks for another guess.