def shutdown(user_input):
    if user_input == "yes":
        return "Shutting down"
    elif user_input == "no":
        return "Abort shut down"
    else:
        return "Sorry"
print("Do you want to shutdown your laptop?")
choice = input("Enter Yes or No: ").lower()
print(shutdown(choice))