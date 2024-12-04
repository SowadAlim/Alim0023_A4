import random


def get_computer_choice():
    """Randomly select a choice for the computer."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(player_choice, computer_choice):
    """Determine the winner of the game."""
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "paper" and computer_choice == "rock") or
            (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"


def play_game():
    """Play a round of Rock, Paper, Scissors."""
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'quit' to exit the game.")

    while True:
        player_choice = input("\nEnter your choice: ").lower()

        if player_choice == "quit":
            print("Thanks for playing! Goodbye!")
            break

        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)


# Run the game
if __name__ == "__main__":
    play_game()
