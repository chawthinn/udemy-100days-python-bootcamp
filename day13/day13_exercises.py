def my_function():
    for i in range(1, 20):
        if i == 19:
            print("You got it!")

my_function()

from random import randint
dice_images = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
dice_num = randint(0,5)
print(dice_images[dice_num])

year = int(input("What's your year of birth? "))

if year >= 1980 and year <= 1994: 
    print("You are a millennial.")
elif year > 1994: 
    print("You are a Gen Z.")

try:
    age = int(input("How old are you? "))
    if age >= 18: 
        print(f"You can drive at age {age}.")
    else: 
        print(f"You cannot drive at age {age}.")
except ValueError: 
    print("Invalid input.")

word_per_page = 0
pages = int(input("Number of page: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(f"Total words: {total_words}")

import random 

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list: 
        new_item = item * 2
        new_item += random.randint(1,3)
        new_item = new_item + item
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])