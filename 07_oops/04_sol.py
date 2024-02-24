class Car:
    def __init__(self, brand, model):
        self.__brand = brand       # __ implies private which was only accessed within the class not in the  object of that class.
        self.model = model

    def get_brand(self):
        return self.__brand + " !!"

    def fullName(self):
        return f"{self.__brand} {self.model}"

# Inheritance
class Electric_Car(Car):   # Inheritance - electric car inherits from car class
    def __init__(self,brand, model, battery_size):
        super().__init__(brand, model)     # calling parent constructor using super() method
        self.battery_size = battery_size

my_Tesla = Electric_Car("Tesla", "Model S", "75KWh")
# print(my_Tesla.__brand)
print(my_Tesla.get_brand())
print(my_Tesla.fullName())

