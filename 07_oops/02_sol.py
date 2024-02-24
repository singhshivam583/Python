class Car:
    def __init__(self, brand, model):
        self.brand = brand       # self is like this keyword in js or pointer to the object
        self.model = model

    def fullName(self):
        return f"{self.brand} {self.model}"

# Inheritance
class Electric_Car(Car):   # Inheritance - electric car inherits from car class
    def __init__(self,brand, model, battery_size):
        super().__init__(brand, model)     # calling parent constructor using super() method
        self.battery_size = battery_size

my_Tesla = Electric_Car("Tesla", "Model S", "75KWh")
print(f"The car is an {my_Tesla.fullName()} and has a {my_Tesla.battery_size} capacity battery.")

