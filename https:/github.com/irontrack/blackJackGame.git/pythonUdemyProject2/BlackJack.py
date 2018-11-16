import random

class Card():
    def __init__(self,card):
        self.card = card
        self.value = 0
        if card[0] == 'A':
            self.value == 11
        elif card[0] == 'K' or card[0] =='Q' or card[0] == 'J':
            self.value == 10
        elif card[0] == '1':
            self.value = 10
        else:
            self.value = int(card[0])
    def card_value(self):
        return self.value
    def face(self):
        return self.card
    def __str__(self):
        
        return self.card
    
class Deck():
    
    def __init__(self):    
        suits = ['D','C','H','S']
        self.cards = {}
        
        index = 1
        for s in suits:
            for n in range(1,14):
                if n == 1:
                    temp = 'A' + s
                elif n == 11:
                    temp = 'J'+ s
                elif n == 12:
                    temp = 'Q' + s
                elif n == 13:
                    temp = 'K' + s
                else:
                    temp = str(n) + s
                self.cards[str(index)] = temp
                index += 1
        self.order = list(range(1,53))
        random.shuffle(self.order)
    def d_card(self):
        return self.cards[str(self.order.pop())]
    def show(self):
        for x in range(0,52):
            print(self.cards[str(self.order[x])])
     

class Player():
    # every player has a hand, a bank
    def __init__(self):
        self.hand = []
        self.bank = 0
        pass
    def draw_card(self,card):
        t_card = Card(card)
        self.hand.append(t_card)
    def get_bank(self):
        return self.bank
    def mod_bank(self,value):
        self.bank = self.bank + value
    
class Game():
    def __init__(self):
        # here create a player, a dealer, a deck, and a pot
        self.player1 = Player()
        self.dealer = Player()
        self.deck = Deck()
        self.pot = 0
        self.keep_playing = True
        self.dealerHide = True
        pass
    def deal(self):
        self.player1.draw_card(self.deck.d_card())
        self.dealer.draw_card(self.deck.d_card())
        self.player1.draw_card(self.deck.d_card())
        self.dealer.draw_card(self.deck.d_card())
    def bust(self,hand):
        # would like a recursive function that finds the minimum sum
        # and return True only if all sums are greater than 21
        
        try:
            temp = hand[:]
            temp.remove(11)
            temp.append(1)
            return sum(hand) > 21 and self.bust(temp)
        except:
            return sum(hand) > 21
        
    def blackJack(self,hand):
        # recursive returns true in any version of hand sums to 21
        try:
            temp = hand[:]
            temp.remove(11)
            temp.append(1)
            return sum(hand) == 21 or self.blackJack(temp)
        except:
            return sum(hand) == 21
    def round(self):
        
        while True:
            try:
                bet = int(input('Place initial wager: '))
            except:
                self.print_screen()
                print('sorry, must be integer amount:')
            if bet > self.player1.get_bank():
                self.print_screen()
                print('sorry, insufficient bank: ')
            else:
                break
        self.pot += bet
        self.player1.mod_bank(-bet)
        self.deal()
        while True:
            decision = input('would you like to hit or stay: y/n? ')
            if decision == 'y':
                self.player1.draw_card()
            values = []  
            for cards in self.player1.hand:
                values.append(cards.value())
            
        
            if self.bust(values):
                break
                pass
            elif self.blackJack(values):
                break
                pass
        
    
    def play(self):
        while True:
            try:
                initialBank = int(input('How much would you like to deposite? :'))
            except:
                print('sorry, must input an integer amount')
            else:
                break
        self.player1.mod_bank(initialBank)
        playAgain = True
        self.print_screen()
        self.round()
        self.print_screen()
        #while playAgain:
            
    def print_screen(self):
        bank = self.player1.get_bank()
        pot = self.pot
        print('\n'*100)
        print('='*30)
        print(f"Pot = {pot} player bank = {bank}")
        print('\n')
        temp = 'Dealer''s hand: '
        for x in range(0,len(self.dealer.hand)):
            if x == 0 and self.dealerHide == True:
                temp += '## '
            else:
                temp += self.dealer.hand[x].face() + ' '
        print(temp)
        temp = 'Player''s hand: '
        for x in self.player1.hand:
            temp += x.face() + ' '
        print(temp)
        print('='*30)
        
        
if __name__ == '__main__':
    game = Game()
    print(game.bust([11,10,5,8]))
  

    
