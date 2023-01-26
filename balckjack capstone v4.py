import random
from replit import clear
from blackjackart import logo

def deal_card():
    """Returns a random card From Deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards as Inout and return the score"""
    #if 11 in cards and 10 in cards and len(cards) == 2:
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(user_score, computer_score):
    """Compare the Score of the user and Return the Result"""
    if user_score == computer_score:
        return "Draw 😉"
    elif computer_score == 0:
        return "Lose, The opponent has BlackJack💀"
    elif user_score == 0:
        return "Win, With a Blackjack😎"
    elif computer_score > 21:
        return "opponent Went Over, You Win! 😂"
    elif user_score > 21:
        return "You Went Over, opponent Win! 😢"
    elif user_score > computer_score:
        return "You Win! 🎇"
    else:
        return "You Lose!"
    
#Creating User Deck ans Computer Deck
def blackjack():
    print(logo)
    user_deck = []
    computer_deck = []

    is_game_over = False

    for card in range(2):
        user_deck.append(deal_card())
        computer_deck.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_deck)
        computer_score = calculate_score(computer_deck)
        print(f"Your cards are {user_deck} and your score is {user_score}")
        print(f"computer first card is {computer_deck[0]}")

        if user_score == 0 or computer_score == 0 and user_score > 21:
            is_game_over = True
        else:
            user_want_deal = input("Type 'y' to get another card, type 'n' to pass : ")
            if user_want_deal == "y":
                user_deck.append(deal_card())
            else:
                is_game_over = True    
                
    while computer_score != 0 and computer_score < 17 :
        computer_deck.append(deal_card())
        computer_score = calculate_score(computer_deck)
    
    print(f"Your final deck is {user_deck} Your final score is {user_score}")   
    print(f"computer final deck is {computer_deck} and Computer final score is {computer_score}")
    print(compare(user_score, computer_score))

    while input("Do You want to play again ? Enter 'y' to restart the game") == 'y':
        clear()
        blackjack()
        
blackjack()