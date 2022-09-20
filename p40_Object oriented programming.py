from p40_Objects import Car

car_1 = Car("Chevy","Corvette",2022,"blue")                 # Using the constructor to make a 'car_1' object.
car_2 = Car("Ford","Mustang",2022,"Black")

#print(car_2.make)                                           # prints the values for said object.
#print(car_2.model)
#print(car_2.year)
#print(car_2.colour)

car_2.drive()                                               # runs the imported functions with 'car_2' object.
car_2.stop()