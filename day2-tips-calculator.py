"""
1. display welcome message
2. prompt for total bill
3. prompt to choose how much tips
4. prompt to ask how many people splitting
5. calculate tip for each person
6. display the result

"""
# Deinfe a function to calculate 
def calculate_bill_per_person(bill, tips_percentage, pax_count):
    
    tips_amount = bill * ( tips_percentage / 100 )

    total_bill = bill + tips_amount

    payable_per_pax = total_bill/ pax_count

    return payable_per_pax

# Execute functions in Main Program
if __name__ == "__main__":

    print("Welcome to the tip calculator!")

    try: 
        # Validate bill input
        bill = float(input("What was the total bill? "))
        if bill <= 0:
            raise ValueError("Total bill should be a positive number.")
        
        # Validate tips_percentage input
        tips_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
        if tips_percentage not in [10,12,15]:
            raise ValueError("Tips percentage should be 10, 12 or 15.")

        pax_count = int(input("How many people to split the bill? "))
        if pax_count < 0: 
            raise ValueError("Total count of people should be a positive number.")
    
        # Call function to calculate the tips
        tips_per_pax = calculate_bill_per_person(bill, tips_percentage, pax_count)
        print(f"Each person should pay: {tips_per_pax:.2f}")

    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")