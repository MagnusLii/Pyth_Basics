# if statement = code that executes only if a condition is true.

age = int(input("How old are you?: "))                  # input for age

if age >= 18:                                           # If statement comparing the value of age to condition.
    print("You are an adult.")                          # Output if true.
elif age <= 0:
    print("you haven't been born yet.")                 # elseif statement to check an additional condition.
elif age == 100:                                        # elif statement to check if you're 100 years old.
                                                        # note that one (=) is to assign a value (==) is for checking equality.
                                                        # note that the order of if statements is important.
    print("You are a century old.")
else:
    print("You are a child.")                           # Output if false. Else is a last resort condition.
