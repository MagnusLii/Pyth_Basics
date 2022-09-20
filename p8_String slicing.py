# Slicing = creating a substring by extracting elements from another string
#                   indexing[] or slice()                   # Both are commands used for slicing.
#                   [start:stop:step]                       # Three optional arguments to fill depending on how we wish to index.


#Indexing
name = "Hunnie Lastname"

#first_name = name[0:6]                                     # Index using the start and stop arguments.
                                                            # Note start is inclusive while stop is exclusive therefore does not include the letter it stops on.
first_name = name[:6]                                       # Start index defaults to 0

#last_name = name[7:15]                                     # Same as above.
last_name = name[7:]                                        # A blank stop index simply includes all remaining characters in the string.

funky_name = name[::2]                                      # Step = how much we increase our index between start and stop. Default is 1.
                                                            # Outputs name except is only counts every second letter.

reversed_name = name[::-1]                                  # Reverses input for output.


print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)



#Slicing

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)                                         # Same as index above except using a negative stop value, therefore it counts backwards.

print(website1[slice])
print(website2[slice])                                      # Same slicing method can be reused to reformat common values.