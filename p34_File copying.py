# copyfile() =  copies contents of a file.
# copy() =      copyfile() + permission mode 0 destination can be a directory.
# copy2() =     copy() + copies metadata (file's creation and modification times).


import shutil                                               # Module that enables above commands.

shutil.copyfile("p31_textfile.txt", "31_textfile_copy.txt")   # shutil.copyfile(src, dst), PC filepaths can be used.

