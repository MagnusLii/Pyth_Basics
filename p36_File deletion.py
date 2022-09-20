import os
import shutil                                   # Needed for deleting folders containing files.

# variables.
path = "C:\\Users\\Mage\\desktop\\test.txt"
path1 = "test"


try:
    #os.remove(path)                             # basic remove command, cannot delete folders/directories.
    #os.rmdir(path)                              # command for removing folders. Short for "remove directory".
    shutil.rmtree(path1)                        # Command for deleting folders containing files.
                                                # Short for "remove tree"

# Error handling.
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("Permission denied.")
except OSError:
    print("You cannot delete that using that function.")
else:
    print(path1+" was deleted")