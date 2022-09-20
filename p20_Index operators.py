# index operator [] =   gives access to a sequence's element, include but not limited to (str,list,tuples)
#                       used via the square brackets []

# variables
name = "hunnie hun"

if(name[0].islower()):                  # If statement checking if 0'th index of var 'name' is lowercase.
    name = name.capitalize()            # This command capitalizes the first letter of var 'name'
                                        # if prev statement is true.

first_name = name[0:6].upper()          # Creates a new variable by taking first 6 indexed values of var 'name'
                                        # and turns them all uppercase.

last_name = name[7:].lower()            # As above.

last_character = name[-1]               # Finds the last character.

print(name)
print(first_name)
print(last_name)
print(last_character)