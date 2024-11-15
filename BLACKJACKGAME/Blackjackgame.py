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
class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        self.dealer_hand = []
    
    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
        


'''
Using a class within another class
'''
class Deck(Card):
    
    def __init__(self):
        self.all_cards = [] 
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
                
#testing...
mydeck = Deck()
# This will be where the cards will go after the dealer hands them out
Player_one_cards = []
mydeck.all_cards
#This will be the player class that will be used in the game logic
class Player(Deck):
    
    def __init__(self, name, BA):
        Deck.__init__(self)
        self.BA = BA
        self.name = name
        self.player_hand = []
        pass
        
    def Stand():
        pass
    
    def shuffle(self):
        return random.shuffle(self.all_cards)
    
    def Hit(self):
        self.player_hand.append(self.all_cards.pop(-1))
        for index in self.player_hand:
            print(f'This is your card: {index} and you have {len(self.player_hand)} cards ')
 
        pass
    
    def value_of_card(self):
        for num in self.all_cards:
            print(num)
        
    
myplayer = Player("player one",500)

#testing..

len(myplayer.all_cards)

#Dealer Class is gonna be made with attributes and methods and will also be used in game logic

class Dealer(Deck):
    
    def __init__(self):
        Deck.__init__(self)
        self.dealer_hand = []
        
        
    def Hit(self):
        self.dealer_hand.append((self.all_cards.pop(-1)))
        for index in self.dealer_hand:
            print(f'This is your card: {index} and you have {len(self.dealer_hand)} cards left')
            
    def Stand(self):
        print(f'You have 17 or more cards left; {len(self.dealer_hand)}')
        if len(self.dealer_hand) >= 17:
            user_input = input('End of Round; no more cards will be given to you, Y or N?')
            if user_input == 'y'.upper():
                print('Thank you for playing, wait for results')
            else:
                pass
mydealer = Dealer()
        
#testing...

player_one = Player('One', 500)
dealer_one = Dealer('Sam')
len(dealer_one.dealer_hand)
len(player_one.all_cards)

myplayer.Hit()
myplayer.Hit()
mydealer.Hit()
mydealer.Hit()
def player_turn():
    choice = input("Welcome to blackjack, if you would like to 'hit' type hit and if you would like to 'pass' type pass").lower()
    while True:
        if choice == 'hit':
            pass

if 1+1 == 2:
    print('1 plus 1 equals 2')









#def dealer_turn():


#Im going to compare player.all_cards and dealer.all_cards, and make sure that if a card is moved from one variable, the same card is moved from the other variable
#Try to find [name of card] in player.player_hand and see if it is in self.all_cards, use a boolean


   
   
