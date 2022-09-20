name = "hunnie"

print(len(name))                                        # Prints lenght of string.
print(name.find("un"))                                  # Looks for first instance of character within string and gives it's numeric placement within string.
print(name.capitalize())                                # Will capitalize first letter of string, does not work on additional words/sentences beyond the first.
print(name.upper())                                     # Turns entire string uppercase.
print(name.lower())                                     # Turns string lowercase.
print(name.isdigit())                                   # Returns true/false statement depending on if string is a digit or not.
print(name.isalpha())                                   # Same as previous except for alphapetical characters, note spaces don't count as alphapetical.
print(name.count("n"))                                  # Counts how many matching characters are within the string.
print(name.replace("n","m"))                            # Replaces all defined characters within string.
print(name*3)                                           # Multiplies string by set number.