"""
This program generates password with combinations based on user's inputs.
"""
import string
import random

# Declare the list of letters, integers and symbols    
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
integers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


"""
Easy Version:
This version generates a password where the characters are grouped by type:
- All letters appear first, followed by all symbols, and then all numbers.
Example:
If the user wants 4 letters, 2 symbols and 3 numbers then the password might look like this: dCJq%&901
"""
def generate_password_v1(letters_count, symbols_count, numbers_count):

    password = "" # Initiate an empty string

    # Generate random letters and add them to password string
    for _ in range(1, letters_count+1):
        password += random.choice(letters) 

    # Generate random symbols and add them to password string
    for _ in range(1, symbols_count+1):
        password += random.choice(symbols) 

    # Generate random integers and add them to password string
    for _ in range(1, numbers_count+1):
        password += random.choice(integers) 

    # Return the final password after all characters are added
    return password
    
"""
Hard Version:
Generate a password with random letters, symbols, and numbers, where the final password is fully randomized. Thus, the letters, symbols, and numbers are mixed in random order. 
Example:
If the user wants 4 letters, 2 symbols, and 3 numbers, the password might look like this: d9C&1q%0J
"""
def generate_password_v2(letters_count, symbols_count, numbers_count):

    password_list = [] # Initialize an empty list
    password = "" # Initialize an empty string

    # Generate random letters and add them to password_list
    for _ in range(1, letters_count+1):
        password_list.append(random.choice(letters))

    # Generate random symbols and add them to password_list
    for _ in range(1, symbols_count+1):
        password_list.append(random.choice(symbols))

    # Generate random integers and add them to password_list
    for _ in range(1, numbers_count+1):
        password_list.append(random.choice(integers))

    # Shuffle all characters in password_list
    random.shuffle(password_list)

    # Combine all shuffled characters into password string
    for items in password_list:
        password += items
    
    return password

""" 
Approach #3:
Using random.sample() to generate non-repeated random characters. 
"""
def generate_password_v3(letters_count, symbols_count, numbers_count):
    password_list = []
    password = ""

    # Add random letters, symbols and numbers to password_list
    password_list += random.sample(letters, letters_count)
    password_list += random.sample(symbols, symbols_count)
    password_list += random.sample(integers, numbers_count)

    # Shuffle all characters in password_list
    random.shuffle(password_list)

    # Combine all shuffled characters into password string
    for items in password_list:
        password += items
    
    return password

"""
Using prebuilt collections of string module 
- string.ascii_letters for all lowercase and uppercase letters
- string.digits for all numbers
- string.punctuation for all symbols
This eliminates the need to define separate lists for letters, numbers and symbols.
"""
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

# Main function
def main():
    print("Welcome to the PyPassword Generator!")
    
    # Get user's inputs
    letters_count = int(input("How many letters would you like in your password?\n"))
    symbols_count = int(input("How many symbols would you like in your password?\n"))
    numbers_count = int(input("How many numbers would you like in your password?\n"))

    # Call function and pass user's inputs
    password = generate_password_v4(letters_count, symbols_count, numbers_count)

    # Print password
    print(f"Generated password: {password}")

# Run main function
if __name__ == "__main__":
    main()