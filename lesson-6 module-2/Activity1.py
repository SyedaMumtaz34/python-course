print("welcome to number guesseing game ")
secret_number=27

guess=int(input("Enter a number "))
if guess == (1,50) :
    print("ice cold congratulations you have passed ")
    if guess == (40,50):
        print("cold you are close ")
        if guess ==(30,40):
            print("warm you are far ")
            if guess ==(20,30):
                print("hot you are too far ")
            
else:
    print("the secret number was",secret_number)