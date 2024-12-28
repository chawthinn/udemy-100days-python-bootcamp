# import word list and stages
from hangman_words import word_list
from hangman_art import stages, logo

# create variable to keep track of number of lives left
lives = 6

# print welcome logo
print(logo)

# randomly choose a word from word_list and assign it to a variable called chosen_word
# then print
import random
chosen_word = random.choice(word_list)

# For each letter in chosen_word, add a _ to placeholder
# so if the chosen_word was "banana" with 6 "_" representing each letter to guess. 
placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print(placeholder)

# Use while loop to let the user guess again
game_over = False
correct_letters = [] # use list to keep record of correcly guess letters
while not game_over:

    # Print count of lives left
    print(f"************{lives}/6 LIVES LEFT************")

    # ask the user to guess a letter and assign their answer to "guess" in lowercase
    guess = input("Guess a letter: ").lower()

    # if user already guessed a letter they already guessed, print the letter 
    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    # Create an empty string called display
    display = ""

    # Loop through each letter in the chosen_word
    # if the letter at that position matches guess then reveal that letter in the display at that position. 
    for index, letter in enumerate(chosen_word): 
        if letter == guess: 
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else: 
            display += "_"
    print(display)
    
    # If guess is not a letter in the chosen_word, reduce lives by 1
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        # If lives goes down to 0, then player lose
        if lives == 0:
            game_over = True
            print(f"************IT WAS {chosen_word}! YOU LOSE************")

    # Player wins if all letters are guessed correctly
    if "_" not in display:
        game_over = True
        print("************YOU WIN************")

    # Print the art
    print(stages[lives])