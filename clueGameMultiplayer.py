import random
from termcolor import colored, cprint
import os
os.system("color")

murderRoom = ''
murderWeapon = ''
murderer = ''


player1 = ''
player2 = ''
player3 = ''
player1Deck = []
player2Deck = []
player3Deck = []


rooms = ['deck', 'bilge', 'berth', 'captain quarters', 'rec room', 'ballroom' ]
suspects = ['blackbeard', 'spanish jackie', 'izzy', 'calico jack', 'nigel', 'zheng yi']
weapons = ['sword', 'knife', 'canonball', 'paperweight', ]
players = ['jim', 'frenchie', 'lucius', 'stede', 'oluwande']
cards = []

#creates strings of the lists and assigns them red color
def arrayToString():
    #strings of the arrays 
    global colorRooms
    global colorWeapons
    global colorSuspects
    colorRooms = ''
    colorWeapons = ''
    colorSuspects = ''
    
    
    #rooms
    nCounter = 1
    roomLen = len(rooms)
    for room in rooms:
        colorRooms = colorRooms + room
        if nCounter < roomLen:
            colorRooms = colorRooms + ', '

    nCounter = nCounter + 1
    #weapons
    nCounter = 1
    weaponLen = len(weapons)
    for weapon in weapons:
        colorWeapons = colorWeapons + weapon
        if nCounter < weaponLen:
            colorWeapons = colorWeapons + ', '
        
    #suspects
    nCounter = nCounter + 1
    nCounter = 1
    suspectLen = len(suspects)
    for suspect in suspects:
        colorSuspects = colorSuspects + suspect
        if nCounter < suspectLen:
            colorSuspects = colorSuspects + ', '

    nCounter = nCounter + 1
    
    colorRooms = colored(colorRooms, "red")
    colorWeapons = colored(colorWeapons, "red")
    colorSuspects = colored(colorSuspects, "red")
    
#combine all lists into one called cards
def setup_cards():
    global cards

    # extract all items from the lists and place into cards so we can shuffle
    # first do the suspects
    for suspect in suspects:
        cards.append(suspect)

    # next do the rooms
    for room in rooms:
        cards.append(room)

    # and last do the suspects
    for weapon in weapons:
        cards.append(weapon)
    
#shuffles cards
def shuffle():   
    random.shuffle(cards)
    
#Chooses correct answers
def answers():
    global murderRoom
    global murderWeapon
    global murderer
    murderRoom = random.choice(rooms)
    murderWeapon = random.choice(weapons)
    murderer = random.choice(suspects)
    
    #remove the cards that have been chosen as the winning answers
    cards.remove(murderRoom)
    cards.remove(murderWeapon)
    cards.remove(murderer)
  
#rules + choose victim
def explain():
    global victim
    victim = random.choice(players)
    players.remove(victim)
    #setting up for color
    intro = 'Welcome to clue! \n \
    Our flag means death version'
    death = 'Oh No! ' + victim + ' was murdered on the revenge'
    rules = 'The goal is to correctly narrow down and guess the location of the murder, what weapon was used, and the murderer themselves \n \
    You will be prompted to enter a room and make a suggestion, if one of your guesses is correct, you will be told so, just not which one ;) \n \
    we recomend taking notes to keep track \n \
    Once you have narrowed it down, you can make a guess, if its correct you win, if not, you lose'
    
    cprint(intro, "light_cyan")
    cprint(death, "light_red")
    print(rules)
            
#sorts cards into decks and removes from cards   
def dealDeck():
    global player1Deck
    global player2Deck
    global player3Deck
    
    counter = 1
    
    for card in cards:
        if (counter == 1):
            player1Deck.append(card)
        if (counter == 2):
            player2Deck.append(card)
        if (counter == 3):
            player3Deck.append(card )
            
        counter = counter + 1
        if(counter == 4):
            counter =1   
    
#pick character names and shows your deck and assigns color for players
def pickPlayer():
    global player1
    global player2
    global player3
    
    print('')
    cprint(players, "green")
    player1 = input('Pick a character to play ')
    
        #enter code to check correct input
        
        
    print('')
    #setting up for color
    global Player1
    Player1 = colored(player1, "light_green")
    print('You are playing as ' + Player1)
    
    #choose player2 + player3 and remove them
    players.remove(player1)
    player2 = random.choice(players)
    players.remove(player2)
    player3 = random.choice(players)
    players.remove(player3)
    
    #setting up for color
    global Player2
    global Player3
    Player2 = colored(player2, "light_green")
    Player3 = colored(player3, "light_green")
    
    
    print('')
    cprint('Youll be playing against ' + Player2 + ' and ' + Player3)
    print('')
    print('Your cards are ')
    cprint(player1Deck, "light_yellow")

