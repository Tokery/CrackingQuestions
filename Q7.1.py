import random

class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.free = True
    def isFree(self):
        return self.free
    def takeCard(self):
        self.free = False
    def returnCard(self):
        self.free = True

# A deck owns a list of cards
class Deck:
    def __init__(self):
        self.listOfCards = []
        self.nextFreeCard = 0

    def createDeck(self, CardClass):
        for suit in range(4):
            for value in range(13):
                newCard = CardClass(value, suit)
                self.listOfCards.append(newCard)
    
    def shuffleDeck(self):
        newDeck = []
        for x in self.listOfCards:
            chosen = random.randint(0, len(self.listOfCards)-1)
            newDeck.append(self.listOfCards[chosen])
            del self.listOfCards[chosen]
        self.listOfCards = newDeck
    def dealCard(self):
        card = self.listOfCards[self.nextFreeCard]
        self.nextFreeCard += 1
        return card
    def dealHand(self, number):
        # Subtract 1 since you want to deal number - 1 ADDITIONAL cards, not number additional cards
        cards = self.listOfCards[self.nextFreeCard, self.nextFreeCard + number - 1]
        self.nextFreeCard += number

class Hand:
    def __init__(self):
        self.listOfCards = []
    def acceptCard(self, card):
        self.listOfCards.append(card)
    def acceptCards(self, cards):
        self.listOfCards = self.listOfCards + cards

class BlackJackCard(Card):
    def __init__(self, value, suit):
        super(BlackJackCard, self).__init__(value, suit)
    def isAce(self):
        return self.value == 1
    def getValue(self):
        if self.isAce():
            return 1
        return self.value
    def getMaxValue(self):
        if self.isAce():
            return 11
        return self.value

# Some testing code
aceCard = BlackJackCard(1, 2)
print aceCard.getValue()

deck = Deck()
deck.createDeck(BlackJackCard)
deck.shuffleDeck()
someCard = deck.dealCard()
print someCard.getValue()