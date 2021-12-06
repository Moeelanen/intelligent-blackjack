import random

# dealer always the last one 
#player that we play with is always the first one


#function to rotate the 4th roller: when they press the initial button and when they press to stay

#function: vector for everyone hands and a the end of the round sum all the cards from everyone hand and count cards


#TO DO : Ask for users input to say the card that get out of the deck instead of do random like they do here

# just need a variable to recevi the valeu of the picture of the card for example 3 ou Q . THen go throw a list and see the valeu of echa valeu of the picture

#function: 1st player clikes saying im the first then the machine rotates till the last player then devide the degrees per amout of players 

def rotate_machine(player,degrees,players):
    position_of_machine=0
    # "player" is going to be the next player that the machine rotates to
    if player == players:
        # we what to return to the player 0 , the initial pasition of the machine
        # rotate the machine to position 0
        return position_of_machine
    position_of_machine += player*degrees 
    #rotates the machine "position_of_machine" degrees
    # 2*60=120 --> the position of the machine is going to be 120 degres from his original position
    return position_of_machine

def hand_total(hand): 
    """
    Calculates sum total values from a list of strings using a dictionary
    """
    d_val = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
             '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11, 'A.': 1}
    return sum(d_val[i] for i in hand)

def confirm_card(card_0):
    """
    List of all possibel cards
    """
    d_val = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
             '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11, 'A.': 1}
    if card_0 in d_val:
        return True
    else:
        return False

def check_ace(hand):
    """
    Checks if there's an ace in the hand
    """
    if 'A' in hand:
        return True
    else:
        return False

def check_(hand_before,card_0): 
    """
    There is one or more Aces on the players hand before taking the card_0
    """

    total_before=hand_total(hand_before)
    
    print(total_before)

    if total_before >= 19 and total_before <=21:
        """
         this is about probabilities
         i wouldnt take the risk of converting the A to 1 
         and end up with less the 20 on the next round
         we could use the true_count valeu and decide based on if theres more low or high cards but i think at the end of the day would be the same!
         It's about probabilities and not exact valeus! Besides the cases with the Aces will be more rare
        """
        return False

    #muda um dos A para o valor 1
    print(hand_before)
    hand_before[hand_before.index('A')]='A.'
    print(hand_before)

    
    new_total=hand_total(hand_before)
    print (new_total)

    hand_after=hand_before[:]
    hand_after.append(card_0)
    print(hand_after)

    if new_total<21:
        total_after=hand_total(hand_after)
        print (total_after)
        if total_after==21:
            return True
        elif total_after > 21:
            #check if there is more aces on the hand before
            check=check_ace(hand_before)
            if check:
                #there is more aces lets convert them 
                return check_(hand_before,card_0)
            else:
                return False
        elif total_after < 21:
            """
             again this is the same situation as before! 
             we are telling him to take the card because we are converting the aces's to valeu 1 
             and then accepting the new card doesnt go over 21 so its okay to accept the new card
             its always better to continue playing 
             again we can use the true_counter and do probabilities with that but i guess that doesnt increase more the ods of winning because we cant see the future cards
             however i decided that if the valeu of the cards before takeing the new card is 19 or 20 we dont take the risk and we dont convert A to 1 and we decide to hit
             otherwise if the total of the and before is less them 19 we converte the valeu of the A to 1 and we decide to stay
            """
            return True
    elif new_total > 21:
        #situation where more then one A was converted one the last play
        return check_(hand_before,card_0)
 
def provisory_list(players_list, card_0):
    p_list=players_list[:]
    p_list.append(card_0)
    total_before=hand_total(players_list)
    total_after= hand_total(p_list)

    #first check if the player has natural BlackJack after reciving the 2 first cards
    if total_before == 21:
        print("You have natural BlackJack!")
        return False
    if total_after <= 21:
        return True
    elif total_after > 21:
        if card_0 == 'A':
            return True
        else:
            aces=check_ace(players_list)
            if not aces:
                return False
            elif aces:
                return check_(players_list[:],card_0)

def add_card_list(players_list,card_valeu):
    """
    Add a card to the players list
    """
    players_list.append(card_valeu)
    return players_list

def player_print(hand, total): 
    """
    Prints player's current hand and total
    """
    print("\nYour hand: ", hand, "\nYour total: ", total)

def initial_game():
    """
    asks if they ant to play blackjack
    """
    while True: 
        # Asking the player to play again or not
        play = input("Do you want to play a new game of BlackJack? \n").lower()
        if play == 'yes' or play == 'y':
            print("\n------------ Blackjack -------------\n")
            return True
        elif play == 'no' or play == 'n':
            return False
        else:
            print("Yes or no? ")
            continue

def play_again():
    """
    Loops the game
    """
    while True: 
        # Asking the player to play again or not
        ans = input("Do you want to play another round of Blackjack? \n").lower()
        if ans == 'yes' or ans == 'y':
            return True
        elif ans == 'no' or ans == 'n':
            return False
        else:
            print("Yes or no? ")
            continue
            
def counting_cards(hand):
    """
    Count cards using strategy 'Hi-Lo'
    """
    vals = {'2': 1, '3': 1, '4': 1, '5': 1, '6': 1, 
            '7': 0, '8': 0, '9': 0, '10': -1, 'J': -1, 
            'Q': -1, 'K': -1, 'A': -1, 'A.': -1}

    return sum(vals[i] for i in hand)

