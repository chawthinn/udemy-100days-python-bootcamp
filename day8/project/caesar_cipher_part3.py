import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Combine both encrypt and decrypt functions
def caesar(input_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in input_text:
        if letter not in alphabet: # if letters are not alphabet, keep them as is
            output_text += letter
        else: 
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {output_text}") 

repeat = True
while repeat:
    # Get user input
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Function calls based on user's input
    caesar(input_text=text, shift_amount=shift,encode_or_decode=direction)

    # Ask user to repeat 'yes' or 'no'
    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no':\n")
    if repeat == 'no':
        repeat = False
        print("Good bye!")