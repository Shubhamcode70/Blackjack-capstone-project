import random

cards_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#User Initial Deck
user_deck = []
card1_user = random.choice(cards_deck)
card2_user = random.choice(cards_deck)
card3_computer = random.choice(cards_deck)
user_deck = [card1_user, card2_user]
user_initial_score = sum(user_deck)
#print(user_deck)

print(f"Your Hand is {user_deck} And Your Score is {user_initial_score}")

computer_deck = [card3_computer]
computer_initial_score = sum(computer_deck)
print(f"Computer's First card is {computer_deck} And Computer Sccore is {computer_initial_score}")

user_choice = input("Do you want to get another card press 'y' to continue and 'n' to pass")
if user_choice == "y": # check when user want to get card
    new_user_deck = [] + user_deck
    new_user_deck.append(random.choice(cards_deck))
    user_final_score = sum(new_user_deck)
    
    print(f"Your Hand is {new_user_deck} And Your Score is {user_final_score}")
    
    new_computer_deck = [] + computer_deck
    new_computer_deck.append(random.choice(cards_deck))
    computer_finale_score = sum(new_computer_deck)
  
    print(f"Computer Final Hand is {new_computer_deck} And Computer Score is {computer_finale_score}")

    if user_final_score > 21:
        print("You Lose the Game")
    elif computer_finale_score > 21:
        print("Computer lose the game! You won")
    elif computer_finale_score <= 21 and computer_finale_score > user_final_score:
        print("Computer won the game! You Lose")
    elif user_final_score <= 21 and user_final_score > computer_finale_score:
        print("You won the game! Computer Lose")
    elif computer_finale_score == user_final_score:
        print("Its a Draw!")
    else:
        print("Something went wrong")
else:# check when user use pass
    #computer Score with apend - that is revealing its card
    new_computer_deck = [] + computer_deck
    new_computer_deck.append(random.choice(cards_deck))
    computer_finale_score = sum(new_computer_deck)
    
    print(f"Computer Final Hand is {new_computer_deck} And Computer Score is {computer_finale_score}")
    
    user_deck = [card1_user, card2_user]
    user_initial_score = sum(user_deck)
    #print(user_deck)

    print(f"Your Hand is {user_deck} And Your Score is {user_initial_score}")
    
    if user_initial_score > 21:
        print("You Lose the Game")
    elif computer_finale_score > 21:
        print("Computer lose the game! You won")
    elif computer_finale_score <= 21 and computer_finale_score > user_initial_score:
        print("Computer won the game! You Lose")
    elif user_initial_score <= 21 and user_initial_score > computer_finale_score:
        print("You won the game! Computer Lose")
    elif computer_finale_score == user_initial_score:
        print("Its a Draw!")
    else:
        print("Something went wrong")