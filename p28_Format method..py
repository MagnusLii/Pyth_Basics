# str.format() =    Optional method for strings that gives users more control when displaying output.


# Variables.
animal = "cow"
item = "moon"
text = "The {} jumped over the {}."
name = "hun"
number = 1000

# Demonstration.
print("The "+animal+" jumped over the "+item)               # Standard print statement.
print("The {} jumped over the {}".format(item,animal))      # Same statement using format format fields.
                                                            # The curly brackets "{}" denote the fields and the
                                                            # "format()" command fills them.

print("The {1} jumped over the {1}".format(item,animal))    # Positional arguments can be placed inside the brackets.
print("The {item1} jumped over the {animal1}".format(item1="cow",animal1="BIG COW"))

print(text.format(animal,item))                             # Formatting the var 'text' which has inbuilt format fields.

print("Hello, myname is {}, who are you?".format(name))
print("Hello, myname is {:10}, who are you?".format(name))  # ':10' inside the brackets adds 10 empty spaces to the
                                                            # right by default.
print("Hello, myname is {:>10}, who are you?".format(name))
print("Hello, myname is {:<10}, who are you?".format(name)) # > and < can be used to add padding before/after the value.
print("Hello, myname is {:^10}, who are you?".format(name)) # ^ centres the value inbetween your padding.


# Formatting numbers.
print("The number is {:.2f}".format(number))                # :.2f displays two floating point numbers after the '.'.
print("The number is {:,}".format(number))                  # :, automatically adds a comma to all 1000s places.
print("The number is {:b}".format(number))                  # :b displays the value as binary.
print("The number is {:o}".format(number))                  # :o displays the value as octal.
print("The number is {:x}".format(number))                  # :x displays the value as lowercase hexadecimal.
print("The number is {:X}".format(number))                  # :X displays the value as all uppercase hexadecimal.
print("The number is {:e}".format(number))                  # :e displays the number as scientific notation.
print("The number is {:E}".format(number))                  # :E same as above, except in uppercase.