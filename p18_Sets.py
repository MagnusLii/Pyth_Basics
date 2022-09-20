# set = collection which is unordered, unindexed. No duplicate values.

# sets.
utensils = {"fork" ,"spoon","knife"}                # Curly brackets = set.
dishes = {"bowl","plate","cup","knife","knife"}     # Despite multiple knives when searched the set will only ever display one.

# set mofification.
utensils.add("napkin")                              # Adding element to set.
utensils.remove("fork")                             # Removing element from set.
utensils.clear()                                    # Clears the set completely.
dishes.update(utensils)                             # Adds elements from utensils into dishes.
dinner_table = utensils.union(dishes)               # Adds two sets together to create a third set.

# comparing sets.
print(dishes.difference(utensils))                  # Prints what 'dishes' has that 'utensils' does not.
print(utensils.intersection(dishes))                # Finds common elements in 'utensils' and 'dishes'.


for x in dinner_table:                              # Prints all the values in 'dinner_table'.
    print(x)