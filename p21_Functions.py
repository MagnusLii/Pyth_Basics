# function =        A block of code which is executed only when it is called.
#                   Useful when you have code that may need to be run multiple times.


# Functions.
def hello():                        # 'def' = code to define a function, 'hello()' = name of the function.
    print("Hello!")                 # Indented code is the code used when the function is called.*
    print("Have a nice day.")
#    pass                            # Pass is used when you want a function to not do anything.

def hello2(name):                   # 'Parameters' can be put inside the brackets
    print("Hello! "+name)
    print("Have a nice day.")

def hello3(first_name,last_name,age):   # Multiple parameters can be assigned.
    print("Hello! "+first_name+" "+last_name)
    print("You are "+str(age)+" years old.")
    print("Have a nice day.")


# Variables.
my_name = "HUNNIE"

# Using functions.
hello()                             # Using the function.
hello()

hello2("Hunnie")                    # When calling a function 'arguments' can be put inside the brackets to fill parameters,
hello2(my_name)                     # 'variables' can be used as 'arguments'.
hello3("hunnie","hun",28)            # All the parameters must be filled.