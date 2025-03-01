from art import logo

# Function to get the drink requirements
def get_drink_requirements(drink_type):
    requirements = {
        "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1.5},
        "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
        "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0}
    }
    return requirements[drink_type]

# Function to get the drink cost
def get_drink_cost(drink_type):
    return get_drink_requirements(drink_type)["cost"]

# Function to check if resources are available to make the drink
def check_resources(drink_type):
    
    current_res = generate_report()
    res = get_drink_requirements(drink_type)
    if res["water"] > current_res["water"]:
        print("Sorry there is not enough water.")
        print(f"required: {res["water"]} -> available: {current_res["water"]}")
    elif res["milk"] > current_res["milk"]:
        print("Sorry there is not enough milk.")
        print(f"required: {res["milk"]} -> available: {current_res["milk"]}")
    elif res["coffee"] > current_res["coffee"]:
        print("Sorry there is not enough coffee.")
        print(f"required: {res["coffee"]} -> available: {current_res["coffee"]}")
    else: 
        return True

# Function to generate report showing current resource values
def generate_report():
    current_resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0
    }
    print(f"Water: {current_resources['water']}ml")
    print(f"Milk: {current_resources['milk']}ml")
    print(f"Coffee: {current_resources['coffee']}g")
    print(f"Money: ${current_resources['money']}")
    return current_resources

# Function to get coins from buyer
def get_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    sum = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    
    # debug
    print(sum)

    return sum
    

print(logo)

choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

while True:

    if choice == "report":

        # Call the function to generate report
        generate_report()

        # Ask user for choice again
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    else:
        print("stop here")

        # Check if resources are available to make latte
        if check_resources(choice) == True:

            # Ask user to insert coins
            buyer_money = get_coins()

            cost = get_drink_cost(choice)

            # Check if user has inserted enough money
            if buyer_money < cost:
                print("Sorry that's not enough money. Money refunded.")
            else: 
                print(f"Here is ${(buyer_money - cost):.2f} in change.")
                print(f"Here is your {choice} ☕️. Enjoy!")