#------------------------------------------------------------
def new_game():                                                         # Defines function 'new_game', called at start and on line 77.

    guesses = []                                                        # Variable for guesses, def empty. Is updated with players answers on line 17.
    correct_guesses = 0                                                 # Variable to keep track of correct guesses.
    question_num = 1                                                    # Variable to keep track of the question asked.

    for key in questions:                                               # For loop that runs for every 'key' in the 'questions' dictionary at the bottom.
        print("------------------------------------------------------------")
        print(key)                                                      # Prints the 'key' value which in our dictionary is always the question.

        for i in options[question_num-1]:                               # a nested loop that checks which question is being asked and then prints the choices from the
                                                                        # the 'options' 2d list at the bottom.
            print(i)
        guess = input("Enter (A, B, C or D): ")                         # Asks the user to input their answer and defines it as 'guess' variable.
        guess = guess.upper()                                           # Converts 'guess' into uppercase.
        guesses.append(guess)                                           # Adds the users guess into the 'guesses' list for the scoreboard at the end.

        correct_guesses += check_answer(questions.get(key),guess)       # Uses the 'check_answer' function to add points to the 'correct_guesses' variable for each correct answer.
        question_num += 1                                               # Adds 1 to the 'question_num' variable as by now the player has completed the currecnt question and is moving on.

    display_score(correct_guesses, guesses)                             # Once all questions are asked the 'display_score' function is called.
#-----------------------------------------------------------
def check_answer(answer, guess):                                        # The 'anwser' parameter is filled on line 19 and and the 'guess' parameter is defined as a variable on lines 15 and 16.
                                                                        # This function is only called on by line 19.
    if answer == guess:
        print("Correct")
        return 1                                                        # returns 1 for the 'correct_guesses' variable point tally on line 19.
    else:
        print("Incorrect")
        return 0                                                        # As above but returns a 0.
#-----------------------------------------------------------
def display_score(correct_guesses, guesses):                            # This function is called on line 22.
    print("------------------------------------------------------------")
    print("Results")
    print("------------------------------------------------------------")

    print("Answers: ", end="")
    for i in questions:                                                 # For loop, 'i' is the number of loops run, used to run through the questions one by one.
        print(questions.get(i), end=" ")                                # checks the value of 'i' (line above) and prints the corresponding question from 'questions' dictionary.
    print()                                                             # used to create a line break.

    print("Guesses: ", end="")
    for i in guesses:                                                   # For loop that runs for each 'i' index in 'guesses' variable line 4.
        print(i, end=" ")                                               # Prints the current value of 'i' aka the answer submitted on line 17 from the 'guesses' variable on line 4.
    print()

    score = int((correct_guesses/len(questions))*100)                   # Creates a score for the player by comparing the value of var 'correct_guesses' line 5 to the number of items in the
                                                                        # questions dictionary.
    print("Your score is: "+str(score)+"%")                             # prints the final tally as a percentage.
#-----------------------------------------------------------
def play_again():                                                       # called on line 78
    response = input("Do you want to play again? (yes or no):")
    response = response.upper()

    if response == "YES":                                               # if player says 'yes' it sets the value to true, used on line 78.
        return True
    else:
        return False
#-----------------------------------------------------------



questions = {                                                           # Dictionary defined as 'questions'.
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],  # 2d list named 'options'.
           ["A. 1989", "B. 1991", "C. 2000", "D.2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. Sometimes", "D. What's Earth?"]]

new_game()

while play_again():                                                     # as long as the value of 'play_again' function remains 'True' (line 52) this loop keeps going.
    new_game()                                                          # Runs the 'new_game' function on line 2.

print("Bye")                                                            # Only runs if the while loop on line 78 is closed.