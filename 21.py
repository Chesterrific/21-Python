"""
deck = [(1,"H"), (2,"H"), (3,"H"), (4,"H"), (5,"H"), (6,"H"), (7,"H"), (8,"H"), (9,"H"), (10,"H"), (11,"H"), (12,"H"), (13,"H"),
        (1,"C"), (2,"C"), (3,"C"), (4,"C"), (5,"C"), (6,"C"), (7,"C"), (8,"C"), (9,"C"), (10,"C"), (11,"C"), (12,"C"), (13,"C"),
        (1,"D"), (2,"D"), (3,"D"), (4,"D"), (5,"D"), (6,"D"), (7,"D"), (8,"D"), (9,"D"), (10,"D"), (11,"D"), (12,"D"), (13,"D"),
        (1,"S"), (2,"S"), (3,"S"), (4,"S"), (5,"S"), (6,"S"), (7,"S"), (8,"S"), (9,"S"), (10,"S"), (11,"S"), (12,"S"), (13,"S")]
"""
def score(hand):
    "Adds up the value of of a hand"
    total = 0               
    card_Val = [item[0] for item in hand]   #takes 1st value from the tuples from the deck, the numerical values of the cards in this case
    for card in card_Val:                       
        if card == 11 or card == 12 or card == 13:  #converts 11-13 to their respective value of 10 to the total
            total += 10
        elif card == 1:   #handles  the case of the ace being either 11 or 1 depending on the score
            if total >= 11: total += 1
            else: total += 11
        else: 
            total += card       #every other card is just worth its own numerical value
    return total

def deal(deck, hands):
    "Deals two cards per hand given"
    num_Of_Hands = len(hands)   #checks for the number of players/hands to be dealt to
    for j in range(2):          #dealing two cards for  the game
        for i in range(num_Of_Hands):
            if len(deck) == 0:
                break
            card = deck.pop(0)   #takes 1st card off deck to prevent duplicates
            hands[i].append(card)   
    return hands
