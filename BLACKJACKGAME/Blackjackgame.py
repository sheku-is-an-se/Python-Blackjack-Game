# We'll use this later
import random 
'''This is the outside variables of the cards'''
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
'''
Creating a Card Class with outside variables¶
Here we will use some outside variables that we know don't change regardless of the situation, such as a deck of cards. Regardless of what round,match, or game we're playing, we'll still need the same deck of cards

'''

'''
Methods:(DECK CLASS)
__init__(self): The constructor method to initialize the deck. This method should create all 52 cards and add them to the cards attribute.
shuffle(self): A method to shuffle the cards in the deck randomly.
deal_card(self): A method to remove and return the top card from the deck.
cards_left(self): A method to return the number of cards remaining in the deck.
__str__(self): A method to provide a string representation of the deck (optional).
'''
class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
        

new_deck = []
'''
Using a class within another class
'''
class Deck(Card):
    
    def __init__(self):
        self.shared_deck = []
        for suit in suits:
            for rank in ranks:
                self.shared_deck.append(Card(suit,rank))
    def deal_one(self):
        return self.shared_deck.pop()

    def shuffle(self):
        random.shuffle(self.shared_deck)
    

    
#testing...
mydeck = Deck()


mydeck.shuffle()
#This will be the player class that will be used in the game logic
class Player(Deck):
    
    def __init__(self, name):
        Deck.__init__(self)
        self.name = name
        self.player_hand = []
        pass
        
    def Stand():
        pass
    
    
    def Hit(self):
        self.player_hand.append(mydeck.deal_one())
        for card in self.player_hand:
            print(card)
        
        
        
 
    
    def value_of_card(self):
        for object in self.player_hand:
            if object.rank == 'King' or object.rank == 'Queen' or object.rank == 'Jack' :
                print('10')
            else:
                print(object.rank)
        
        
    
myplayer = Player("player one")

#testing......


#Dealer Class is gonna be made with attributes and methods and will also be used in game logic

class Dealer(Deck):
    
    def __init__(self):
        Deck.__init__(self)
        self.dealer_hand = []
        
        
    def Hit(self):
        self.dealer_hand.append(mydeck.deal_one())

        
            
    def Stand(self):
        print(f'You have 17 or more cards left; {len(self.dealer_hand)}')
        if len(self.dealer_hand) >= 17:
            user_input = input('End of Round; no more cards will be given to you, Y or N?')
            if user_input.upper() == 'Y':
                print('Thank you for playing, wait for results')
            else:
                pass
mydealer = Dealer()
        
#testing...


#GAME LOGIC


#Deal two cards to player and dealer
myplayer.Hit()
myplayer.Hit()
mydealer.Hit()
mydealer.Hit()


#Player turn
game_on = True
def player_turn():
    while game_on:
        choice = input("Welcome to blackjack, if you would like to 'hit' type hit and if you would like to 'stand' type stand").lower()
        if choice == 'hit':
            myplayer.Hit()
        elif choice == 'stand':
            break

player_turn()





#Im going to compare player.all_cards and dealer.all_cards, and make sure that if a card is moved from one variable, the same card is moved from the other variable
#Try to find [name of card] in player.player_hand and see if it is in self.all_cards, use a boolean

type(myplayer.player_hand)
myplayer.value_of_card()
for key in myplayer.player_hand:
    print(key)

myplayer.player_hand[5]

myplayer.rank