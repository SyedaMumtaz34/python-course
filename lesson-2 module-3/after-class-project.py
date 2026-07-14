def shutdown(user_input):
    if user_input == "Yes":
        return "Shutting down"
    elif user_input == "No":
        return "Abort shut down"
    else:
        return "Sorry"

choice = input("Enter Yes or No: ")
print(shutdown(choice))