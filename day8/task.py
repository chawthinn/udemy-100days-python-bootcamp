# function
def greet():
    print("Hello")
    print("Welcome")
    print("How do you do?.")

greet()

# function with parameter
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Welcome {name}")
    print(f"How do you do? {name}")

greet_with_name("John") # pass argument

# life_in weeks function
def life_in_weeks(current_age):
    weeks_left = (90 - current_age) * 52
    print(f"You have {weeks_left} weeks left.")
    
life_in_weeks(30)

# function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"Welcome to {location}")

greet_with("John", "Toronto")
greet_with(location="New York", name="Angela") # define name and location