import random 

# print random integer N such that a <= N <= b
random_integer = random.randint(1, 10)
print(random_integer)

# print random floating-point number between 0.0 <= X < 1.0
random_number_0_to_1 = random.random()
print(random_number_0_to_1)

random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

# print random floating-point number N such that a <= N <= b
random_float = random.uniform(1, 10)
print(random_float)

# print Heads or Tails randomly
random_integer = random.randint(0, 1)
if random_integer == 0: 
    print("Heads")
else:
    print("Tails")

# create a list of states
us_states = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# append an item at the end of the list 
us_states.append("Disneyland")
print(us_states[-1])

# extend the list by appending all items
us_states.extend(["Lalaland", "Legoland"])
print(us_states[-1:-3:-1])

import random
friends = ["Alice", "Bob", "Mary", "Sue", "Jim", "Kelcee"]

# 1st option: print a random element from friends list
print(random.choice(friends))

# 2nd option: generate a random integer as index and use that index to fetch the item in the list
random_index = random.randint(0, 5)
print(friends[random_index])

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozens = [fruits, vegetables]
print(dirty_dozens[-1][-1])