from art import logo

# Define menu
drinks_menu = {
    "espresso": {"ingredients": {"water": 50, "milk": 0, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
    "americano": {"ingredients": {"water": 250, "milk": 0, "coffee": 24}, "cost": 2.0},
}

# Define resources
current_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
    "items_sold": 0
}

# Main function
if __name__ == "__main__":
    print(logo)
    machine_on = True
    while machine_on:
        # Prompt user to choose drink type
        choice = input("What would you like to drink? (espresso/latte/cappuccino/americano): ").lower()
        if choice == "off":
            machine_on = False   # Turn off the machine
            break   # Break the loop if the user chooses to turn off the machine
        elif choice == "report":
            # Generate report if user chooses to see the report
            print(f"Water: {current_resources['water']}ml")
            print(f"Milk: {current_resources['milk']}ml")
            print(f"Coffee: {current_resources['coffee']}g")
            print(f"Money: ${current_resources['money']}")
            print(f"Items sold: {current_resources['items_sold']}")
        elif choice in drinks_menu.keys():
            order = drinks_menu[choice]["ingredients"]
            # Check if resources are sufficient
            sufficient_resources = True
            for item in order:
                if order[item] > current_resources[item]:
                    print(f"Sorry there is not enough {item}.")
                    sufficient_resources = False
                    break
            if sufficient_resources:
                # Prompt user to insert coins
                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickles = int(input("How many nickles?: "))
                pennies = int(input("How many pennies?: "))

                # Calculate total sum of money inserted
                total_sum = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
                drink_cost = drinks_menu[choice]["cost"]

                # Check if user has inserted enough money
                if total_sum < drink_cost:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    print(f"Here is ${(total_sum - drink_cost):.2f} in change.")
                    print(f"Here is your {choice} ☕️. Enjoy!")
                    current_resources["water"] -= order["water"]
                    current_resources["milk"] -= order["milk"]
                    current_resources["coffee"] -= order["coffee"]
                    current_resources["money"] += drink_cost
                    current_resources["items_sold"] += 1
        else: 
            print("Invalid input. Try again!")