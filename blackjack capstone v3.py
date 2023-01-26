import random
# user_deck = [deal_card, deal_card]
# computer_deck = [deal_card, deal_card]

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(user_deck:list, computer_deck:list):
    
    print(f" User Deck {user_deck} computer deck {computer_deck}")
    user_score = sum(user_deck)
    computer_score = sum(computer_deck)
    
    if user_deck == [11, 10] or user_deck == [10, 11]:
        return 0
    elif computer_deck == [11, 10] or computer_deck == [10, 11]:
        return 0
    else:  
        for ace in user_deck:
            if ace == 11 and user_score >= 21:
                user_deck.remove(11)
                user_deck.append(1)
                user_score = sum(user_deck)
            elif ace == 11 and user_score == 10:
                ace = 11
            elif ace == 11 and user_score <= 21:
                user_deck.remove(11)
                user_deck.append(11)
                user_score = sum(user_deck)
            else:
                user_score = sum(user_deck)
                
        for ace in computer_deck:
            if ace == 11 and computer_score >= 21:
                computer_deck.remove(11)
                computer_deck.append(1)
                computer_score = sum(computer_deck)
            elif ace == 11 and computer_score == 10:
                ace = 11
            elif ace == 11 and computer_score <= 21:
                computer_deck.remove(11)
                computer_deck.append(11)
                computer_score = sum(computer_deck)
            else:
                computer_score = sum(computer_deck)
        # print(user_score, computer_score)      
        
            # if len(user_deck) == 2 and ace == 11 and user_deck[ace] == 10:
    user_choice = input("Do You want to draw a card or pass ? Press 'y' to to draw card or 'n' to pass \n")
    if user_choice == "y":
        user_deck.append(deal_card)
        computer_deck.append(deal_card)
        return declare_winner(user_score, computer_score)
    elif user_choice == "n": 
        return declare_winner(user_score, computer_score)
  
    return user_score, computer_score, user_choice
    
    
    
#calculate_score(user_deck, computer_deck)
# user_choice = input("Do You want to draw a card or pass ? Press 'y' to to draw card or 'n' to pass \n")

# def draw_cards(user_choice):
#     if user_choice == "y":
#         user_deck.append(deal_card)
#         computer_deck.append(deal_card)
        
#     elif user_choice == "n": 
#         return declare_winner
    
def declare_winner(user_score:int, computer_score:int):
    if user_score > 21:
        print("You Lose the Game")
    elif computer_score > 21:
        print("Computer lose the game! You won")
        
    elif computer_score <= 21 and computer_score > user_score:
        print("Computer won the game! You Lose")
    elif user_score <= 21 and user_score > computer_score:
        print("You won the game! Computer Lose")
    elif computer_score == user_score:
        print("Its a Draw!")
    else:
        print("Something went wrong")
        

user_deck = [deal_card(), deal_card()]
computer_deck = [deal_card(), deal_card()]
calculate_score(user_deck, computer_deck)

