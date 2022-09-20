import os

source = "31_textfile_copy.txt"                         # Variable for the file we'll be moving.
destination = "C:\\Users\\Mage\\desktop\\test.txt"      # Variable for the location well move it to.

try:
    if os.path.exists(destination):                     # If statement to check if the path/file already exists.
        print("There is already a file there.")
    else:
        os.replace(source,destination)                  # Moves the file from src to dst.
        print(source+" was moved.")
except FileNotFoundError:                               # exception if the 'source' path is empty.
    print(source+" was not found.")