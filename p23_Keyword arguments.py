# Keyword arguments =   Arguments preceded by an identifier when we pass them to a function
#                       the order of the arguments doesn't matter, unlike positional arguments
#                       python knows the names of the arguments that our function receives.


# Functions
def hello(first,middle,last):                       # 'Defining' function 'hello' and it's 'parameters'.
    print("Hello "+first+" "+middle+" "+last)

def hello1(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

# Code
hello(last="three.",middle="two,",first="one,")     # Arguments with keywords.
                                                    # These arguments use keywords to define which argument corresponds
                                                    # to which paramater.

hello1("one,","two,","three.")                      # Positional arguments
                                                    # These arguments use their position to correspond to parameters.