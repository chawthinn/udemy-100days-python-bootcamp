"""
This program is a rock, paper, scissors game. 
Player will compete with computer which will randomly choose rock, paper or scissors. 
Rules: 
- Rock wins against scissors.
- Scissors win against paper. 
- Paper wins against rock. 
"""
import random

# Create function to display rock, paper or scissors
def display_pick(choice):
    rock = """✊
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """
    paper = """✋
        ________
    ---'    ____)___
            ________)
             ________)
             _______)
    ---.__________)
    """
    scissors = """✌️
        ________
    ---'    ____)___
            ________)
             ________)
          (____)
    ---.__(___)         
    """
    if choice == 0:
        return rock
    elif choice == 1: 
        return paper
    elif choice == 2: 
        return scissors

# Create function to generate results based on game rules
def rock_paper_scissors_game(player_pick, computer_pick):
    if player_pick == 0: 
        player_choice = display_pick(player_pick)
        computer_choice = display_pick(computer_pick)
        if computer_pick == 0: 
            result = "It's a draw."
        elif computer_pick == 1:
            result = "You lose!"
        else: 
            result = "You win!"
    elif player_pick == 1: 
        player_choice = display_pick(player_pick)
        computer_choice = display_pick(computer_pick)
        if computer_pick == 0: 
            result = "You win!"
        elif computer_pick == 1:
            result = "It's a draw."
        else: 
            result = "You lose!"
    elif player_pick == 2: 
        player_choice = display_pick(player_pick)
        computer_choice = display_pick(computer_pick)
        if computer_pick == 0: 
            result = "You lose!"
        elif computer_pick == 1:
            result = "You win!"
        else: 
            result = "It's a draw."
    else: 
        result = "Invalid choice. Choose 0, 1 or 2!"
    
    return player_choice, computer_choice, result

# Main function
def main():
    try_again = "y" # set try_again as default for multiple tries

    try:
        while (try_again != "n"): # as long as user don't choose "n"

            # randomly generate integer between 0 and 2
            computer_pick = random.randint(0,2)

            # get player input between 0 and 2
            print("What do you choose?")
            player_pick = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

            # Call the rock_paper_scissors_game function
            player_choice, computer_choice, result = rock_paper_scissors_game(player_pick, computer_pick)

            # Display the choices and the result
            print(f"Your choice: \n{player_choice}")
            print(f"Computer's choice: \n{computer_choice}")
            print(result)

            # Let player choose to try again
            print("------------------")
            try_again = input("Try again? (y/n): ")
            if try_again == "n":  # if user chooses "n" to stop trying again
                break
    except ValueError: 
        print("Invalid input.")
    finally:
        print("Exiting the game.")
     
# Run main function
if __name__ == "__main__":
    main()