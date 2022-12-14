from random import shuffle
import time

# Blackjack
class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def face(self):
        return self.value + ' ' + self.suit
    
    def score(self):
        scores = {'Ace' : (1, 11),
                  '2' : 2,
                  '3' : 3,
                  '4' : 4,
                  '5' : 5,
                  '6' : 6,
                  '7' : 7,
                  '8' : 8,
                  '9' : 9,
                  '10' : 10,
                  'Jack' : 10,
                  'Queen' : 10,
                  'King' : 10}
        
        return scores[self.value]

class Deck():
    def __init__(self):
        self.deck = self.fillDeck()
        
    def fillDeck(self):
        deck = []
        
        suit = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
        value = ['Ace','2','3','4','5','6','7',
                 '8','9','10','Jack','Queen','King']    
        
        for i in suit:
            for j in value:
                deck.append(Card(i,j))
        
        shuffle(deck)
        
        return deck

    def printDeck(self):
        for card in self.deck:
            print(card.face())
            
    def dealOne(self):
        return self.deck.pop()
    
class BlackJack():
    def __init__(self):
        self.deck = Deck()
        self.state = 'safe'

    def newGame(self):
        self.deck = Deck()

    def letsJack(self):
        x = self.playerTurn()
        y = self.dealerTurn()
        
        if x >= y:
            print('You win')
        else:
            print('Dealer wins')
        
    def playerTurn(self):

        score = 0
        shadow = score
        answer = 'twist'
        
        while score <= 21 and answer != 'stick':
            
            if score == shadow:
                print('Your score is: ', score)
            if (score != shadow) and shadow <= 21:
                    print('Your score is: ', score,
                          'or ', shadow)   
                
            ans = input('Stick (1) or twist (0): ')
            answer = 'twist' if ans == str(0) else 'stick'
           
            if answer == 'twist':
                card = self.deck.dealOne()
                if type(card.score()) == int:
                    score += card.score()
                    shadow += card.score()

                if type(card.score()) == tuple:
                    score += 1
                    shadow += 11
                
                if score > 21:
                    print('Bust!')
                    self.state = 'bust'
                    return -1
                    
            if answer == 'stick':
                if shadow <= 21:
                    score = shadow
                print('You\'re stuck, your score is: ', score)
                time.sleep(0.5)
                return score
    
    def dealerTurn(self):
        if self.state == 'bust':
            return 1

        print('Dealer\'s turn ...')
        time.sleep(0.5)

        score = 0
        shadow = score
        answer = 'twist'

        while score <= 21 and answer != 'stick':
            
            if score == shadow:
                print('Dealer\'s score is: ', score)
            if (score != shadow) and shadow <= 21:
                    print('Dealer\'s score is: ', score,
                          'or ', shadow)   
                
            time.sleep(0.75)
            if score > 18 or shadow > 18:
                answer = 'stick'
                print('Dealer sticks')
            else: 
                answer = 'twist'
                print('Dealer twists')
           
            if answer == 'twist':
                card = self.deck.dealOne()
                if type(card.score()) == int:
                    score += card.score()
                    shadow += card.score()

                if type(card.score()) == tuple:
                    score += 1
                    shadow += 11
                
                if score > 21:
                    print('Bust!')
                    self.state = 'bust'
                    
            if answer == 'stick':
                if shadow <= 21:
                    score = shadow
                print('Dealer stuck, their score is: ', score)
                return score


game = BlackJack()
game.letsJack()

#print(x.dealOne().score())