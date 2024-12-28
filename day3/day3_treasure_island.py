"""
This program will run Treasure Island game where program prompts player different choices. Based on the choice, user finally win or game over. 
"""
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
first_choice = input("left or right? ").lower()
if first_choice == "left": # if player choose left
    second_choice = input("swim or wait? ").lower()
    if second_choice == "wait": # if player choose wait
        third_choice = input("Which door? (Red, Blue, Yellow) " ).lower()
        if third_choice == "red": # if player choose red
            print("Burned by fire.\nGame Over.")
        elif third_choice == "blue": # player choose blue
            print("Eaten by beasts.\nGame Over.")
        elif third_choice == "yellow": # player choose yellow
            print("You Win!")
        else: # anything else
            print("Game Over.")
    else: # if player choose swim or anything else
        print("Attacked by trout.\nGame Over.")
else: # if player choose right or anything else
    print("Fall into a hole.\nGame Over.")
