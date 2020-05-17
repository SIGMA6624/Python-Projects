# classes here
class Card:
    '''
    Each Card object only needs two attributes: suit and rank
    '''
    
    def __init__(self,rank,suit):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
class Deck:
    '''
    Deck object that will hold all card objects in the deck
    '''
    
    def __init__(self):
        # start with an empty list for the deck, then instantiate each card as a Card object to the deck
        print()
        print('Putting all the cards in the deck...')
        
        self.deck = []  
        for suit in suits:
            # go through all the suits in the global suits tuple
            for rank in ranks:
                # go through all the ranks in the global ranks tuple
                self.deck.append(Card(rank,suit))
    
    
    def __str__(self):
        # not necessary, but just for testing what's inside your deck. Use this to see if __init__ or shuffle() works
        
        printdeck = ''
        for item in self.deck:
            printdeck += str(item) + '\n'
        return printdeck

    def shuffle(self):
        # shuffle the deck
        print('Shuffling the deck...')
        random.shuffle(self.deck)
        
    def deal(self,playerhand,dealerhand):
        '''
        Players get 2 cards from the deck, and these cards are visible in the whole game. 
        In this simplified game, there's only one player.
        The Dealer will also draw 2 cards, but only one is visible. The other card is face down. 
        
        We will be taking 2 hand objects here. One for the player; one for the dealer
        '''
        
        # draw 2 cards from deck (remove these cards from deck) and add to player hand
        for loop in range(0,2):
            #playerhand.cards.append(self.deck.pop())
            playerhand.add_card(self.deck.pop())
        
        # debug for playerhand
        '''
        print('Player Hand:')
        for card in playerhand.cards:
            print(card)
        '''
        
        for loop in range(0,2):
            #dealerhand.cards.append(self.deck.pop())
            dealerhand.add_card(self.deck.pop())
            
        # debug for dealerhand
        '''
        print('Dealer Hand:')
        for card in dealerhand.cards:
            print(card)
        '''

class Hand:
    def __init__(self):
        # runs when a new game starts and when initializing a player
        
        self.cards = []  # start with an empty list as we did in the Deck class; Card objects go here
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        # add a Card object here, might add values here, too?
        
        if card.rank != 'Ace':
            # if the card you add isn't an Ace
            # add the card to your hand
            self.cards.append(card)
            
            # add the values of the cards in your hand (double check pls)
            for key in values.keys():
                # go through values.keys() and compare it with the card's rank

                if key == card.rank:
                    # add the equivalent of the card value in self.values
                    self.value += values[card.rank]
            
        else:
            # when the card drawn is an ace
            
            self.aces += 1           # add self.aces counter
            self.cards.append(card)  # add the card to your hand
            self.adjust_for_ace(self.aces)    # function to adjust the value of Ace
    
    def adjust_for_ace(self, acecard):
        
        # function adjusts the value of Ace 
        
        # this dictionary just removes 'Ace'
        adjvalues = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10}
        tempvalue = 0              # this placeholder variable checks if setting your aces as 11 will make self.value exceed 21 
        
        
        
        # a loop that will recount the value of your hand without aces
        for card in self.cards:
            for key,value in adjvalues.items():
                if card.rank == key:
                    tempvalue += value   # Note: no aces yet
            
        # a loop based on the number of aces so far
        for count in range(1, self.aces+1):
            
            if tempvalue + values['Ace'] > 21:
                # if your hand w/o Aces + an Ace (11) > 21, change Ace to 1 and add it to your value 
                tempvalue += 1
            else:
                # else just treat Ace as an 11
                tempvalue += values['Ace']
                
        self.value = tempvalue    # changes self.value to ace adjusted value 

class Chips:
    # the number of chips a player has when playing a game
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        print(f'The player will start with {self.total} chips')
        self.bet = 0
        
    def win_bet(self):
        print(f"You win the bet! Here's {self.bet}.")
        self.total += self.bet
    
    def lose_bet(self):
        print(f"You lost the bet! I'll be taking {self.bet} now.")
        self.total -= self.bet
        
        
        

# normal functions here
def take_bet(chips):
    # function for taking a bet, returns the amount you will bet
    settingbet = True
    
    while settingbet:
        try:
            bet = int(input('How much would you bet for this game? '))
        except ValueError:
            #if input to bet isn't a number
            print("That's not a valid input. Try again.")
            
            # reset the loop right away if this happens
            continue
        
        # once there is no error in the input
        if bet <= chips.total:
            # successfully set a bet and exit the loop
            print(f'You have set your bet successfully. You bet {bet} chips.')
            settingbet = False
        else:
            # bet too much and a message will tell you. Repeat the loop again.
            print("You can't bet more than you have. Try again.")
    
    # this should be passed to the bet attribute of Chips()
    return bet

def show_some(player,dealer):
    '''
    Player turn scenario
    
    dealer will only show one card and leave the other hidden.
    player will show both cards dealt and the ones he will be hitting.
    They are Hand objects
    '''
    
    # show player cards and value
    print()
    print('These are the player cards:')
    for card in player.cards:
        print(card)
    print(f'Value: {player.value}')
    print()
    
    # show dealer cards (1 visible, 1 hidden)
    print()
    print('These are the dealer cards:')
    print(dealer.cards[0])
    print('Hidden\n')
    print()
    
def show_all(player,dealer):
    '''
    Dealer turn scenario (AKA player's done hitting) 
    
    player will show all cards in his hand
    dealer will show all the cards 
    '''
    
    # show player cards and value
    print()
    print('These are the player cards:')
    for card in player.cards:
        print(card)
    print(f'Value: {player.value}')
    print()
    
    # show dealer cards and value
    print()
    print('These are the dealer cards:')
    for card in dealer.cards:
        print(card)
    print(f'Value: {dealer.value}')
    print()
    
