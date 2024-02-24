class Car:
    def __init__(self, brand, model):
        self.brand = brand       # self is like this keyword in js or pointer to the object
        self.model = model

my_Car = Car("Ford", "Mustang")
print(my_Car.brand) 
print(my_Car.model)




