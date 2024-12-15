import string
import random
import streamlit as st

# Function to load external files
def load_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# Load CSS and HTML
footer_css = load_file("footer.css")
footer_html = load_file("footer.html")

# Inject CSS and HTML into the Streamlit app
st.markdown(f"<style>{footer_css}</style>", unsafe_allow_html=True)

# Password generation functions
def generate_password(letters_count, symbols_count, numbers_count):
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
st.title("🔐 PyPassword Generator")
st.markdown("Generate secure, random passwords with your choice of letters, symbols, and numbers.")

# Inputs
st.subheader("📝 Select your password criteria:")
letters_count = st.number_input("How many letters?", min_value=0, value=4)
symbols_count = st.number_input("How many symbols?", min_value=0, value=2)
numbers_count = st.number_input("How many numbers?", min_value=0, value=3)

# Generate button
if st.button("🔄 Generate Password"):
    # Generate password
    password = generate_password(letters_count, symbols_count, numbers_count)

    # Display the password with copy-to-clipboard
    st.success("🎉 Password generated! Hover to copy to clipboard.")
    st.code(password)

# Inject Footer HTML at the end
st.markdown(footer_html, unsafe_allow_html=True)