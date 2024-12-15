# app.py
import streamlit as st
from day4_rock_paper_scissors import display_pick, rock_paper_scissors_game
import random

# Streamlit App
st.title("Rock, Paper, Scissors Game")

# Display game instructions
st.markdown("### Choose Rock, Paper, or Scissors:")

# Streamlit UI setup
st.title("Rock, Paper, Scissors Game")

# Player's move input
player_choice = st.radio("Choose your move:", ["Rock", "Paper", "Scissors"])

# Mapping player input to a number (0 = Rock, 1 = Paper, 2 = Scissors)
if player_choice == "Rock":
    player_choice_number = 0
elif player_choice == "Paper":
    player_choice_number = 1
else:
    player_choice_number = 2

# Create a button to start the game
if st.button("Play Game"):
    # Randomly select the computer's choice (0 = Rock, 1 = Paper, 2 = Scissors)
    computer_choice_number = random.randint(0, 2)

    # Get the result of the game
    player_choice_result, computer_choice_result, result = rock_paper_scissors_game(player_choice_number, computer_choice_number)

    # Show the choices made
    st.write("You chose:")
    st.text(player_choice_result)  # ASCII art for player's choice
    st.write("Computer chose:")
    st.text(computer_choice_result)  # ASCII art for computer's choice

    # Show the result
    st.success(result)