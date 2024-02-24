class Car:
    def __init__(self, brand, model):
        self.__brand = brand       # __ implies private which was only accessed within the class not in the  object of that class.
        self.model = model

    def get_brand(self):
        return self.__brand + " !!"

    def fullName(self):
        return f"{self.__brand} {self.model}"

    def fuel_Type(self):
        return "Petrol or Diesel"

# Inheritance
class Electric_Car(Car):   # Inheritance - electric car inherits from car class
    def __init__(self,brand, model, battery_size):
        super().__init__(brand, model)     # calling parent constructor using super() method
        self.battery_size = battery_size

    def fuel_Type(self):
        return "Electric Charge"


my_Tesla = Electric_Car("Tesla", "Model S", "75KWh")
print(my_Tesla.fullName())
print(my_Tesla.fuel_Type())

my_Safari = Car("Tata", "Safari")
print(my_Safari.fullName())
print(my_Safari.fuel_Type())
# Encapsulation
