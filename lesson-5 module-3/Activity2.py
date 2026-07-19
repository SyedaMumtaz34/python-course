# 1) Import the `random` module to let the computer make a random choice.
import random 
# 2) Start an infinite loop using `while True` so the game can repeat for multiple rounds.
while True:
    
# 3) Take the user's choice as input and store it in `user_action`.
    user_action=input("Enter a choice (rock,paper,scissors): ").lower()
# (Expected inputs: "rock", "paper", or "scissors".)

# 4) Create a list `possible_actions` containing the three valid moves.
    possible_actions=['rock','paper','scissors']
# 5) Use `random.choice(possible_actions)` to randomly select the computer’s move
    computer_action=random.choice(possible_actions)
# and store it in `computer_action`.

# 6) Display both choices (user and computer) using an f-string.
    print(f"You Choose {user_action},Computer choose {computer_action}")
# 7) Compare `user_action` and `computer_action` to decide the result:

# a) If both are the same, print that it’s a tie.
    if user_action==computer_action:
        print(f"both player selected {user_action}. it's a tie")
# b) Else if the user chose "rock":
    elif user_action=="rock":
        if computer_action=="scissors":
            print("rock smashes scissors you win ")
        else:
            print("paper covers rock you lose ")
# i) If computer chose "scissors", user wins.
    elif user_action=="paper":
        if computer_action=="rock":
            print("paper covers rock you win ")
        else:
            print("scissors cut paper you lose ")
# ii) Otherwise, user loses (computer chose "paper").

# c) Else if the user chose "paper":
    elif user_action=="scissors":
        if computer_action=="paper":
            print("scissors cut paper you win ")
        else:
            print("rock smashes scissors you lose ")
    play_again=input("Do you want to play again y or n? ")
    if play_again=="n":
        break 
# i) If computer chose "rock", user wins.

# ii) Otherwise, user loses (computer chose "scissors").

# d) Else if the user chose "scissors":

# i) If computer chose "paper", user wins.

# ii) Otherwise, user loses (computer chose "rock").

# 8) After showing the result, ask the user if they want to play again

# and store the input in `play_again`.

# 9) If `play_again` is not "y", stop the game using `break`.

# Otherwise, the loop continues and a new round starts.