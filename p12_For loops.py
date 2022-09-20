# for loop = a statement that will execute it's block of code for a limited amount of times.

        # while loop = unlimited
        # for loop = limited

import time                                             # Import time module for use in countdown.


#for i in range(10):                                     # A for loop that counts up to 10.
#    print(i)

#for I in range(50,100+1):                               # range = 50-100. (second value is exclusive thus +1)
#    print(I)

#for j in name:                                          # runs a loop for the word or variable.
#    print(j)


for seconds in range(10,0,-1):                          # creates a countdown, starting at 10, ending at 0 and counting down by 1.
    print(seconds)                                      # prints current value of 'seconds'.
    time.sleep(1)                                       # sets a delay of 1 second before going back to top and continuing countdown.
print("Happy new year!")                                # What happens after the countdown has finished.




