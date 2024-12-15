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
    rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """
    paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    """
    scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """
    if choice == 0:
        print(rock)
    elif choice == 1: 
        print(paper)
    elif choice == 2: 
        print(scissors)

# Create function to generate results based on game rules
def rock_paper_scissors_game(player_pick, computer_pick):
    if player_pick == 0: 
        display_pick(player_pick)
        print("Computer chose:")
        if computer_pick == 0: 
            display_pick(computer_pick)
            print("It's a draw.")
        elif computer_pick == 1:
            display_pick(computer_pick)
            print("You lose!")
        else: 
            display_pick(computer_pick)
            print("You win!")
    elif player_pick == 1: 
        display_pick(player_pick)
        print("Computer chose:")
        if computer_pick == 0: 
            display_pick(computer_pick)
            print("You win!")
        elif computer_pick == 1:
            display_pick(computer_pick)
            print("It's a draw.")
        else: 
            display_pick(computer_pick)
            print("You lose!")
    elif player_pick == 2: 
        print("Computer chose:")
        display_pick(player_pick)
        if computer_pick == 0: 
            display_pick(computer_pick)
            print("You lose!")
        elif computer_pick == 1:
            display_pick(computer_pick)
            print("You win!")
        else: 
            display_pick(computer_pick)
            print("It's a draw.")
    else: 
        print("Invalid choice. Choose 0, 1 or 2!")

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

            # call rock_paper_scissors_game function
            rock_paper_scissors_game(player_pick, computer_pick)

            # let player choose to try again
            print("------------------")
            try_again = input("Try again? (y/n) ")
            if try_again == "n": # if user choose "n" to stop trying again
                break
    except ValueError: 
        print("Invalid input.")
    finally:
        print("Exiting the game.")
     
# Run main function
if __name__ == "__main__":
    main()