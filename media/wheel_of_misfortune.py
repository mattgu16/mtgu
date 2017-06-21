
#Tejas Guha, Matthew Gu, Dan Xu

#--Game Name--#
#Wheel of Misfortune#

#--Program--#
#Python#



print("Note: This game is best played in full screen.")
print(" ")
print("Type wheel_of_misfortune to start.")


#-----------------------Wheel Core Randomizer---------------------#

def wheelcore():
        from random import randint
        points=[50,"Bankrupt",50,"Bankrupt",60,60,65,65,70,"Bankrupt",70,80,80,90,"Bankrupt",90,250,"Bankrupt","Bankrupt","Bankrupt"]
        x=randint(0,19)
        print(points[x])
        
#--------------------Wheel Spinner--------------------#

#This function is dependent on the wheelcore and core funtions. It will not work called by itself.

def wheel():
        from random import randint
        import time
        x=randint(0,19) #Picks a rondom integer from 0 to 20
        points=[50,"Bankrupt",50,"Bankrupt",60,60,65,65,70,"Bankrupt",70,80,80,90,"Bankrupt",90,250,"Bankrupt","Bankrupt",350]
        print(' ')
        print("Spinning...")
        time.sleep(1)
        print("══════════════════════════════")
        wheelcore() #Gives a sense of "spinnning a wheel"
        time.sleep(0.01)
        wheelcore()
        time.sleep(0.01)
        wheelcore()
        time.sleep(0.01)
        wheelcore()
        time.sleep(0.01)
        wheelcore()
        time.sleep(0.01)
        wheelcore()
        time.sleep(0.025)
        wheelcore()
        time.sleep(0.025)
        wheelcore()
        time.sleep(0.025)
        wheelcore()
        time.sleep(0.025)
        wheelcore()
        time.sleep(0.025)
        wheelcore()
        time.sleep(0.025)
        wheelcore()
        time.sleep(0.025)
        wheelcore()
        time.sleep(0.05)
        wheelcore()
        time.sleep(0.05)
        wheelcore()
        time.sleep(0.05)
        wheelcore()
        time.sleep(0.05)
        wheelcore()
        time.sleep(0.05)
        wheelcore()
        time.sleep(0.05)
        wheelcore()
        time.sleep(0.05)
        wheelcore()
        time.sleep(0.05)
        wheelcore()
        time.sleep(0.05)
        wheelcore()
        time.sleep(0.05)
        wheelcore()
        time.sleep(0.05)
        wheelcore()
        time.sleep(0.05)
        wheelcore()
        time.sleep(0.1)
        wheelcore()
        time.sleep(0.1)
        wheelcore()
        time.sleep(0.1)
        wheelcore()
        time.sleep(0.1)
        wheelcore()
        time.sleep(0.1)
        wheelcore()
        time.sleep(0.1)
        wheelcore()
        time.sleep(0.1)
        wheelcore()
        time.sleep(0.1)
        wheelcore()
        time.sleep(0.1)
        wheelcore()
        time.sleep(0.25)
        wheelcore()
        time.sleep(0.25)
        wheelcore()
        time.sleep(0.25)
        wheelcore()
        time.sleep(0.25)
        wheelcore()
        time.sleep(0.5)
        wheelcore()
        time.sleep(0.5)
        wheelcore()
        time.sleep(0.75)
        wheelcore()
        time.sleep(0.75)
        print("══════════════════════════════")
        time.sleep(1)
        print("Multiplier: "+str(points[x])) #Points received by player is value when points is indexed by x
        letter=""
        print('')
        print(puzzle)
        print(hint)
        print('')
        if points[x]=="Bankrupt":
                print("You are bankrupt!")
                return letter, "bankrupt"
        else:
                while letter not in validletters:   #Will keep asking user for letter unless he/she gives in a proper format
                        letter=input("Choose a letter: ").lower()
                return letter, points[x]
                
                
                        
#-----------------------Board Creator---------------------#

def puzzleboard(phrase): #creates puzzleboard of phrase
        p = ''
        for e in phrase:  #iterates through every character in string to make it an underscore and space
                if e == ' ':
                        p = p + '  '
                else:
                        p = p+ '_' + ' '
        return p
#inputs one extra space at the end

#-----------------------Board Display------------------------#

#Requires puzzleboard

