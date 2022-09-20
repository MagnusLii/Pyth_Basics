# Nested loops = The "inner loop" will finish all of it's iterations before finishing one iteration of the "outer loop".
#                Basically a loop within a loop.

# Variables
rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):                                   # Outer loop, controls rows. Using range function.
    for j in range(columns):                            # Inner loop. controls columns. Using range function.
        print(symbol, end="")                           # end="" prevents the print commands from moving down to the next line once it's done printing.
                                                        # Note this is the command executed by the inner loop.
    print()                                             # Same as before except for the outer loop.