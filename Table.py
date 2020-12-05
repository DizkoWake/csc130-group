import random

class Card:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def main():
    deck = []
    cardShapes = {"club", "diamond", "heart", "spade"}
    cardValue = {"ace", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"}
    # Create a 52 unique card objects and populate deck with them.
    for shape in cardShapes:
        for value in cardValue:
          deck.append(Card(cardShape = shape, cardValue = value))

    # shuffle deck
    random.shuffle(deck)

    # We can delete this printing loop later,
    # it's here just to show that deck is filled with anonymous Card objs
    for card in deck:
        print(card.cardShape + " " + card.cardValue) #Don't worry about warnings here, theses fields are created above


#def pullCard():

#def placeCard():

#def viewHand():

#def viewQueue():

main()
