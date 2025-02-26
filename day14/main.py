# Import the necessary libraries
import random
from art import logo, vs
from game_data import data

# Function to get the details of the choice
def get_details(choice):
	return {
		'name': choice['name'],
		'description': choice['description'],
		'country': choice['country'],
		'follower_count': choice['follower_count']
	}

# Function to compare the follower count
def compare(count_a, count_b):
	return 'A' if count_a > count_b else 'B'

# Initialize the score
score = 0

# Loop until the user gets the wrong answer
while True:

	# Get two random choices and get the details
	random_a, random_b = random.sample(data, 2)
	choice_1 = get_details(random_a)
	choice_2 = get_details(random_b)

	# Print the logo and the choices
	print(logo)
	print(f"Compare A: {choice_1['name']}, a {choice_1['description']}, from {choice_1['country']}.")
	print(vs)
	print(f"Compare B: {choice_2['name']}, a {choice_2['description']}, from {choice_2['country']}.")

	# Prompt the user to guess
	user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
	
	# Break the loop if the user gets the wrong answer
	if user_guess != compare(choice_1['follower_count'], choice_2['follower_count']):
		print(f"Sorry, that's wrong. Final score: {score}.")
		break

	# Increment the score if the user gets the right answer
	score += 1
	print(f"You're right! Current score: {score}.")