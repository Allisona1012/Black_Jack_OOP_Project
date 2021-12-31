import random

# suits = ['Diamonds','Hearts','Spades', 'Clubs']
# values = [1,2,3,4,5,6,7,8,9,10,10,10,10,11] 
# cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
# deck = [(v,s) for v in values for s in suits]


class Card:
    #What makes a card? suits and numbers.
    #this is "making" the card
    def __init__(self, suits, values, symbol):
        self.suits = suits
        self.values = values
        self.symbol = symbol
    #this is showing what the card is.    
    def show_card(self):

            print(self.suit,self.symbol)
        
        
        
    def __repr__(self,card):
        return f'{self.value} of {self.suit}'    

        
class Deck:
    #what makes a deck? 52 cards
    def __init__(self, cards):
        self.how_many_cards = cards
        self.deck =[]

    # make a deck
    def make_a_deck(self):
        suits = ['Diamonds','Hearts','Spades', 'Clubs']
        values = [2,3,4,5,6,7,8,9,10,10,10,10,11] 
        cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.deck = [(v,s) for v in values for s in suits]
        for card in self.deck:
            self.deck.append(card)
            
        
    #check to see if the deck is working
    def show_deck(self,deck):
        for card in self.deck:
            card.show_card()
        
    #This is going to shuffle the deck    
#     def shuffle_deck(self):
#         random.shuffle(deck)
#         return (deck)
#         print(deck)

deck1 = Deck(52)
deck1.make_a_deck()
deck1.show_deck(deck1)

print(deck1)