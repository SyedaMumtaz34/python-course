class vehicle:
    def __init__(self,brand,max_speed):
        self.brand=brand
        self.max_speed=max_speed
    def show_details(self):
        print("brand:",self.brand)
        print("max_speed:",self.max_speed,"km/h")
class car(vehicle):
    def __init__(self, model,seats,brand, max_speed):
        self.model=model
        self.seats=seats
        super().__init__(brand, max_speed)
    def show_details(self):
        print("model:",self.model)
        print("seats:",self.seats)
        return super().show_details()
    def fuel_type(self,fuel):
        print(self.model,"uses",fuel)
my_car=car("city rider",5,"honda",100)
my_car.show_details()
my_car.fuel_type("petrol")
print("Is a car a subclass of vehicle?",issubclass(car,vehicle))
