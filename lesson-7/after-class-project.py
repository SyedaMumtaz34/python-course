a=input("Enter a letter: ")

if len(a)==1:
    print("ASCII value:",ord(a)) 
    
    if 'A' <= a <= 'Z':
        print("Letter type: Uppercase letter")
    elif 'a' <= a <= 'z':
        print("Letter type: Lowercase letter")
    elif '0' <= a <= '9':
        print("This is a Digit, not a letter")
    else:
        print("This is a Special character, not a letter")
else:
    print("Error: Please enter exactly ONE letter")#