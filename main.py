import time #import for .sleep
import random #import for random list selection
import string #import for getting the alphabet list

finalList = []#Global variable for storing word list to avoid having to pass to functions

def main():
  mainMenu()


def mainMenu():  #Basic main menu loop, displays rules, asks for selections for genre and gametype
  global finalList #Tell python to use the global finalList for this function instead of creating a local one
  print("Hi, Welcome to Hangman!") 
  checkRules = input("Would you like to hear the rules? ") #Display Rules Prompt
  if checkRules.lower() == "yes" or checkRules.lower() == "y": #Check input and display accordingly
    print("1. Players will choose which hangman game they want to play: Video Games, Films, Musicians.")
    time.sleep(1) #Sleep for a second so the console isnt insantly populated with text
    print("Once the set is decided, each player will take turns to guess a letter they believe is in the word")
    time.sleep(1)
    print(
      "If the letter is in the word, it will be added to the answer. The last person to guess the right letter wins."
    )
    time.sleep(1)
  gameType = input(
    "Would you like to play against AI(A), Automated Play(P) or Player vs Player(H)"
  )#Ask for the game mode type
  genreType = input(
    "What genre would you like to play? (Video Games(V), Film(F), Musicians(M)"
  )# Ask for the Genre 
  #Just some hardcoded lists for input/error handling
  gameCheck = ["video games", "v", "vg", "video", "games", "game"]
  filmCheck = ["film", "f", "movie"]
  musicCheck = ["music", "m", "musician"]
  #========This If chain checks if their input is in any of the respective lists and populates the potential wordList accordingly================== 
  if genreType.lower() in gameCheck:
    finalList = [
      "hotline miami", "the walking dead", "hollow knight", "sally face",
      "fran bow", "fortnite", "detroit become human", "the last of us",
      "life is strange", "valorant", "league of legends"
    ]
  elif genreType.lower() in filmCheck:
    finalList = [
      "batman", "bullet train", "coraline",
      "everything everywhere all at once", "the joker", "fight club",
      "american psycho"
    ]
  elif genreType.lower() in musicCheck:
    finalList = [
      "radiohead", "paramore", "placebo", "mcr", "kendrick lamar",
      "have a nice life", "my bloody valentine", "the cure", "elliot smith"
    ]
  #==============END OF IF CHAIN================

  #Then, depending on the value of the gameType, start the proper game function
  if gameType.lower() == "h":
    pvpPlay() #For PVP
  elif gameType.lower() == "a":
    AiPlay()# For vs AI
  elif gameType.lower() == "p":
    autoPlay()#For Automated Play


def pvpPlay(): #Function is for doing hangman automated play
  P1Turn = True #Bool to keep track of whos turn it is
  guessedLetters = [] #List to keep track of letters guessed already
  guessesLeft = 7 # Counter that keeps track of guesses left, shared between players
  output = "" #initialize output 
  word = random.choice(finalList)#pick a random word from the wordList
  for i in range(0, len(word)):#Create the hangman output by replacing all letters with _ and all spaces with ' '
    if word[i] == ' ':
      output += ' '
    else:
      output += "_"
  print(output) #Print the hangman board
  while (guessesLeft > 0): #Loop until they are out of guesses
    if (P1Turn): #If its P1's turn
      while True:#Do-while to handle errors
        guess = input("Player 1, Enter your Guess: ") #Grab user input
        guess = guess.strip()#Strip the spaces
        if (len(guess) != 0 and len(guess) == 1 
            and guess not in guessedLetters):#Ensure that the guess is exactly 1 letter, and has not been guessed already
          break #If it is a valid input, break the do-while
        else:#otherwise print an error message, and loop
          print("Invalid Input (Invalid Length or Already Guessed)")
    else:
      #Same thing but for player 2
      while True:
        guess = input("Player 2, Enter your Guess: ")
        guess = guess.strip()
        if (len(guess) != 0 and len(guess) == 1
            and guess not in guessedLetters):
          break
        else:
          print("Invalid Input (Invalid Length or Already Guessed)")
    guessedLetters.append(guess) #Now we know the input is valid, we can add it to the list of guessed letters
    if guess in word:#Then if the letter is in the word
      P1Turn = not P1Turn #Swap turns
      for i in range(len(word)): #Iterate through every letter in the word
        if word[i] == guess:# If any of the letters in the word match the guess
          output = output[:i] + guess + output[i + 1:] #Add the '_' up to the letter, change that letter to the guess, then place the '_' back on the right hand side
      print(output + "\n") #print the resulting board
      if "_" not in output and P1Turn: #If there are no more '_' in the word, they Win!
        print("Congrats! Player 2, you win!")
        break
      elif "_" not in output and not P1Turn:#Same thing but check if the other player won
        print("Congrats! Player 1, you win!")
        break
    else: #Else their guess wasn't in the word
      P1Turn = not P1Turn # Swap turns
      guessesLeft -= 1 #deduct a guess
      print("Wrong Guess! " + str(guessesLeft) + " guesses left\n") #print a resulting message
  if guessesLeft == 0:#Check if they are out of guesses
    print("Out of Guesses! You Lose!") #If they are, they lose!
  playAgain = input("Would you like to play again? y/n") #Ask them to play again
  if (playAgain == 'y'):#If so, 
    mainMenu()#restart at the main menu


