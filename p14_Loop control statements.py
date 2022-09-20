# Loop control statements = change a loops execution from it's normal sequence.

# break =       used to terminate the loop entirely.
# continue =    skips to the next iteration of the loop.
# pass =        does nothing, acts as a placeholder.

# break usage.

while True:                                     # Starts a loop.
    name = input("Enter your name: ")           # code that is looped.
    if name != "":                              # the loop continues as long as the 'if' statement is true, aka name = empty.
        break                                   # once the loops conditions are met, the code moves to this line, break here stops the loop.



# continue usage.

phone_number = "123-456-789"

for i in phone_number:                          # For each character in our number do...
    if i == "-":                                # If any of the characters equal a '-' then...
        continue                                # continue the loop w/o indexing the '-'.
    print(i, end="")                            # The loop prints it's indexed data, 'end=""' means the print statement
                                                # ends with an empty space rather that skipping to next line.


# pass usage.

for j in range(1,21):                           # Counts through the numbers 1-20 by assigning them to j.
    if j == 13:                                 # checks if the value of j = 13.
        pass                                    # if j = 13 then it passes, aka does nothing and continues the code.
    else:
        print(j)                                # if j =/= 13, then j is printed.
