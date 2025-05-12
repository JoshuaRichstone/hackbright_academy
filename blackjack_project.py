import time
import random

# STEP ONE - Greet and capture player name
"""Asks the Player for name and assigns it to a variable""" 

def ask_player_name():    
    # player_name = input("Hello friend! What is your name?\n > ")
    # player_name = player_name.title()
    
    print(f"Welcome {player_name} to the Intergalactic B21 Tournament!!!\n")
    print(f"My name is {dealer_name}, I am your tournament announcer and dealer\n")



# STEP TWO - Deliver the rules of the game
"""Explains the rules of the game"""

def deliver_rules():
    print("To emerge victorious one must outplay the dealer by getting a score as close as possible to the magic number 21 without exceeding 21!\n")
    print("One can increase their score with 'HIT' or can keep the current score with 'STAY'\n")
    
    # print("Be mindful not to exceed a score of 21 points as that will result in a 'bust' or a LOSS.\n")
    
    # print("In the event the player AND the dealer both reach 21 then the PLAYER is deemed the WINNER, as this is not Vegas Blackjack \n")


# STEP 3 - Delivering card values/scoring
"""Explains the game scoring"""

# def card_scoring():
#     print("Please note the score valuation of the following card types:\n")
#     print("The (A)ce card holds the value of 1\n")
#     print("Cards 2-10 hold the value of their number, the 2 card has the value of 2.\nCards (J)ack, (Q)ueen and (K)ing have the value of 10\n(AA) 'Double Ace' cards hold the value of 11\n")
    



# STEP 4 - ASK TO PLAY & DEAL THE CARDS - 
"""Defines the deal_cards function, prompts player to play or not, deals cards"""

def deal_cards():
    time.sleep(2)
    PC1 = random.randint(1,11)    
    print(f"{player_name}'s Card #1 is: {PC1}\n")

    time.sleep(2)
    DC1 = random.randint(1,11)
    print(f"{dealer_name}'s Card #1 is: {DC1}\n")

    time.sleep(2)
    PC2 = random.randint(1,11)
    print(f"{player_name}'s Card #2 is: {PC2}\n")

    time.sleep(2)
    DC2 = random.randint(1,11)
    print(f"{dealer_name}'s Card #2 is: {DC2}\n")

    time.sleep(2)
    sum_player = (PC1 + PC2)
    # print(type(sum_player))
    print(f"{player_name}'s current score is {sum_player}\n")

    time.sleep(2)
    sum_dealer = (DC1 + DC2)
    # print(type(sum_dealer))
    print(f"{dealer_name}'s current score is {sum_dealer}\n")

    while True: 
        if sum_player < 21:
            choice = input("Would you like to HIT or STAY? > \n")
            choice = choice.upper()
            if choice == "HIT":
                additional_card = random.randint(1,11)
                time.sleep(2)
                print(f"Additional Card is:{additional_card}\n")
                
                sum_player = sum_player + additional_card
                time.sleep(2)
                print(f"{player_name}'s New Score is: {sum_player}\n")

            if sum_player > 21:
                time.sleep(2)
                print(f"Oh Nooo, {player_name} has gone bust and has exceeded the 21 point limit, please try again in our next tournament, friend!\n")
                time.sleep(2)
                play_again = input("Would you like to play again? Yes or No > \n")
                play_again = play_again.upper()
                if play_again == "YES":
                    time.sleep(2)
                    deal_cards()
                elif play_again == "NO":
                    time.sleep(2)
                    print(f"See you in the next Tournament {player_name}!")
                    break
                
                
            elif choice == "STAY":
                player_final_score = sum_player
                time.sleep(2)
                print(f"{player_name}'s Final Score is: {player_final_score}\n")
                while True:
                    if sum_dealer <= 16:
                        additional_card = random.randint(1,11)
                        time.sleep(2)
                        print(f"Additional Card is {additional_card}\n")
                
                        sum_dealer = sum_dealer + additional_card
                
                        time.sleep(2)
                        print(f"{dealer_name}'s New Score is: {sum_dealer}\n")
                    if sum_dealer >= 17:
                        dealer_final_score = sum_dealer
                        time.sleep(2)
                        print(f"{dealer_name}'s Final Score is {dealer_final_score}\n")
                        if dealer_final_score > player_final_score:
                            time.sleep(2)
                            play_again = input(f"{dealer_name} has won the tournament! Would you like to play again? Yes or No > \n ")
                            play_again = play_again.upper()
                            if play_again == "YES":
                                time.sleep(2)
                                deal_cards()
                            elif play_again == "NO":
                                time.sleep(2)
                                print("See you in the next Tournament!")
                        elif player_final_score >= dealer_final_score:
                            time.sleep(2)
                            play_again = input(f"{player_name} has won the tournament! Would you like to play again? Yes or No > \n ")
                            play_again = play_again.upper()
                            if play_again == "YES":
                                time.sleep(2)
                                deal_cards()
                            elif play_again == "NO":
                                time.sleep(2)
                                print(f"See you in the next Tournament{player_name}!")                                        
                        break
                
            elif sum_player == 21:
                time.sleep(2)
                print("You are the WINNER, CONGRATULATIONS!")
                
            
        

    return
    
   
    

def lets_begin():
    time.sleep(2)
    start_game = input("Would you like to play? Yes or No \n > ")
    start_game = start_game.upper()
    if start_game == "YES":
        time.sleep(2)
        deal_cards()
    elif start_game == "NO":
        time.sleep(2)
        print("See you in the next Tournament!")
        #play_again = input("Would you like to play again? Yes or No > ")
    else :
        time.sleep(2)
        print("Invlaid answer, please state Yes or No\n")
        time.sleep(2)
        start_game = input("Would you like to play? YES or NO \n > ")




# STEP 5 - ADD THE VALUATION OF THE CARDS TO GET SUM AND CHECK FOR INDUCING A WIN 


# WHEN A PLAYER HAS AN ACE CARD THEN PROVIDE THE PLAYER THE CHOICE TO USE AN ACE AS A 1 OR 11 WITH EACH NEW CARD ADDED VIA "HIT" UNTIL "STAND" CHOSEN OR "BUST" SCENARIO IS MET.


def play_game():

        
    ask_player_name()
    deliver_rules()
    # card_scoring()
    lets_begin()
    # deal_cards()





player_name = input("Hello friend! What is your name?\n > ")
player_name = player_name.title()
dealer_name = "Mr. Alonsa"
play_game()
