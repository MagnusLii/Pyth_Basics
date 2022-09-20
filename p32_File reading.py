# Reading files.


try:                                                            # Try block to enable exception handling.

    with open("p31_textfile.txt") as file:    # 'with' statement https://www.geeksforgeeks.org/with-statement-in-python/
                                                                # 'open' opens the specified file, 'as' defines it as
                                                                # the following keyword, "file" in this case.

        print(file.read())                                      # 'file.read' reads the contents of the file and 'print'
                                                                # prints them in the console.

except FileNotFoundError:                                       # An exception error for if the file is not found.
    print("That file was not found :(")

print(file.closed)                                              # 'file.closed' checks if the file is closed and prints
                                                                # true if closed, fasle if still open.
                                                                # The 'with' command closes files automatically.