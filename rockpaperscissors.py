import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_player_choice():
    choice = input("Enter your choice (rock/paper/scissors): ")
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid choice. Enter your choice (rock/paper/scissors): ")
    return choice

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
        (player_choice == 'scissors' and computer_choice == 'paper') or \
        (player_choice == 'paper' and computer_choice == 'rock'):
        return "Player wins!"
    else:
        return "Computer wins!"

def play_game():
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    print(f"Player chose {player_choice}")
    print(f"Computer chose {computer_choice}")
    print(determine_winner(player_choice, computer_choice))

if __name__ == "__main__":
    play_game()