# app.py
import streamlit as st
import random
from day4_rock_paper_scissors import display_pick, rock_paper_scissors_game
from footer_utils import load_footer

# Streamlit App
st.title("Rock, Paper, Scissors Game")
st.info("""
ℹ️ Rules: 
- Rock wins against scissors.
- Scissors win against paper. 
- Paper wins against rock.
""")

# Inputs
player_choice = st.radio("Choose your pick: ✊✋✌️", ["Rock", "Paper", "Scissors"])

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
    st.code(player_choice_result,  language=None)  # ASCII art for player's choice
    st.write("Computer chose:")
    st.code(computer_choice_result)  # ASCII art for computer's choice

    # Show the result
    if result == "You lose!":
        st.error("🙁" + result)
    elif result == "You win!":
        st.success("🥳" + result)
    else: 
        st.info("🤷" + result)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Display the footer with the dynamic day number
day_number = 4
footer_html = load_footer(day_number)
st.markdown(footer_html, unsafe_allow_html=True)