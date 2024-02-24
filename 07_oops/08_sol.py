class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand       # __ implies private which was only accessed within the class not even in the object of that class.
        self.__model = model
        # self.total_car +=1
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !!"

    def fullName(self):
        return f"{self.__brand} {self.__model}"


    @staticmethod
    def general_description():
        return "Cars are means of transport"

    @property                                           # cant write  value but can read the value
    def model(self):
        return self.__model


class Electric_Car(Car):   # Inheritance - electric car inherits from car class
    def __init__(self,brand, model, battery_size):
        super().__init__(brand, model)     # calling parent constructor using super() method
        self.battery_size = battery_size

my_Tesla = Electric_Car("Tesla", "Model S", "75KWh")
# my_Tesla.model = "S"                # we can't rewrite this parameter  because it is a property not a variable
print(my_Tesla.model)


my_Safari = Car("Tata", "Safari")
# print(my_Safari.general_description())

my_newCar = Car("Tata", "Altroz")
print(my_newCar.model)
# print(my_newCar.brand)          

