# To play a hand of Blackjack the following steps must be followed:

#     Create a deck of 52 cards
#     Shuffle the deck
#     Ask the Player for their bet
#     Make sure that the Player's bet does not exceed their available chips
#     Deal two cards to the Dealer and two cards to the Player
#     Show only one of the Dealer's cards, the other remains hidden
#     Show both of the Player's cards
#     Ask the Player if they wish to Hit, and take another card
#     If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
#     If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
#     Determine the winner and adjust the Player's chips accordingly
#     Ask the Player if they'd like to play again

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
          'Queen':10, 'King':10, 'Ace':11}
playing = True

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.deck.append(created_card)
    
    def __str__(self):
        return self.deck

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()

# test_deck = Deck()
# test_deck.shuffle()
# for i in test_deck.deck:
#     print(i)

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        if type(card) == type([]):
            self.cards.extend(card)
        else:
            self.cards.append(card)
    
    def adjust_for_ace(self):
        pass

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        pass
    
    def lose_bet(self):
        pass

def take_bet():
    
    pass

def hit(deck,hand):
    
    pass

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    pass

def show_some(player,dealer):
    
    pass
    
def show_all(player,dealer):
    
    pass

def player_busts():
    pass

def player_wins():
    pass

def dealer_busts():
    pass
    
def dealer_wins():
    pass
    
def push():
    pass

