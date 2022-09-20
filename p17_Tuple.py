# tuple = Collection which is ordered and unchangeable, used to group together related data.

student = ("bro", 21, "male")

print(student.count("bro"))                             # Counts how many times the value of "bro" appears and prints the answer.
print(student.index("male"))                            # Finds index value of 'male'.

for x in student:                                       # For loop to print all the values of tuple.
    print(x)

if "bro" in student:                                    # if check for specific values in tuple.
   print("bro is here")