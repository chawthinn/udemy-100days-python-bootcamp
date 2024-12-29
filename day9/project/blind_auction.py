import art
print(art.logo)

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

# Create function to get highest bidder and bid
def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    highest_bidder = ""

    for bidder, bid in bidding_dictionary.items():
        if bid > highest_bid: 
            highest_bid = bid
            highest_bidder = bidder
        
    print(f"The winner is {highest_bidder} with a bid of {highest_bid}.")

# Get user input
bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: "))

    # Add to dictionary
    bids[name] = price

    # Continue bidding
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == 'no':
        continue_bidding = False
        # Call function to get highest bidder and highest bid
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        print("\n" * 20) # to clear the output