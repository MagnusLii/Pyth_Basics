# Nested function calls =   Function calls inside other function calls.
#                           Innermost function calls are resolved first,
#                           returned value is used as argument for the next outer function.

# Function
num = input("Enter a whole positive number: ")      # Asks user for input and sets that input as variable 'num'
num = float(num)                                    # Converts variable 'num' into floating point number.
num = abs(num)                                      # Converts variable 'num' into it's absolute value.
num = round(num)                                    # Rounds the variable 'num'.
print(num)                                          # Prints 'num'.

# Nested Function
print(round(abs(float(input("Enter a whole positive number: ")))))  # Does the same as above except in one line of code.
