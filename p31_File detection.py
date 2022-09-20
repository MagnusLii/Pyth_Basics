# Basic file detection.

import os                                           # Imports OS module.


path = "C:\\Users\\Mage\\Desktop\\test.txt"         # Defining a file location as var 'path', double backslashes are
                                                    # needed as that's the escape sequence for a backslash.

if os.path.exists(path):                            # Checks if the path exists.
    print("That location exists!")
    if os.path.isfile(path):                        # Checks if it's a file
        print("That is a file.")
    elif os.path.isdir(path):                       # checks if the path is a folder aka directory.
        print("That is a directory.")
else:                                               # if the path is invalid/does not exist.
    print("That location doesn't exist!")