# We'll use this later
import random 
import time
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
    
    def __init__(self, name,deck):
        Deck.__init__(self)
        self.name = name
        self.player_hand = []
        self.deck = deck
        pass
        
    def Stand():
        pass
    
    
    def Hit(self):
        self.player_hand.append(mydeck.deal_one())
    
    def bet(self,bet):
        print("$" + bet)
        pass
        
        
        
        
 
    
    def value_of_card(self):
        counter = 0
        for card in self.player_hand:
            counter += card.value
            
        if counter > 21:
            for card in self.player_hand:
                if card.rank == 'Ace':
                    counter -= 10
        return counter

    
        
    


#testing......


#Dealer Class is gonna be made with attributes and methods and will also be used in game logic

class Dealer(Deck):
    
    def __init__(self, deck):
        Deck.__init__(self)
        self.dealer_hand = []
        self.deck = deck
        pass
        
        
    def Hit(self):
        self.dealer_hand.append(mydeck.deal_one())

        
            
    def Stand(self):
        pass

    def value_of_card(self):
        total = 0
        for card in self.dealer_hand:
            total += card.value
        return total

#Create player and dealer, sharing a single deck through arguments
myplayer = Player("player one", mydeck)
mydealer = Dealer(mydeck)
        
#testing...


#GAME LOGIC


#Deal two cards to player and dealer
myplayer.Hit()
myplayer.Hit()
mydealer.Hit()
mydealer.Hit()


#Player turn
def player_turn():
    game_on = True
    num_of_round = 0
    testing = True
    num_of_round += 1
    global round
    round = 0
    while testing:
        try:
            choice = int(input("Welcome to blackjack, how many games would you like to play?").lower())
            round += choice
            testing = False  # Exit the loop if input is a valid integer
        except ValueError:
            print("Invalid input. Please enter an integer.")
        while testing == False and game_on == True:


            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            print(f'Game {num_of_round} of {choice}')
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            print("Your hand:")
            for card in myplayer.player_hand:
                print(card)
            print("Values:",myplayer.value_of_card())
            print("\n")
            print("Dealer's hand:")
            for card in mydealer.dealer_hand[0:1]:
                print(card)
            print("Hidden Card")
            print("Values:",)
            print("\n")
            
            #User Input
            sec_choice = input("Please choose 'Hit' or 'Stand':").lower()
    
            if sec_choice == 'Hit'.lower():
                myplayer.Hit()
            elif sec_choice == 'Stand'.lower() or sec_choice == 'Quit'.lower():
                break
            if myplayer.value_of_card() > 21:
                num_of_round += 1
                print("\n")
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                print("Player BUSTS, Dealer wins!")
                print("Final Value:",myplayer.value_of_card())
                print('Final Card:', myplayer.player_hand[-1] )
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                print("\n")
                break


print('shuffling...')   
time.sleep(4)
print('Place your bets')
wager = input('How much would you like to wager? Note: The maximum bet is $2,500.')
myplayer.bet(wager)
print('@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('Choose: Grey:1, Black:10, Blue: 100, or Green: 500')
print('@@@@@@@@@@@@@@@@@@@@@@@@@@')
time.sleep(4)            
player_turn()

            

def dealer_turn():
    while mydealer.value_of_card() <= 17:
        mydealer.Hit()
        
        
    print("Dealer's hand:")
    for card in mydealer.dealer_hand:
        print(card)
    print("Values:", mydealer.value_of_card())
    print("\n")    
    
    if mydealer.value_of_card() > 21:
        print("\n")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print("Dealer BUSTS, you win!")
        print("\n")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    
    
    elif mydealer.value_of_card() > myplayer.value_of_card():
        print("\n")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print("Dealer Wins!")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print("\n")
        
    elif myplayer.value_of_card() > mydealer.value_of_card():
        print("You win!")
    
    else:
        print("\n")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print("Draw!")
        print("\n")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    

if myplayer.value_of_card() <= 21:
    dealer_turn()
else:
    pass


#def play_again():
    #if round > 1:
        #player_turn()
        #dealer_turn()
    #else:
        #pass


