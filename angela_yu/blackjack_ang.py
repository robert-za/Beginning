import os, random
from bj_art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return cards[random.randint(0, 12)]

def calculate_score(hand):
    score = 0
    for card in hand:
        score += card
        if score > 21:
            for card in hand:
                if card == 11:
                    card = 1
    return score

def print_hand_score(hand):
    if hand == player_hand:
        print(f"    Your cards: {player_hand}, final score: {player_score}")
    elif hand == card_dealer_hand:
        print(f"    Computer's hand: {card_dealer_hand}, final score: {card_dealer_score}")

def print_dealer_card():
    print(f"    Computer's first card is: {card_dealer_hand[0]}")

def check_score():
    if player_score == 21 and card_dealer_score < 21:
        print("You win. :)")
    elif player_score <= 21 and player_score > card_dealer_score:
        print("You win. :)")
    elif player_score <= 21 and (card_dealer_score > 21):
        print("You win. :)")
    elif player_score == 21 and card_dealer_score == 21:
        print("Draw. :|")
    elif player_score == card_dealer_score:
        print("Draw. :|")
    else:
        print("You lose. :(")

###########################################################################################
######################################GAME#################################################
###########################################################################################

if input("Do you want to play a Black Jack game? y or n: ") == "y":
    play_game = True
    player_score = 0
    card_dealer_score = 0
    player_hand = [deal_card(), deal_card()]
    card_dealer_hand = [deal_card(), deal_card()]

print(logo)
player_score = calculate_score(player_hand)
card_dealer_score = calculate_score(card_dealer_hand)
if player_score == 21:
    while card_dealer_score <= 17:
            card_dealer_hand.append(deal_card())
            card_dealer_score = calculate_score(card_dealer_hand)
    

print_hand_score(player_hand)
print_dealer_card()

while play_game:
    if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
        player_hand.append(deal_card())
        player_score = calculate_score(player_hand)
        if player_score > 21:
            print_hand_score(player_hand)
            print_hand_score(card_dealer_hand)
            check_score()
            play_game = False
            os.system("clear")
        else:
            print_hand_score(player_hand)
            print_dealer_card()
    else:
        player_score = calculate_score(player_hand)
        print_hand_score(player_hand)
        while card_dealer_score <= 17:
            card_dealer_hand.append(deal_card())
            card_dealer_score = calculate_score(card_dealer_hand)
        print_hand_score(card_dealer_hand)
        check_score()
        play_game = False
        os.system("clear")