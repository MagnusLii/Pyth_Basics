# *args =   Parameter that will pack all arguments into a tuple useful so that a function
#           can accept a varying amount of arguments.

def add(*stuff):                        # The * denotes that this is arg
    sum = 0                             # Creates variable named 'sum' with default value of 0.

    #stuff = list(stuff)                 # Since tuples are unchangeable we need to cast it (as a list) in order
                                         # to allow editing values.
    #stuff[0] = 0                        # Changes the first value in 'stuff' to be 0.

    for i in stuff:                     # For loop.
        sum += i                        # Adds 'sum' to 'i'
    return sum                          # Sets the value from previous line as the value for 'sum'.

print(add(1,2,3))