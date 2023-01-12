import time
import random
import string

finalList = []


def main():
  mainMenu()


def mainMenu():
  finalList.clear()
  print("Hi, Welcome to Hangman!")
  checkRules = input("Would you like to hear the rules? ")
  if checkRules.lower() == "yes" or checkRules.lower() == "y":
    print(
      "1. Players will choose which hangman game they want to play: Video Games, Films, Musicians."
    )
    time.sleep(1)
    print(
      "Once the set is decided, each player will take turns to guess a letter they believe is in the word"
    )
    time.sleep(1)
    print(
      "If the letter is in the word, it will be added to the answer. The last person to guess the right letter wins."
    )
    time.sleep(1)
  gameType = input(
    "Would you like to play against AI(A), Automated Play(P) or Player vs Player(H)"
  )
  genreType = input(
    "What genre would you like to play? (Video Games(V), Film(F), Musicians(M)"
  )
  gameCheck = ["video games", "v", "vg", "video", "games", "game"]
  filmCheck = ["film", "f"]
  musicCheck = ["music", "m", "musician"]
  wordList = []
  if genreType.lower() in gameCheck:
    wordFile = open("games.txt", "r")
    wordList = wordFile.readlines()

    for i in wordList:
      finalList.append(i.replace("\n", ""))
   # print(finalList)
  elif genreType.lower() in filmCheck:
    wordFile = open("film.txt", "r")
    wordList = wordFile.readlines()

    for i in wordList:
      finalList.append(i.replace("\n", ""))
    # print(finalList)
  elif genreType.lower() in musicCheck:
    wordFile = open("music.txt", "r")
    wordList = wordFile.readlines()

    for i in wordList:
      finalList.append(i.replace("\n", ""))
    # print(finalList)

  if gameType.lower() == "h":
    pvpPlay()
  elif gameType.lower() == "a":
    AiPlay()
  elif gameType.lower() == "p":
    autoPlay()


def pvpPlay():
  P1Turn = True
  selectedWord = random.choice(finalList)
  guessedLetters = []
  guessesLeft = 7
  # print(selectedWord + "\n")
  output = ""
  for i in range(0, len(selectedWord)):
    output += "_"
  print(output)
  while (guessesLeft > 0):
    if (P1Turn):
      guess = input("Player 1, Enter your Guess: ")
    else:
      guess = input("Player 2, Enter your Guess: ")
    guess = guess.strip()
    while (len(guess) == 0 or len(guess) > 1):
      guess = input("Enter your Guess: ")
      guess = guess.strip()
      print("Invalid Input")

    if (guess in guessedLetters):
      guessedLetters.append(guess)
    elif guess in selectedWord:
      P1Turn = not P1Turn
      index = selectedWord.find(guess)
      selectedWord = selectedWord[:index] + "_" + selectedWord[index + 1:]
      output = output[:index] + guess + output[index + 1:]
      print(output + "\n")
      if selectedWord == '_' * len(selectedWord) and P1Turn:
        print("Congrats! Player 2, you win!")
        break
      elif selectedWord == '_' * len(selectedWord) and not P1Turn:
        print("Congrats! Player 1, you win!")
        break
    else:
      P1Turn = not P1Turn
      guessesLeft -= 1
      print("Wrong Guess! " + str(guessesLeft) + " guesses left\n")
  if guessesLeft == 0:
    print("Out of Guesses! You Lose!")
  playAgain = input("Would you like to play again? y/n")
  if (playAgain == 'y'):
    mainMenu()


def AiPlay():
  P1Turn = True
  alphabet = list(string.ascii_lowercase)
  # print(alphabet)
  selectedWord = random.choice(finalList)
  guessedLetters = []
  guessesLeft = 7
  # print(selectedWord + "\n")
  output = ""
  for i in range(0, len(selectedWord)):
    output += "_"
  print(output)
  while (guessesLeft > 0):
    if (P1Turn):
      guess = input("Player 1, Enter your Guess: ")
    else:
      guess = random.choice(alphabet)
      alphabet.remove(guess)
      print("AI guesses " + guess + "\n")
      time.sleep(2)
    guess = guess.strip()
    P1Turn = not P1Turn
    while (len(guess) == 0 or len(guess) > 1):
      guess = input("Enter your Guess: ")
      guess = guess.strip()
      print("Invalid Input")
    if (guess in guessedLetters):
      guessedLetters.append(guess)
    elif guess in selectedWord:
      index = selectedWord.find(guess)
      selectedWord = selectedWord[:index] + "_" + selectedWord[index + 1:]
      output = output[:index] + guess + output[index + 1:]
      print(output + "\n")
      if selectedWord == '_' * len(selectedWord) and P1Turn:
        print("Congrats! Player 2, you win!")
        break
      elif selectedWord == '_' * len(selectedWord) and not P1Turn:
        print("Congrats! Player 1, you win!")
        break
    else:
      guessesLeft -= 1
      print(output + "\n")
      print("Wrong Guess! " + str(guessesLeft) + " guesses left\n")
  if guessesLeft == 0:
    print("Out of Guesses! You Lose!")
  playAgain = input("Would you like to play again? y/n")
  if (playAgain == 'y'):
    mainMenu()


def autoPlay():
  print("AUTOPLAY")
  alphabet = list(string.ascii_lowercase)

  selectedWord = random.choice(finalList)
  guessedLetters = []
  guessesLeft = 7
  print(selectedWord + "\n")
  output = ""
  for i in range(0, len(selectedWord)):
    output += "_"
  print(output)
  while (guessesLeft > 0):

    guess = random.choice(alphabet)
    alphabet.remove(guess)
    print("AI guesses " + guess + "\n")
    time.sleep(2)
    guess = guess.strip()
    while (len(guess) == 0 or len(guess) > 1):
      guess = input("Enter your Guess: ")
      guess = guess.strip()
      print("Invalid Input")
    if (guess in guessedLetters):
      guessedLetters.append(guess)
    elif guess in selectedWord:
      index = selectedWord.find(guess)
      selectedWord = selectedWord[:index] + "_" + selectedWord[index + 1:]
      output = output[:index] + guess + output[index + 1:]
      print(output + "\n")
      if selectedWord == '_' * len(selectedWord):
        print("The AI has solved the word!")
        break
    else:
      guessesLeft -= 1
      print("Wrong Guess! " + str(guessesLeft) + " guesses left\n")
  if guessesLeft == 0:
    print("Out of Guesses! The AI was unable to solve the word")
  playAgain = input("Would you like to play again? y/n")
  if (playAgain == 'y'):
    mainMenu()


main()
