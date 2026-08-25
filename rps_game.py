import random


def main():
    print("Hello!! This is Rock Paper Scissors Game. Enjoy it!!")
    print()
    print("Rules:")
    print("Rock beats scissors.")
    print("Scissors beats paper.")
    print("Paper beats rock.")
    print("If both players choose the same option, it is a tie.")
    print()

    player_choice = input("Enter rock, paper, or scissors: ")

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print("You selected:", player_choice)
    print("Computer selected:", computer_choice)


if __name__ == "__main__":
    main()