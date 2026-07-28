class parrot:
    species="bird"
    def __init__(self,name,age ):
        self.name=name
        self.age=age
blu=parrot("blu",10)
woo=parrot("woo",15)
print("blu is a ",blu.species)
print("woo is a ",woo.species)
print("{} is {} years old ".format(blu.name,blu.age))
print("{} is {} years old ".format(woo.name,woo.age))