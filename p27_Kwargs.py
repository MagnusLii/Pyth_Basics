# **kwargs =    Parameter that will pack all arguments into a dictionary, useful so that a function
#               can accept a varying amount of keyword arguments.

#               Args accept varying amount of positional arguments and pack them into tuples,
#               kwargs accept varying keyword arguments and pack them into dictionaries.


# Regular function with two keywords.
#def hello(first, last):                                         # Only accepts two arguments.
    #print("Hello " + first + " " + last)                        # Cannot be used by someone with three names.



# Kwarg function.
def hello2(**kwargs):                                           # The two ** denote this as a kwarg.
    #print("Hello " + kwargs['first'] + " " + kwargs['last'])   # The standard way to use kwargs, using the command
                                                                # 'kwargs', "['word']" denotes the keyword we wish to use.

    # Adaptive code that displays someone's full name based on the amount of keywords entered.
    print("Hello",end=" ")                                      # Starts by printing 'Hello', end=" " means the code
                                                                # won't skip to next line but will instead end with an empty space.

    for key,value in kwargs.items():                            # For loop that iterates through each key value pair
                                                                # in the 'kwargs' dictionary.

        print(value,end=" ")                                    # prints each value.

# Function values.
#hello(first="Bro",middle="Dude",last="Code")
hello2(title="Mr.",first="Bro",middle="Dude",last="Code")
