import random

while True:

    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors?: ").lower()
        if player != choices:
            print("Choose from: rock, paper, scissors")

    if player == computer:
        print("Computer: ", computer)
        print("Player: ", player)
        print("Tie :/")
    elif player == "rock":
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose. Try next time :)")
        elif computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win! Good job :D")
    elif player == "paper":
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose. Try next time :)")
        elif computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win! Good job :D")
    elif player == "scissors":
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose. Try next time :)")
        elif computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win! Good job :D")

    play_again = input("Play again? (y/n): ").lower()

    if play_again != "y" or play_again != "yes":
        break

print("Bye then!")
