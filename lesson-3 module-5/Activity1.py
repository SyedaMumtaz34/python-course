class FamilyMember:
    def __init__(self,eye_colour,height_cm):
        self.eye_colour=eye_colour
        self.height_cm=height_cm
    def show_traits(self):
        print("eye_colour ",self.eye_colour)
        print("height_cm ",self.height_cm)
class kid(FamilyMember):
    def __init__(self, name,age,eye_colour, height_cm):
        self.name=name
        self.age=age
        super().__init__(eye_colour, height_cm)
    def show_traits(self):
        print("name",self.name)
        print("age",self.age)
        return super().show_traits()
    def favorite_hobby(self,hobby):
        print(self.name,"loves",hobby)
child=kid("Syeda",15,"brown",4.11)
child.show_traits()
child.favorite_hobby("painting")
print("Is kid subclass of FamilyMember? ",issubclass(kid,FamilyMember))