def display_letters(phrase,puzzle,letter): #displays user-given letter on puzzleboard
        fuzzy = puzzle
        instance = phrase.find(letter) #finds first instance of letter
        while instance != -1:
                fuzzy = fuzzy[0:instance*2]+letter+fuzzy[(instance*2)+1:] #concatenates to string where place of instance becomes letter on puzzleboard
                instance = phrase.find(letter,instance+1)
        return fuzzy
        
        
#-----------------------Core Program---------------------#
        
def wheel_of_misfortune(): #actual game
        import random
        import time
        print("══════════════════════════════════════════════════")
        print("Note: This is best played in full screen.")
        print('══════════════════════════════════════════════════')
        time.sleep(2)
        print("Welcome to WHEEL OF MISFORTUNE!")
        print("══════════════════════════════════════════════════")
        time.sleep(2)
        directionsprompt="maybe"
        peopleplaying="9001"
        players=["2","3","4"]
        cities=["salt lake city","providence","concord","minneapolis","oklahoma city","portland","annapolis","atlanta","boston","juneau","sacramento","carson city","little rock","chicago","tampa","seattle","houston","omaha","charleston"]
        name_brands=["nike","starbucks","apple","google","facebook","mcdonalds","amazon","microsoft","intel","wikipedia","united airlines","mercedes benz","new york times","spotify","ferrari","frito lay","national geographic","rolex"]
        actions=["taking a shower","eating breakfast","stuck in traffic","baking gingerbread cookies","updating my status","working out","surfing the internet","charging my phone","eating dinner","watching tv"]
        song_lyrics=["why you got to be so rude","shut up and dance with me","shake it off","call me maybe", "you look like my next mistake", "let it go", "remember me for centuries","the wheels on the bus go round and round","i cant feel my face when im with you","hey hey hey hey living like were renegades","dont believe me just watch"]
        science = ["osmosis","photosynthesis","gravity","law of conservation of energy","chromosomes","sunspots","solar wind","deoxyribonucleic acid","ecosystem","isotopes","thermodynamics","string theory","quantum mechanics","general relativity"]
        hints = ["American Cities","Name Brand","Everyday Action","Song Lyrics","Science Terms"]
        global validletters
        validletters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","guess"]
        validdirectionanswers=["yes","no"]
        while directionsprompt not in validdirectionanswers:
        	directionsprompt=input("Would you like an overview of the directions? Type yes if this is your first time playing, otherwise no.  ")
        	if directionsprompt in validdirectionanswers:
        		if directionsprompt=="yes":
        			directions()
        			break
        		else:
        			break
        while peopleplaying not in players:
            print('══════════════════════════════════════════════════')
            peopleplaying=str(input("How many people are playing? (2-4 Players): ")) #keeps asking user how many players are playing until valid input is given
        print("══════════════════════════════════════════════════")
        print("Let's Start!")
        time.sleep(1)
        total_points = {"Player 1":0,"Player 2":0,"Player 3":0,"Player 4":0} #creates dictionary of total points
        i = 1
        players = ["1"]+players[0:players.index(peopleplaying)+1] #creates list of what players are playing
        while i <= 6: #iterates for 6 rounds
                print('══════════════════════════════════════════════════')
                print("»»Round"+" "+str(i)+"««")
                time.sleep(1.5)
                categories = [cities,name_brands,actions,song_lyrics,science] 
                category = random.choice(categories) #picks a random category
                global hint
                hint = hints[categories.index(category)] #gives the category name
                phrase = random.choice(category) #picks random phrase in category
                global puzzle
                puzzle = puzzleboard(phrase)
                blank_with_phrase = ''
                for k in list(phrase):
                        blank_with_phrase = blank_with_phrase + k + ' ' #makes copy of finsihed version of puzzlebaord (with all letters guessed)
                e = 1
                j = 0 
                while puzzle != blank_with_phrase:
                        while j != 1: #iterates forever
                                for e in players:
                                        print('══════════════════════════════════════════════════')
                                        print("►Player"+ ' '+e)
                                        print("══════════════════════════════════════════════════")
                                        time.sleep(1)
                                        print("Loading...")
                                        time.sleep(1)
                                        print(' ')
                                        time.sleep(2)
                                        time.sleep(2)
                                        letter, points = wheel()
                                        if letter == "guess": #if user wants to guess
                                                guess = input("Your guess: ")
                                                if guess == phrase: #if guess is right
                                                        points = 500
                                                        print('You got it right!')
                                                        print('')
                                                        total_points["Player"+ ' '+e] = total_points["Player"+ ' '+e]+points #500 points added to player
                                                        print("Your Score:",total_points["Player"+ ' '+e])
                                                        time.sleep(2)
                                                        j = 1 #makes infinte loop stop
                                                        puzzle = blank_with_phrase #automatically sets puzzlebaord to blank_with_phrase
                                                        break #breaks out of for loop
                                        if points == "bankrupt":
                                        	total_points["Player"+ ' '+e] = 0 #if bankrupt player gets 0 points
                                        if letter in phrase and len(letter) > 0:
                                        	puzzle = display_letters(phrase,puzzle,letter) #if letter in phrase, displays on board
                                        	total_points["Player"+ ' '+e] = total_points["Player"+ ' '+e]+multiplier(phrase,letter,points)
                                        print("Your Score:",total_points["Player"+ ' '+e])
                                        time.sleep(1)
                                        if puzzle == blank_with_phrase:
                                                j = 1 #if puzzleboard is guessed infinite loop stopped
                                                break #for loop stopped
                                        print('')
                                        time.sleep(1.5)
                i = i + 1 #moves on to next round
        print('')
        print('Total Scores')
        for i in players:
                print('')
                print("Player" + " " + i+" "+'has'+" "+str(total_points["Player"+ ' '+i])+" "+'points.')
                
                
                
                        