def AiPlay(): #Function for playing vs AI
  P1Turn = True # Set P1 to go first
  alphabet = list(string.ascii_lowercase) #Populate a list all the possible guesses (letters)
  # print(alphabet)
  word = random.choice(finalList)#Choose a random word from the list
  guessedLetters = [] # List for already guessed letters
  guessesLeft = 7 # Keep track of already guessed letters
  print(word + "\n")
  output = "" #Initalize output
  for i in range(0, len(word)): #Populate hangman output according to word selected
    if word[i] == ' ':# spaces become spaces
      output += ' '
    else:# everything else is an '_'
      output += "_"
  print(output) # prints the now hidden word as ______
  while (guessesLeft > 0):#While there are guesses left
    if (P1Turn):
      while True:#Do-while for player input
        guess = input("Player 1, Enter your Guess: ")#grab their input
        guess = guess.strip()#Get rid of the spaces
        if (len(guess) != 0 and len(guess) == 1
            and guess not in guessedLetters):#check that its one letter, and hasn't been guessed already
          break #If its valid, break the loop
        else:
          print("Invalid Input (Invalid Length or Already Guessed)") #otherwise print an error
    else:#Else if its The AI's turn
      guess = random.choice(alphabet)#The ai guesses a random letter from the alphabet
      time.sleep(1)#Sleep to simulate thinking time
      print("AI guesses " + guess + "\n") #Print a message
    P1Turn = not P1Turn #swap turns
    guessedLetters.append(guess) #Add the guessed letter(s) to the list of already guessed letters
    alphabet.remove(guess) # Remove the guessed letter as a possible option for the AI (slight optimization)
    if guess in word:#If the letter is in the word
      for i in range(len(word)):#Search the word to get the index
        if word[i] == guess: # when found
          output = output[:i] + guess + output[i + 1:] #Copy the output, replacing the _ of the guessed letter with the letter
      print(output + "\n") #print it
      if "_" not in output and P1Turn: #check if AI won by checking if there are any '_' left in the output
        print("Congrats! Player 2, you win!") #Print corresponding message
        break #break out of the game loop
      elif "_" not in output and not P1Turn: #Same thing but for player
        print("Congrats! Player 1, you win!")
        break
    else: #Else the guess wasn't in the word
      guessesLeft -= 1 #subtract a guess
      print(output + "\n") #print the gameboard again
      print("Wrong Guess! " + str(guessesLeft) + " guesses left\n")#print a message
  if guessesLeft == 0:# If they are out of guesses
    print("Out of Guesses! You Lose!")#print a message
  playAgain = input("Would you like to play again? y/n") #ask them to play again
  if (playAgain == 'y'):#Check if yes
    mainMenu() #restart at main menu


def autoPlay(): #Function for automated play
  print("==========AUTOPLAY==========")
  guessCount = 0 #Counter for counting how many guesses it took
  alphabet = list(string.ascii_lowercase) # Populate the list of potential guesses
  word = random.choice(finalList) # Select a random word from the list
  print("The word the AI is trying to guess is: " + word + "\n") #Prompt
  output = "" #Initialize output
  for i in range(0, len(word)):#Create the gameboard using the word
    if word[i] == ' ':#If the word has spaces
      output += ' ' #Place a space
    else:
      output += "_" #otherwise, place a '_'
  while True:#Play until its solved
    guess = random.choice(alphabet)#Guess a random letter
    alphabet.remove(guess)#Remove that letter from being guessed again
    print("AI guesses " + guess + "\n")#Print the guess
    guessCount += 1 #increment the counter
    time.sleep(1.5)#Sleep to avoid clutter + simulate thinking
    if guess in word:#Check if the guess is in the word
      for i in range(len(word)):# IF it is
        if word[i] == guess:#Find the index
          output = output[:i] + guess + output[i + 1:]#replace the '_' with the guessed letter
      print(output + "\n")#print the gameboard
      if "_" not in output:#Check if the word has been solved by checking if there are any '_' left
        print("Congrats! The AI has solved the word!\nIt took: " +
              str(guessCount) + " guesses!")#If so, print a congratulations!
        break #break out of the gameloop
    else:#Else 
      print("Wrong Guess!\n")#The guess is wrong
      print(output + "\n\n")#REprint the game board
  playAgain = input("Would you like to play again? y/n: ")#After word is solved, ask if they want to play again
  if (playAgain == 'y'):#If so,
    mainMenu()#restart at main menu


main()
