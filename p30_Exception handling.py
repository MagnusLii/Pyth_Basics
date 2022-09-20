# exception = events detected during execution that interrupt the flow of a program.

try:                                                                # 'Try' block, useful when code could cause errors.
                                                                    # It tries each block of code looking for if a
                                                                    # following condition such as 'except' is met.
    numerator = float(input("Enter a number to divide: "))
    denominator = float(input("Enter a number to divide by: "))
    result = numerator / denominator                                # This code can result in many errors as it requires
                                                                    # unsupervised user input.

except ZeroDivisionError as e:                                      # 'except' checks for and activates if the specified
                                                                    # error occurs, in this case the error is dividing
                                                                    # by 0.
                                                                    # 'as e' sets the python exception error as var 'e',
                                                                    # this is optional put allows you to catch the
                                                                    # the actual error.
    print(e)                                                        # Creates an error for user when they attempt to
    print("You can't divide by zero! Idiot!")                       # divide by 0.

except ValueError as e:                                             # Creates an error for user when user attempts to
    print(e)                                                        # a value that is not a number.
    print("Enter only number plz")

except Exception as e:                                              # A general exception error for when something
    print(e)                                                        # unspecified goes wrong.
    print("Something went wrong. :(")

else:
    print("The result is: "+str(result))                            # If no errors are met the result is printed.

finally:                                                            # 'finally' is a clause that always executes whether
                                                                    # an error is met or not.
    print("code has been executed.")