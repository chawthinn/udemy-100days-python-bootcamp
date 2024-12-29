alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

"""
# Encrypt function
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        new_position = alphabet.index(letter) + shift_amount
        new_position %= len(alphabet)
        cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")

# Decrypt function
def decrypt(cipher_text, shift_amount):
    original_text = ""
    for letter in cipher_text:
        original_position = alphabet.index(letter) - shift_amount
        original_position %= len(alphabet)
        original_text += alphabet[original_position]
    print(f"The decoded text is {original_text}") 
"""

# Combine both encrypt and decrypt functions
def caesar(input_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in input_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"The decoded text is {output_text}") 

# Function calls based on user's input
caesar(input_text=text, shift_amount=shift,encode_or_decode=direction)