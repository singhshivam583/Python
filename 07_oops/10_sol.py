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

class Battery:
    def battery_info(self):
        return "this is the battery"

class Engine:
    def  engine_info(self):
        return "This is an engine"

class ElectricCar(Car,Battery,Engine):                # multiple inheritance is possible in python
    pass

my_newTesla = ElectricCar("Tesla", "Model S")
print(my_newTesla.fullName())
print(my_newTesla.engine_info())
print(my_newTesla.battery_info())
print(my_newTesla.model)
print(my_newTesla.get_brand())
