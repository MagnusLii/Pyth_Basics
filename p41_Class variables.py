from p40_Objects import Car

Car.wheels = 2                          # Changes the default value for the class variable.

car_1 = Car("Chevy","Corvette",2022,"blue")
car_1.wheels = 3                        # Changes the value of the class var for a specific object.

print(Car.wheels)                       # prints default value for class.
print(car_1.wheels)
attrs = vars(car_1)
print(', '.join("%s: %s" % item for item in attrs.items()))