def hit(deck,hand):
    ''' 
    Get a Deck and Hand object for the hit function.
    Need to use both here
    
    'Hit' means drawing a card from the deck and adding it to your hand. Meaning return the card "drawn".
    
    Players have the option to keep hitting, until they've gone bust. 
    The dealer will be programmed to keep hitting while their hand is less than 17.
    
    .pop() usually removes an item with an index of -1 (last item of the list).
    The moment you call this, the last deck item will be removed (even if you are just checking for its suit or rank).
    Therefore, you should have a variable to store this Card object the moment you call this.
    
    '''
    # hand.cards.append(deck.deck.pop())
    hand.add_card(deck.deck.pop())
    
def hit_or_stand(deck,hand):
    '''
    hit = draw a card
    stand = don't draw a card. Dealer will be drawing now
    
    This will be at the player's turn. It ends when he chooses 'stand'.
    '''
    
    global playing  # to control an upcoming while loop
    
    while True:
        choice = input('Hit or stand? Choose: ')

        if choice.lower() == 'hit':
            print('You chose hit.')
            
            # hit function
            hit(deck,hand)
            
            break
        elif choice.lower() == 'stand':
            print('You chose stand.')
            
            # stand function. Move to dealer drawing
            playing = False
            print("It's now the dealer's turn.\n\n")
            
            break
        else:
            print('Invalid choice. Try again.')
    
def player_busts(chips):
    print("You've gone bust.")
    chips.lose_bet()

def player_wins(chips):
    print("Your hand value beats the dealer's.")
    chips.win_bet()
    
def player_instantwin(chips):
    print("Your hand value is exactly 21!")
    chips.win_bet()

def dealer_busts(chips):
    print("The dealer's gone bust.")
    chips.win_bet()
    
def dealer_wins(chips):
    print("The dealer's hand value beats yours.")
    chips.lose_bet()
    
def replay():
    while True:
        answer = input("Want to play again? Type 'yes' if you do. Type 'no' if you don't: ")
        if answer.lower() == 'yes':
            return True
            break
        elif answer.lower() == 'no':
            return False
            break
        else:
            print('Not a valid answer!')
    
    
# import functions and modules here
import random
import time




# global variables here
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

init = True   # boolean for setting up the game objects





# print opening statement here
print("""
Welcome to Charles's Python Blackjack game!\n
We will be playing only a simplified version of the game.
The rules are:\n
1. The player and the dealer will draw 2 cards, each, from the deck.\n
2. The player's hand will be visible for the whole game. The dealer's hand will only show one card, and the other will be hidden.\n
3. We start with the player. The goal is to have a hand reach the closest to 21. If the player gets 21, he wins the bet automatically.\n
4. If the hand isn't 21, he can 'hit' and get a card. He can do this again and again until he feels like it. However, if his hand exceeds 21, he 'busts' and loses the bet.\n
5. If the player feels like his hand is enough, he can 'stand' and stop drawing, ending his turn. This will lead to the dealer's turn.
6. The dealer will reveal his hidden card and will also start 'hitting' until he feels like it. \n
7. The dealer has a chance to 'bust', too, by having his hand exceed 21.\n
8. Once the dealer feels like he can't 'hit' anymore than his risk tolerance, he will 'stand', ending his turn.\n
9. If neither busts, the hand closest to 21 wins.\n
""")


        
# default starting chips at 100
chips = Chips()
    
    
# Main game here
while True:
    
    if init:
        # Create & shuffle the deck
        main_deck = Deck()
        main_deck.shuffle()
        
        # instantiate the player and the dealer
        playerhand = Hand()
        dealerhand = Hand()
        
        # deal two cards to each Hand
        main_deck.deal(playerhand,dealerhand)
        
        # Prompt the Player for their bet
        chips.bet = take_bet(chips)
    
        # Show cards (but keep one dealer card hidden)
        # show_some(playerhand,dealerhand)
        
        # we're done setting up the game
        init = False
        
        # it's time to play the game
        playing = True

    playerbusted = False
    while playing:  # recall this variable from our hit_or_stand function
        
        # before asking hit or stand, check if the hand is exactly 21
        if playerhand.value == 21:
            # if exactly 21, instantly win
            player_instantwin(chips)
            playerbusted = True
            break
        
        # clear screen
        # print('\n'*100)
        
        
        # Show cards (but keep one dealer card hidden)
        show_some(playerhand,dealerhand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if playerhand.value > 21:
            player_busts(chips)
            playerbusted = True
            break
            
        # Prompt for Player to Hit or Stand
        hit_or_stand(main_deck,playerhand)
        
    
    # Show all cards
    show_all(playerhand,dealerhand)
    
    # If Player hasn't busted, play Dealer's hand until Dealer's value reaches 17
    dealerbusted = False
    while dealerhand.value < 17 and not playerbusted:
    
        # dealer hits until 17 or bust
        hit(main_deck,dealerhand)
        
        
        # Show all cards
        show_all(playerhand,dealerhand)
        
        # Run different winning scenarios
        if dealerhand.value > 21:
            dealer_busts(chips)
            dealerbusted = True
            
        time.sleep(5)
    
    # No one busts so far
    if not playerbusted and not dealerbusted:       
        # Run different winning scenarios
        if playerhand.value > dealerhand.value:
            player_wins(chips)
        elif playerhand.value < dealerhand.value:
            dealer_wins(chips)
        elif playerhand.value == dealerhand.value:
            print("It's a tie. No one's winning or losing chips.")
    
    # Inform Player of their chips total 
    print(f"You now have {chips.total} chips.")
    
    # end of game, ask to replay or not
    if replay():
        init = True
        print('Restarting the game...')
    else:
        print('Thank you for playing!')
        break