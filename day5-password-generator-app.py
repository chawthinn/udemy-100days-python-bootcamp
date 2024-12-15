import string
import random
import streamlit as st
import time

# Create session state variables
if "last_clicked" not in st.session_state:
    st.session_state.last_clicked = time.time() 
if "generated_password" not in st.session_state:
    st.session_state.generated_password = ""
if "first_click" not in st.session_state:
    st.session_state.first_click = True  # Track if it's the first click
if "countdown" not in st.session_state:
    st.session_state.countdown = 0  # Store the countdown timer

# Define rate limiting parameters
rate_limit_interval = 6  # Time interval in seconds

# Function to load file content
def load_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# Load CSS and HTML content
footer_css = load_file("footer.css")
footer_html = load_file("footer.html")

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
    # Check the time of the last button click
    current_time = time.time()

    # Check if the rate limit interval has passed and if it's not the first click
    if not st.session_state.first_click and current_time - st.session_state.last_clicked < rate_limit_interval:
        time_remaining = rate_limit_interval - (current_time - st.session_state.last_clicked)
        st.session_state.countdown = int(time_remaining)  # Update countdown
        st.warning(f"Please wait {st.session_state.countdown} seconds before trying again.")
    else:
        # Update the session state time and generate the password
        st.session_state.last_clicked = current_time
        st.session_state.generated_password = generate_password(letters_count, symbols_count, numbers_count)
        
        # Mark first click as complete
        st.session_state.first_click = False

        # Display the password with copy-to-clipboard
        st.success("🎉 Password generated!")
        st.code(st.session_state.generated_password)

# Display countdown in real-time
if st.session_state.countdown > 0:
    for i in range(st.session_state.countdown, 0, -1):
        st.session_state.countdown = i
        st.experimental_rerun()  # Rerun the app to update the countdown every second

# Add Spacer
st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

# Inject CSS into the app
st.markdown(f"<style>{footer_css}</style>", unsafe_allow_html=True)

# Add the footer HTML
st.markdown(footer_html, unsafe_allow_html=True)