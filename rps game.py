import random

def computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def user_choice():
    while True:
        user_input = input("Enter your choice (Rock, Paper, or Scissors): ").strip().lower()
        if user_input[:1] in ['r', 'p', 's']:
            return user_input[:1]
        else:
            print("Invalid input. Please enter Rock, Paper, or Scissors.")

def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'r' and computer_choice == 'scissors') or \
         (player_choice == 'p' and computer_choice == 'rock') or \
         (player_choice == 's' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        computer_choice_val = computer_choice()
        player_choice_val = user_choice()
        
        print(f"Computer chose: {computer_choice_val.capitalize()}")
        print(f"You chose: {player_choice_val.capitalize()}")
        
        print(get_winner(player_choice_val, computer_choice_val))
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
