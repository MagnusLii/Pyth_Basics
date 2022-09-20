class Car:                                          # class names are commonly capitalized.

    # attribute = stuff an object is/has.
    #make = None
    #model = None
    #year = None
    #colour = None

    # Instance variables.   Variables with no default value.
    # method = what the object does.
    def __init__(self,make,model,year,colour):      # '__init__()' is a special method that constructs objects, known as 'constructor' in other programming languages.

        # attributes for creating new objects.
        self.make = make                            # 'self.' refers to the object currently being created.
        self.model = model                          # connects the arguments to the parameters on line 10.
        self.year = year
        self.colour = colour

    # Class variable.       Variables with a default value.
    wheels = 4











    def drive(self):                                # 'self' refers to the object itself.
        print("This "+self.model+" is driving.")

    def stop(self):
        print("This car is stopped.")