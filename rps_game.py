import random


def determine_winner(player, computer):
    if player == computer:
        return "tie"

    if (
        (player == "rock" and computer == "scissors")
        or (player == "scissors" and computer == "paper")
        or (player == "paper" and computer == "rock")
    ):
        return "player"

    return "computer"


def play_round(round_number):
    print()
    print("Round", round_number)

    player_choice = input("Enter rock, paper, or scissors: ")

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print("You selected:", player_choice)
    print("Computer selected:", computer_choice)

    result = determine_winner(player_choice, computer_choice)

    if result == "tie":
        print("It's a tie! Rematch!")
    elif result == "player":
        print("You win!")
    else:
        print("Computer wins!")

    return result


def main():
    print("Hello!! This is Rock Paper Scissors Game. Enjoy it!!")
    print()
    print("Rules:")
    print("Rock beats scissors.")
    print("Scissors beats paper.")
    print("Paper beats rock.")
    print("If both players choose the same option, it is a tie.")
    print()

    round_number = 1

    while True:
        result = play_round(round_number)

        if result != "tie":
            break

        round_number += 1


if __name__ == "__main__":
    main()
