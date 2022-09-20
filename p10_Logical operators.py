# Logical operators (and, or, not) = used to check if two or more conditional statements are true.

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:                        # checks if temp is between 0-30. Due to 'and' condition both conditions need to be true.
    print("The temperature is good today.")
    print("Go outside.")
elif temp < 0 or temp > 30:                         # Checks if temp is less than 0 or more than 30. 'or' statement only requires one condition to be true.
    print("The temperature is bad today.")
    print("Stay inside.")

#if not(temp >= 0 and temp <= 30:)                  # 'not' condition flips the output from true to false or from false to true.