#----------------------------Score Multiplier------------------------------#

# Multiplies points from wheel() and the number of times letter occurs in phrase
def multiplier(phrase, letter, points):
        histograms(phrase)
        y=dict()
        for z in phrase:
                if z not in y:
                        y[z]=1
                else:
                        y[z]=y[z]+1
        keys=y.keys()
        keys=list(keys)
        keys.sort()
        for e in keys:
                if e==letter:
                        netpoints=y[e]*points
                        a=y[e]
                        return netpoints
        
        
#--------------------------Histogram Things----------------------#

def histograms(x): #finds occurence of each letter in phrase
        y=dict()
        for z in x:
                if z not in y:
                        y[z]=1
                else:
                        y[z]=y[z]+1
        return y
        printhist(y)
                        
#--------------------------Histogram Part 2---------------------------------------#
def printhist(x):
        keys=x.keys()
        keys=list(keys)
        keys.sort()
        for e in keys:
                if e==letter:
                        return(x[e])
                        
#-----------------------------Directions----------------------------------#
def directions():
	import time
	print('══════════════════════════════════════════════════')
	print("This game is a spin-off of ABC's popular game show, Wheel of Fortune.")
	print('')
	time.sleep(3)
	print("The 'wheel' has been rigged to include many more misfortunes (a.k.a losing all your points), and the game has been altered a bit to balance these features.")
	print('')
	time.sleep(5)
	print("Please read the following rules regardless of previous knowledge of the original game.")
	print('')
	time.sleep(3)
	print("In a moment, the game will begin. At the start, you will be prompted to input the amount of players playing. This game is meant for 2 to 4 players.")
	print('')
	time.sleep(7)
	print("After you answer, the game will display the round number (there are 3 rounds), and which player's turn it is.")
	print('')
	time.sleep(5)
	print("The player up should take control over the keyboard.")
	print('')
	time.sleep(3)
	print("The most updated puzzleboard will be loaded, and the game will then proceed to spin 'the wheel'.")
	print('')
	time.sleep(5)
	print("When you see the dotted lines, (-----), the next element will be your point multiplier (or bankrupt).")
	print('')
	time.sleep(5)
	print("This multiplier will determine your score for that turn based on how many of the letter you guessed are actually in the puzzle.")
	print('')
	time.sleep(6)
	print("After guessing your letter, your turn ends, and the game displays the total score of the player that just went.")
	print('')
	time.sleep(5)
	print("If you would like to guess the puzzle, type 'guess' (without the quotes) when prompted to choose a letter.")
	print('')
	time.sleep(5)
	print("All puzzles in WHEEL OF MISFORTUNE are lower case, without punctutation (only letters and spaces)")
	print('')
	time.sleep(5)
	print("The game will now begin in..")
	time.sleep(3)
	print("3..")
	time.sleep(1)
	print("2..")
	time.sleep(1)
	print("1..")
	time.sleep(2)
	
	
	
	
	
