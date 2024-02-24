class Car:
    def __init__(self, brand, model):
        self.brand = brand       # self is like this keyword in js or pointer to the object
        self.model = model

    def fullName(self):
        return f"{self.brand} {self.model}"

my_Car = Car("Ford", "Mustang")
print(my_Car.brand) 
print(my_Car.model)

myNew_Car = Car("Toyota", "Corolla")
print(myNew_Car.fullName()) 


