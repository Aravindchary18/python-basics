import random
#card class 
class card:
    def __init__(self,suits,ranks):
        self.suits=suits
        self.rank=ranks["rank"]
        self.value=ranks["Value"]
    def __str__(self):
        return f"{self.rank} of {self.suits}"
#deck class , this class holds all cards ,that is this remembers the cards through the end because of self which strengthens the variable lasts to the end.
class deck:
    def __init__(self):
        self.cards=[]
        suits=["spades","clubs","hearts","diamonds"]
        ranks=[{"rank":"A","Value":11},
              {"rank":"2","Value":2},
              {"rank":"3","Value":3},
              {"rank":"4","Value":4},
              {"rank":"5","Value":5},
              {"rank":"6","Value":6},
              {"rank":"7","Value":7},
              {"rank":"8","Value":8},
              {"rank":"9","Value":9},
              {"rank":"10","Value":10},
              {"rank":"J","Value":10},              
              {"rank":"Q","Value":10},
              {"rank":"K","Value":10}]
        #create all 52 cards
        for suit in suits:
            for rank in ranks:
                self.cards.append(card(suit,rank))
    def shuffle(self):
           random.shuffle(self.cards)
    def deal(self,number=1):
        cards_dealt=[]
        for _ in range(number):
            if self.cards:#only if deck is not empty
                  cards_dealt.append(self.cards.pop())
        return cards_dealt 
    #hand class          
class hand:
        def __init__(self,dealer=False):
            self.cards=[]
            self.value=0
            self.dealer=dealer
        def add_card(self,cards):
            self.cards.extend(cards)
        def calculate_value(self):
            self.value=0
            aces=0
            for card in self.cards:
                self.value+=card.value
                if card.rank=='A':
                    aces+=1
            while self.value>21 and aces:
                        self.value-=10
                        aces-=1
        def get_value(self):
            self.calculate_value()
            return self.value
        def is_blackjack(self):
            return self.get_value()==21
        def display(self,show_all_dealer_card=False):
            owner = "dealers" if self.dealer else "yours"
            print(f"{owner}hand:")   
    
            for index,card in enumerate(self.cards):
                #hides dealer's first card
                if index==0 and self.dealer and not show_all_dealer_card and not self.is_blackjack():
                    print("hidden")
                else :
                    print(card)
            if not self.dealer:
                print("value:",self.get_value())
            if self.dealer and show_all_dealer_card:
                print("value=",self.get_value())
                  
#game class

class game():
    def __init__(self):
        self.deck=deck()
        self.deck.shuffle()
    def check_winner(self,playerhand,dealerhand):
        if playerhand.get_value()>21:
            print("you are busted.dealer wins")
            return True
        elif dealerhand.get_value()>21:
            print("dealer busted. you win")
            return True
        elif playerhand.is_blackjack() and dealerhand.is_blackjack():
            print("both got blackjack. draw")
            return True
        elif dealerhand.is_blackjack():
            dealerhand.display(show_all_dealer_card=True)
            print("dealer got blackjack hee wins")
            return True      
        elif playerhand.is_blackjack():
            print("player got blackjack. you win")
            return True
        elif playerhand.get_value()>dealerhand.get_value():
            print("player won")
            return True
        elif dealerhand.get_value()>playerhand.get_value():
            print("dealer wins")
            return True
        else:
            print("its a draw")
            return True
    def play(self):
        playerhand=hand()
        dealerhand=hand(dealer=True)
        #draw initial 2 cards
        playerhand.add_card(self.deck.deal(2))
        dealerhand.add_card(self.deck.deal(2))
        #display initial cards
        playerhand.display()
        dealerhand.display()
       
    
        #dealer draws until 17
        while dealerhand.get_value()<17:
            dealerhand.add_card(self.deck.deal(1))
            #display final cards
        print("\nfinal hands:")
        dealerhand.display(show_all_dealer_card=True)
      #  checkwinner at the end
        self.check_winner(playerhand,dealerhand)
        #run game
if __name__=="__main__":
    game=game()
    game.play()