# list = used to store multiple items in a single variable.

food = ["pizza", "hamburger", "spaghetti", "hotdog"]    # squarebrackets allows the addition of multiple items under one variable.

# editing lists.
food[0] = "sushi"                                       # replaces item 0 with 'sushi'.
food.append("ice cream")                                # adds 'ice cream' to the end of the list.
food.remove("hotdog")                                   # removes 'hotdog' from the list.
food.pop()                                              # pop function removes whatever the last item on the list is.
food.insert(0, "cake")                                  # insert function adds 'cake' to position 0.
food.sort()                                             # sorts the list alphabetically.
food.clear()                                            # removes all the elements from the list.


#print(food[0])                                          # print specific items in the list.

for x in food:                                          # for loop, indexes all items in list.
    print(x)                                            # prints all items in list.