def true_counter(deck, r_count):
    """
    Calculates and returns the true count rounded down
    """
    try:
        return round(r_count/(deck//52))
    except:
        # Compensating for when there is less than 52 cards or 1 deck left
        return r_count


def print_count(true_cnt, r_count):
    """
    Prints out current counts
    """
    print('\nRunning Count: --->', r_count, '\nTrue Count: ', true_cnt)
    
def blackjack(players, deck_num, degrees_between):

    """
    Playing Blackjack
    """
    card_0 = ''
    n_of_cards=0
    players_list=[[] for _ in range(players)]

    #gives the first two cards from this round
    while n_of_cards < 2 :
        for i in range(players):
            print(players_list)

            #machine throws the card
            while True:
                #camera reads also the cards
                card_0=input("What is the card that got out for player nr " + str(i) + ": ")
                if confirm_card(card_0):
                    break
                else:
                    print("Not a valid card. Please repeat! ")
                    continue

            
            players_list[i]=add_card_list(players_list[i],card_0)
            deck_num-=1
            #make the machine rotating to the next player
            machine_rotation = rotate_machine(i+1,degrees_between,players)
        n_of_cards +=1
    #now every player has 2 cards in their hand

    #prints players hands to see if it works
    for i in range(players):
        print("Players", i, "hand: ", players_list[i])
        
    n_players=0
    while n_players < players:   
        while deck_num >= 1:
            #read the information from the camera module in this case we put the input
            #ask camera for the valeu
            while True:
                #camera reads also the cards
                card_0 = input ("What is the card that the camera detected?  " )
                if confirm_card(card_0):
                    break
                else:
                    print("Not a valid card. Please repeat! ")
                    continue
            
            if n_players==0: # player that plays with the machine
                check=provisory_list(players_list[n_players], card_0)
                if check == True:
                    #tell user to take the card with the devise
                    print("Take the card!")
                else:
                    #tell user not to take the card with the devise
                    print("Dont take the card!")
            
            print(players_list[n_players])

            if n_players == players-1: 
                print("Dealer turn! ")
        
            # Alow the players to make a move
            move = input("Hit or stay? ").lower() #returns the lower case string
            #then this needs to be changed with the buttons input
            
            #at this moment the user had already received the information 
            #on his portable device so he can decide accordinally
            if move == "hit" or move == "h":
                """
                    machine throws the card to the player 
                """
                players_list[n_players]=add_card_list(players_list[n_players],card_0)
                deck_num-=1
                print(players_list[n_players])
                print(deck_num)  # ----------------------------------------------------
                continue
                
            elif move == "stay" or move == "s":
                #rotates the machine for the next player
                machine_rotation=rotate_machine(n_players+1,degrees_between,players)
                break
            else:
                # Continuing the loop if input was different from 'hit' or 'stay'
                print('Please type hit or stay')
                continue
        n_players +=1

    return[players_list,deck_num]
    
def play_blackjack():
    
    ply=initial_game()
    if not ply:
        print("You dont want to play blackjack so i will exit the game!")
        return False

    """
        basic feutures
    """
    players=int(input("How many players? "))
    deck= int(input("How many deck? "))
    """
        machine turns around and devides the degres per n of players
    """
    degree=int(input("How many degree did the sensor calculated? "))
    degrees_between=degree/players # 180/3 = 60
    #machine turns back again for the position 0 ? 
    # Or just stays there and consider the last position the player n0

    star=input("Press some key to start. ") # or whatever you want to implement this parte Miikka

    """
        machine starts giving cards to the players -----> in this case its going to be the user giving the valeus
    """
    total_cards=52*deck
    r_count = 0
    true_cnt = 0
    play = True
    machine_rotation=0.0
    
    while play :
        
        #final = [players_list, total_cards]
        final=blackjack(players, total_cards, degrees_between)

        total_cards=final[1]
        # Determining if there are enough cards left
        if final[1]//players*2 < 1:
            print("Not enough cards left. ")
            return False
        play = play_again()

        #if play is true we are going to play another round so its time to make the bets
        if play:
            """
                Couting cards for the bets for the next round
                Since we have a camera we only need to count cards to decide our bets, 
                we dont need to count cards to decide 'hit' or 'stay', the machine decides that for us
            """
            for i in final[0]:
                r_count+=counting_cards(i) 
            true_cnt=true_counter(r_count,final[1])
            print_count(true_cnt,r_count)

            """
            How do you want to do now ? do something like: 
            if true_count<0 that means that are more low card on the deck then high card so bet low
            if true_count>0 the means that are more high cards left on the deck then low so bet higher
            ??? 
            I dont know how the bets work?? 
            You can decide what you want to do. Or if you want i can make some research about it and decide

            if true_count==0 --> bet normal
            if true_counter>0 --->lots of high cards on the deck
            if true_count<0 ---> lots of low cards on the deckno
            """
            if true_cnt==0 :
                print("Bet normal")
            elif true_cnt>0:
                print("True count is grather than 0 ---> More high cards left on the deck. Bet higher!")
            else:
                print("True count is less than 0 ---> More low cards left on the deck. Bet lower!")

            print("\n------------ Another Round of Blackjack -------------")

    return play


# starts the game    
game=True
while game:
    game=play_blackjack()

exit

