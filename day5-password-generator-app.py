import string
import random
import streamlit as st

# Password generation functions
def generate_password_v4(letters_count, symbols_count, numbers_count):
    password_list = []
    password = ""

    # Generate random letters, symbols, and numbers using random.choices()
    letters = random.choices(string.ascii_letters, k=letters_count)
    symbols = random.choices(string.punctuation, k=symbols_count)
    numbers = random.choices(string.digits, k=numbers_count)

    # Combine all characters into password_list
    password_list = letters + symbols + numbers

    # Shuffle the list for randomness
    random.shuffle(password_list)

    # Combine all shuffled characters into password string
    for items in password_list:
        password += items
    
    return password

# Streamlit App
st.title("PyPassword Generator")
st.text("Here you can generate password with your choice of random letters, symbols and numbers.")

# Inputs
letters_count = st.number_input("How many letters?", min_value=0, value=4)
symbols_count = st.number_input("How many symbols?", min_value=0, value=2)
numbers_count = st.number_input("How many numbers?", min_value=0, value=3)

# Generate password button
if st.button("Generate Password"):
    password = generate_password_v4(letters_count, symbols_count, numbers_count)
    st.success(f"Passowrd generated!")
    st.text_input("Copy your password", value=password, key="password_input", disabled=True)
    st.code(password)
