
text = "Appendix complete."                                         # Text var, '\n' is the newline character.

#with open("p31_textfile.txt","w") as file1:                          # The second argument in the 'open' command is 'w'
                                                                    # for write. By default, 'open' only reads the file.
                                                                    # This will overwrite not add to the file.

with open("p31_textfile.txt", "a") as file1:                          # 'a' in the open command stands for append, it adds
                                                                    # to rather than overwrites the opened file.

    file1.write(text)                                               # Command to write to 'file1' using the string in
                                                                    # variable 'text'.