#goes through each players turn, make suggestion, and search decks   
def playerGuessAndCheck():
    print()
 
    #randomize choices and search others decks for match
    playerRoom = ''
    playerWeapon = ''
    playerSuspect = ''
    #setting up for color

    
    turn = 1
    
    #user/player1 turn
    if turn == 1:
        print(colorRooms)
        playerRoom = input('Pick a location to investigate ')
        print('')
        print('You are now in ' + playerRoom)
        print(' ')
        print(colorSuspects)
        playerSuspect = input('Who would you like to suggest?')
        print('')
        print(colorWeapons)
        playerWeapon = input('What weapon would you like to suggest?')
        print('')
        #setting up for color
        #playerRoom = colored(playerRoom, "light_red")
        #playerWeapon = colored(playerWeapon, "light_red")
        #playerSuspect = colored(playerSuspect, "light_red")

        
        
        if playerRoom in player2Deck:
            playerRoom = colored(playerRoom, "light_red")
            print(Player2 + ' has the ' + playerRoom + ' card')
        if playerRoom in player3Deck:
            playerRoom = colored(playerRoom, "light_red")
            print(Player3 + ' has the ' + playerRoom + ' card')
                  
        if playerSuspect in player2Deck:
            playerSuspect = colored(playerSuspect, "light_red")
            print( Player2 + ' has the ' + playerSuspect + ' card')
        if playerSuspect in player3Deck:
            playerSuspect = colored(playerSuspect, "light_red")
            print(Player3 + ' has the ' + playerSuspect + ' card') 
            
        if playerWeapon in player2Deck:
            playerWeapon = colored(playerWeapon, "light_red")
            print(Player2 + ' has the ' + playerWeapon + ' card')
        if playerWeapon in player3Deck:
            playerWeapon = colored(playerWeapon, "light_red")
            print(Player3 + ' has the ' + playerWeapon + ' card')
            
        turn = turn + 1 
        input()
         
    #player2 turn    
    if turn == 2:
        playerRoom = random.choice(rooms)
        playerWeapon = random.choice(weapons)
        playerSuspect = random.choice(suspects)
        #setting up for color
        playerRoomC = colored(playerRoom, "light_red")
        playerWeaponC = colored(playerWeapon, "light_red")
        playerSuspectC = colored(playerSuspect, "light_red")
        
        print(Player2 + ' has suggested ' + playerSuspectC + ' killed ' + victim + ' in the ' + playerRoomC + ' with a ' + playerWeaponC)
        
     
        if playerRoom in player1Deck:     
            playerRoom = colored(playerRoom, "light_red")
            print('You show ' + Player2 + ' your ' + playerRoom + ' card')             
        if playerRoom in player3Deck:
            playerRoom = colored(playerRoom, "light_red")
            print(Player3 + ' shows ' + Player2 + ' a card')
                  
        if playerSuspect in player1Deck:      
            playerSuspect = colored(playerSuspect, "light_red")
            print('You show ' + Player2 + ' your ' + playerSuspect + ' card')
        if playerSuspect in player3Deck:
            playerSuspect = colored(playerSuspect, "light_red")
            print(Player3 + ' shows ' + Player2 + ' a card')
          
        if playerWeapon in player1Deck:
            playerWeapon = colored(playerWeapon, "light_red")
            print('You show ' + Player2 + ' your ' + playerWeapon + ' card')           
        if playerWeapon in player3Deck:
            playerWeapon = colored(playerWeapon, "light_red")
            print(Player3 + ' shows ' + Player2 + ' a card')
            
        turn = turn + 1   
        input() 
         
    #player3 turn   
    if turn == 3:
        playerRoom = random.choice(rooms)
        playerWeapon = random.choice(weapons)
        playerSuspect = random.choice(suspects)
        #setting up for color
        playerRoomC = colored(playerRoom, "light_red")
        playerWeaponC = colored(playerWeapon, "light_red")
        playerSuspectC = colored(playerSuspect, "light_red")
        
        
        print(Player3 + ' has suggested ' + playerSuspectC + ' killed ' + victim + ' in the ' + playerRoomC + ' with a ' + playerWeaponC)
        
        if playerRoom in player1Deck:
            playerRoom = colored(playerRoom, "light_red")
            print('You show ' + Player3 + ' your ' + playerRoom + ' card')     
        if playerRoom in player2Deck:
            playerRoom = colored(playerRoom, "light_red")
            print(Player2 + ' shows ' + Player3 + ' a card')
                  
        if playerSuspect in player1Deck:            
            playerSuspect = colored(playerSuspect, "light_red")
            print('You show ' + Player3 + ' your ' + playerSuspect + ' card')
        if playerSuspect in player2Deck:
            playerSuspect = colored(playerSuspect, "light_red")
            print(Player2 + ' shows ' + Player3 + ' a card')
          
        if playerWeapon in player1Deck:
            playerWeapon = colored(playerWeapon, "light_red")
            print('You show ' + Player3 + ' your ' + playerWeapon + ' card')
        if playerWeapon in player2Deck:
            playerWeapon = colored(playerWeapon, "light_red")
            print(Player2 + ' shows ' + Player3 + ' a card')
            
        turn = turn + 1 
        input() 
          
        
    if turn == 4:
        turn = 1
   
#final guess
def makeFinalGuess(m_room, m_weapon, m_suspect):
    print('Time to make your final guess')
    g_room = input('What room was the murder in')
    print('')
    g_suspect = input('Whos the killer?')
    print('')
    g_weapon = input('What was the weapon used?')
    print('')
    if(g_room == m_room and g_suspect == m_suspect and g_weapon == m_weapon):
        print('Congrats you win!')
    else:
        print('Sorry that is incorrect. \n' 'The correct answers were: ' + g_room + ', ' + g_suspect + ',and ' + g_suspect \
              + ' \n Game Over :(')
        

def toLower(input):
    lowered = input.lower()
    return lowered

upper = 'UPPER'
print(upper)
toLower(upper)

#arrayToString()
#setup_cards()
#shuffle()
#answers()
#explain()
#dealDeck()
#pickPlayer()


proceed = input('Ready to start?')

playerGuessAndCheck()
repeat = input('Would you like to make another suggestion? y/n')
while(repeat == 'y'):
    playerGuessAndCheck()
    repeat = input('Would you like to make another suggestion? y/n')
        
makeFinalGuess(murderRoom, murderWeapon, murderer)
        

