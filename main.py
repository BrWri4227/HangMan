import time
import random
import string

finalList = []


def main():
  mainMenu()


def mainMenu():
  global finalList
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
  filmCheck = ["film", "f", "movie"]
  musicCheck = ["music", "m", "musician"]
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

  if gameType.lower() == "h":
    pvpPlay()
  elif gameType.lower() == "a":
    AiPlay()
  elif gameType.lower() == "p":
    autoPlay()


# def pvpPlay():
#   P1Turn = True
#   selectedWord = random.choice(finalList)
#   guessedLetters = []
#   guessesLeft = 7
#   # print(selectedWord + "\n")
#   output = ""
#   for i in range(0, len(selectedWord)):
#     output += "_"
#   print(output)
#   while (guessesLeft > 0):
#     if (P1Turn):
#       guess = input("Player 1, Enter your Guess: ")
#     else:
#       guess = input("Player 2, Enter your Guess: ")
#     guess = guess.strip()
#     while (len(guess) == 0 or len(guess) > 1):
#       guess = input("Enter your Guess: ")
#       guess = guess.strip()
#       print("Invalid Input")

#     if (guess in guessedLetters):
#       guessedLetters.append(guess)
#     elif guess in selectedWord:
#       P1Turn = not P1Turn
#       index = selectedWord.find(guess)
#       selectedWord = selectedWord[:index] + "_" + selectedWord[index + 1:]
#       output = output[:index] + guess + output[index + 1:]
#       print(output + "\n")
#       if selectedWord == '_' * len(selectedWord) and P1Turn:
#         print("Congrats! Player 2, you win!")
#         break
#       elif selectedWord == '_' * len(selectedWord) and not P1Turn:
#         print("Congrats! Player 1, you win!")
#         break
#     else:
#       P1Turn = not P1Turn
#       guessesLeft -= 1
#       print("Wrong Guess! " + str(guessesLeft) + " guesses left\n")
#   if guessesLeft == 0:
#     print("Out of Guesses! You Lose!")
#   playAgain = input("Would you like to play again? y/n")
#   if (playAgain == 'y'):
#     mainMenu()

# def pvpPlay():
#   P1Turn = True
#   selectedWord = random.choice(finalList)
#   guessedLetters = []
#   guessesLeft = 7
#   # print(selectedWord + "\n")
#   output = ""
#   for i in range(0, len(selectedWord)):
#     if selectedWord[i] == ' ':
#       output += ' '
#     else:
#       output += "_"
#   print(output)
#   while (guessesLeft > 0):
#     if (P1Turn):
#       guess = input("Player 1, Enter your Guess: ")
#     else:
#       guess = input("Player 2, Enter your Guess: ")
#     guess = guess.strip()
#     while (len(guess) != 1 and guess != ' '):
#       print("Invalid Input")
#       guess = input("Enter your Guess: ")
#       guess = guess.strip()

#     if (guess in guessedLetters):
#       guessedLetters.append(guess)
#     elif guess in selectedWord:
#       P1Turn = not P1Turn
#       index = selectedWord.find(guess)
#       selectedWord = selectedWord[:index] + "_" + selectedWord[index + 1:]
#       output = output[:index] + guess + output[index + 1:]
#       print(output + "\n")
#       print(selectedWord)
#       if '_' not in output and P1Turn:
#         print("Congrats! Player 2, you win!")
#         break
#       elif '_' not in output and not P1Turn:
#         print("Congrats! Player 1, you win!")
#         break
#     elif guess == ' ' and ' ' in selectedWord:
#       P1Turn = not P1Turn
#       index = selectedWord.find(guess)
#       selectedWord = selectedWord[:index] + "_" + selectedWord[index + 1:]
#       output = output[:index] + ' ' + output[index + 1:]
#       print(output + "\n")
#     else:
#       P1Turn = not P1Turn
#       guessesLeft -= 1
#       print("Wrong Guess! " + str(guessesLeft) + " guesses left\n")
#   if guessesLeft == 0:
#     print("Out of Guesses! You Lose!")
#   playAgain = input("Would you like to play again? y/n")
#   if (playAgain == 'y'):
#     mainMenu()


def pvpPlay():
  P1Turn = True
  guessedLetters = []
  guessesLeft = 7
  output = ""
  word = random.choice(finalList)
  for i in range(0, len(word)):
    if word[i] == ' ':
      output += ' '
    else:
      output += "_"
  print(output)
  while (guessesLeft > 0):
    if (P1Turn):
      while True:
        guess = input("Player 1, Enter your Guess: ")
        guess = guess.strip()
        if (len(guess) != 0 and len(guess) == 1
            and guess not in guessedLetters):
          break
        else:
          print("Invalid Input (Invalid Length or Already Guessed)")
      # guess = input("Player 1, Enter your Guess: ")
    else:
      while True:
        guess = input("Player 2, Enter your Guess: ")
        guess = guess.strip()
        if (len(guess) != 0 and len(guess) == 1
            and guess not in guessedLetters):
          break
        else:
          print("Invalid Input (Invalid Length or Already Guessed)")
    guess = guess.strip()
    guessedLetters.append(guess)
    if guess in word:
      P1Turn = not P1Turn
      for i in range(len(word)):
        if word[i] == guess:
          output = output[:i] + guess + output[i + 1:]
      print(output + "\n")
      if "_" not in output and P1Turn:
        print("Congrats! Player 2, you win!")
        break
      elif "_" not in output and not P1Turn:
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
  word = random.choice(finalList)
  guessedLetters = []
  guessesLeft = 7
  # print(selectedWord + "\n")
  output = ""
  for i in range(0, len(word)):
    if word[i] == ' ':
      output += ' '
    else:
      output += "_"
  print(output)
  while (guessesLeft > 0):
    if (P1Turn):
      while True:
        guess = input("Player 1, Enter your Guess: ")
        guess = guess.strip()
        if (len(guess) != 0 and len(guess) == 1
            and guess not in guessedLetters):
          break
        else:
          print("Invalid Input (Invalid Length or Already Guessed)")
    else:
      guess = random.choice(alphabet)
      print("AI guesses " + guess + "\n")
      time.sleep(1)
    guess = guess.strip()
    P1Turn = not P1Turn
    guessedLetters.append(guess)
    alphabet.remove(guess)
    if guess in word:
      for i in range(len(word)):
        if word[i] == guess:
          output = output[:i] + guess + output[i + 1:]
      print(output + "\n")
      if "_" not in output and P1Turn:
        print("Congrats! Player 2, you win!")
        break
      elif "_" not in output and not P1Turn:
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
  print("==========AUTOPLAY==========")
  guessCount = 0
  alphabet = list(string.ascii_lowercase)
  word = random.choice(finalList)
  guessesLeft = 1
  print("The word the AI is trying to guess is: " + word + "\n")
  output = ""
  for i in range(0, len(word)):
    if word[i] == ' ':
      output += ' '
    else:
      output += "_"
  print(output)
  while (guessesLeft > 0):
    guess = random.choice(alphabet)
    alphabet.remove(guess)
    print("AI guesses " + guess + "\n")
    guessCount += 1
    time.sleep(1.5)
    guess = guess.strip()
    if guess in word:
      for i in range(len(word)):
        if word[i] == guess:
          output = output[:i] + guess + output[i + 1:]
      print(output + "\n")
      if "_" not in output:
        print("Congrats! The AI has solved the word!\n It took: " +
              str(guessCount) + "guesses!")
        break
    else:
      print("Wrong Guess!\n")
      print(output + "\n\n")
  playAgain = input("Would you like to play again? y/n")
  if (playAgain == 'y'):
    mainMenu()


main()
