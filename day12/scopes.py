enemies = 1 # global scope

def increase_enemies():
    enemies = 2 # local scope
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside functon: {enemies}")

# There is no block scope in python

game_level = 10
enemies = ['Skeleton', 'Zombie', 'Alien']

def create_new():
    new_enemy = "" # Initialize the variable
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

create_new()

enemies = 1 # global scope

def increase_enemies(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1

enemies = increase_enemies(10)
print(f"enemies outside function: {enemies}")