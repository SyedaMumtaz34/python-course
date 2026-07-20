try:
    age=int(input("Enter your age: "))
    if age%2==0:
        print("Your age is even ")
    else:
        print("your age is odd ")
except ValueError:
    print("enter a valid integar ")