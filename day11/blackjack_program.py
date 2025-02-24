import random

def deal_card():
    """This function returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """This function takes a list of cards and return the score calculated from the cards"""

    # Retrun 0 if the sum of the cards is 21 and the length of the cards is 2
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    # Remove 11 from the cards if there's an ace in the cards and the sum is greater than 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)   

def compare(u_score, c_score):
    """This function compares the user's score and the computer's score and return the result"""
    if u_score == c_score: 
        return "Draw!"
    elif u_score == 0:
        return "You win with a Blackjack!"
    elif c_score == 0:
        return "Computer wins with a Blackjack!"
    elif u_score > 21:
        return "You went over. You lose!"
    elif c_score > 21:
        return "Computer went over. You win!"
    elif u_score > c_score: 
        return "You win!"
    elif u_score < c_score:
        return "You lose!"
    
def play_game():
    """This function runs the game of Blackjack"""
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    # Deal the cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    # Loop through the game
    while not is_game_over:
        # Calculate the scores and display the cards
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check if the game is over
        if user_score == 0 or computer_score == 0 or user_score > 21: 
            is_game_over = True
        else: 
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else: 
                is_game_over = True

    # Let the computer run its turn
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Display the final scores
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()