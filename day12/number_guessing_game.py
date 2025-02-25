import random

def generate_num():
    """This function will generate a random number between 1 and 100 and return the number."""
    num = random.randint(1, 100)
    return num


if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    correct_choice = generate_num()
    count = 0
    while True:
        user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if user_choice == "easy": 
            count = 10
            break
        elif user_choice == "hard": 
            count = 5
            break
        else:
            print("Invalid choice. Please type 'easy' or 'hard'.")
    while count != 0:
        print(f"You have {count} attempts remaining to guess the number.")
        try: 
            guess = int(input("Make a guess: "))
            if guess < 1 or guess > 100:
                print("Guess a number between 1 and 100.")
                continue
            elif guess == correct_choice: 
                print(f"You guess correct! The correct number is {correct_choice}.")
                break
            elif guess < correct_choice:
                count -= 1
                if count == 0:
                    break
                print("Too low. Guess again.") 
            elif guess > correct_choice:
                count -= 1
                if count == 0:
                    break
                print("Too high. Guess again.")
        except ValueError: 
            print("Invalid input. Enter a number between 1 and 100.")
    if count == 0:
        print(f"You've run out of guesses. Correct number was {correct_choice}.")