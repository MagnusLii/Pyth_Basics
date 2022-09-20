# While loop = a statement that will execute it's block of code, as long as it's condition(s) remain true.

#while 1==1:                                               # while keeps executing a program as long as the conditions are true.
#    name = print("Help! I'm stuck in a loop!")

name = ""
while len(name) == 0:
    name = input("Enter your name: ")                      # Keeps prompting the user for a name as long as the 'name' var remains empty.

print("Hello "+name)
