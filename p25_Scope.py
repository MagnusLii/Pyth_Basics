# Scope =   The region that a variable is recognized.
#           A variable is only available from inside the region it is created.
#           A global and locally scoped versions of a variable can be created.


name = "Bleegh"                     # Global scope. (Available anywhere)

def display_name():
    name = "Hunnie"                 # Local scope. (Available only inside this function)
    print(name)                     # If the same variable exists locally and globally the local var will be prioritized.

# Python follows "LEGB" ordering, Local -> Enclosed -> Global -> Built-in.

display_name()                      # Calling the function to print a local var 'name'.
print(name)                         # Printing the global var 'name'.