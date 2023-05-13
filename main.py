import random

# Define the game options
options = ["rock", "paper", "scissors"]

# Define the game function
def play_game():
    # Get player choice
    player_choice = input("Choose rock, paper, or scissors: ")

    # Validate player choice
    if player_choice not in options:
        print("Invalid choice.")
        return

    # Get computer choice
    computer_choice = random.choice(options)

    # Print choices
    print("Player: " + player_choice)
    print("Computer: " + computer_choice)

    # Determine winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("Computer wins!")

# Play the game
play_game()
