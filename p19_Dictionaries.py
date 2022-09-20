# dictionary =  a changeable, unordered collection of unique  key:value pairs.
#               Fast because they use hashing, allow us to access a value quickly.


# dictionary exmp.
capitals = {"USA":"Washington DC",          # dictionary, in format "Key:value".
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}

# updating dictionaries.
capitals.update({"Germany":"Berlin"})       # Adds the 'key:value', Germany:Berlin to the dictionary.
capitals.update({"usa":"Las Vegas"})        # Updates the 'key' of USA with 'value' Las Vegas.
capitals.pop("China")                       # Removes a 'key' and it's associated 'value'.
#capitals.clear()                            # Clears everything in the dictionary.

# Useful commands
print(capitals["Russia"])                   # Fetches the value associated with key "Russia".
#print(capitals["Germany"])                  # Searches for a value with key that does not exist in dictionary.
print(capitals.get("Germany"))              # The 'get' function allows us to search if the key
                                            # 'Germany' exists in the dictionary.
print(capitals.keys())                      # Prints all keys found in dictionary.
print(capitals.values())                    # Prints all values in dictionary.
print(capitals.items())                     # Prints entire dictionary.
for key, value in capitals.items():         # A 'for loop' that prints all 'key' and 'value' values in the dictionary.
    print(key,value)