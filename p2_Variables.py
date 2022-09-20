# Variable = a container for value. Behaves as a value that it contains.
first_name = "Hunnie"                               # variable with a sring as a value.
last_name = "brah"
full_name = first_name +" "+ last_name              # Combining two variables and an empty space within another variable.
print("Hello " +full_name)                          #Printing string"Hello" and variable 'name'.


# Integers

age = 21                                           # Integer variable, note integers are not within "" marks. Only store whole numbers.
age = age + 3                                      # Can also be written as "age += 1"

#print(age)                                         # Prints age.
#print(type(age))                                   # Prints the type of variable used.

#print("Your age is: "+(age))                       # Will not work cause of mixing two different variable types.
print("Your age is: " +str (age))                  # "str" converts the int variable into a string which allows us to combine it with another string. Also called typecasting.


# Floating point numbers

height = 250.5                                     # Float number. Is a number that contains decimal points.


# Booleans                                         # Useful for if statements.

human = False                                      # Booleans are true/false values.
print("Are you human: "+str(human))                # Example print command using Boolean with typecasting.