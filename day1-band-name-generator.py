"""
This program can generate the band name based on your inputs: 
the city that you grew up in 
your pet's name

Steps: 
1. prompt to collect the name of the city
2. prompt to collect the pet's name
3. combine two strings and display as band name
"""

# Define function to generate band name
def generate_band_name(first_string, second_string):
    
    result = first_string + " " + second_string
    return result

# Execute function in Main Program
if __name__ == "__main__":

    # Prompt welcome message
    print("Welcome to the Band Name Generator.")

    # Collect name of the city
    first_string = input("What's the name of the city you grew up in?\n")

    # Collect pet's name
    second_string = input("What's your pet's name?\n")

    # Call function and display band name
    print(f"Your band name could be {generate_band_name(first_string, second_string)}")