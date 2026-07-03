print("Enter Obtained Marks in 5 subjects")
Subject1=int(input("Enter Your Marks :"))
Subject2=int(input("Enter your Marks :"))
Subject3=int(input("Enter Your Marks :"))
Subject4=int(input("Enter Your Marks :"))
Subject5=int(input("Enter Your Marks :"))
Total=Subject1+Subject2+Subject3+Subject4+Subject5
Average=(Total//5)
validRange=range(0,101)
if Average not in validRange :
    print("invalid input")
elif Average in range(91,101):
    print("Your Grade is A1")
elif Average in range(81,91):
    print("Your Grade is A2")
elif Average in range(71,81):
    print("Your Grade is B1")
elif Average in range(61,71):
    print("Your Grade is B2")
elif Average in range(51,61):
    print("Your Grade is C1")
elif Average in range(41,51):
    print("Your Grade is C2")
elif Average in range(31,41):
    print("Your Grade is D1")
elif Average in range(21,31):
    print("Your Grade is D2")
elif Average in range(11,21):
    print("Your Grade is E1")
elif Average in range(1,11):
    print("Your Grade is E2")