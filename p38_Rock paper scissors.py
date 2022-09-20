import random

while True:
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors?: ").lower()

    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("Player loses!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("Player wins!")
    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("Player loses!")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("Player wins!")
    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("Player loses!")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("Player wins!")
    Play_again = input("Play again? (yes/no): ").lower()
    if Play_again != "yes":
        break
print("Bye!")