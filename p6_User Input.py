# User input

#input("what is your name?:")                                               # Asks for user input. By default user input is always string data.
name = input("What is your name?: ")                                        # Assigns variable based on user input.
age = int(input("How old are you?: "))                                      # Same as before except the variable is turned into an integer to allow math.
age = age + 1                                                               # Example of birthday.
height = float(input("How tall are you?: "))                                # Same as before but float datatype, allowing the input of decimal numbers.

print("Hello "+name)
print("You are "+str(age)+" years old.")                                    # Printing age after addition and conversion.
print("You are "+str(height)+"cm tall.")