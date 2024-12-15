# app.py
import streamlit as st
from day4_rock_paper_scissors import display_pick, rock_paper_scissors_game
import random

# Streamlit App
st.title("Rock, Paper, Scissors Game")

# Display game instructions
st.markdown("### Choose Rock, Paper, or Scissors:")

# Radio buttons to select Rock, Paper, or Scissors
player_pick = st.radio("What do you choose?", ["Rock", "Paper", "Scissors"])

# Map the player input to numbers (Rock=0, Paper=1, Scissors=2)
choices = ["Rock", "Paper", "Scissors"]
player_choice = choices.index(player_pick)

# Generate a random computer choice
computer_pick = random.randint(0, 2)
computer_choice = choices[computer_pick]

# Display the choices
st.write(f"Your choice: {player_pick}")
st.image(display_pick(player_choice), use_column_width=True)

st.write(f"Computer's choice: {computer_choice}")
st.image(display_pick(computer_pick), use_column_width=True)

# Display result
result = rock_paper_scissors_game(player_choice, computer_pick)
st.write(f"Result: {result}")

# Option to try again
if st.button("Play Again"):
    st.experimental_rerun()