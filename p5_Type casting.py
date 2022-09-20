# Type casting = Convert the data type of a value to another data type.

x = 1                                   # Integer
y = 2.0                                 # Float
z = "3"                                 # String

y = int(y)                              # Permanently converts Y into an integer.
x = str(x)                              # Converts X into string.
z = float(z)                            # Converts Z into a floating point number.

print(int(y))                           # Converts Y into an integer. Not permanent.
print("X is "+x)
#print("Z is "+z)                        # Does not work as you cannot display a string alongside an integer/float.
print("Z is "+str(z))                   # Converts Z into a string thus allowing both to be displayed.