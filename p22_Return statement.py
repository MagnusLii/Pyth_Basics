# return statement =        Functions that send python values/objects back to the caller.
#                           These values/objects are known as the function's return value.

# Functions
def multiply(number1,number2):              # 'Defining' the 'function' "multiply" and it's 'parameters'.
    #result = number1 * number2              # defining the result of multiplication code as a variable.
    #return result                           # returning the result

    return number1 * number2                # does the same as above code except shorter.

# Variables
x = multiply(6,8)                           # storing the returned value as a variable

# code
print(x)