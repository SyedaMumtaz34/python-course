def DueAmount():
    bill =float(input("enter a bill amount "))
    paid =float(input("enter a paid amount "))
    due = paid - bill
    return due
Amount=DueAmount()
print("The amount shopkeeper return is ",Amount)

    