#Project Name: "Python Hangman Game"
#Author: Jacob Møller & Oliver Thejl Eriksen
#Updated: 2/10 2018

#Import libraries and hangman text.
import random
import hangmanascii
import os

#Global variables.
word = "placeholder" #The word to guess, value will be overwritten.
shownLetters = [] #Array that stores what letters of the word has been shown.
usedLetters = [] #Array that stores the letters already guessed.
lives = 6 #Number of lives left.

def StartGame():
    #TODO: Import wordlist
    dkWordList = ["sporvogn", "skole"]
    for i in range(len(dkWordList)):
        #Change all letters to uppercase
        dkWordList[i] = dkWordList[i].upper()
    #Chooses a random word in the wordlist array
    index = random.randint(0, len(dkWordList)-1)
    #Selects the text based on the number
    global word
    global shownLetters
    word = dkWordList[index]
    shownLetters = ["_"]*len(word)
    #Prints underscores the number of letters
    Draw()
    GuessLetter()

def GuessLetter():
    letter = input("Gæt et bogstav: ")
    letter = letter.upper() #Make letter uppercase (to match word)
    index = [] #List of indexes for where the letter appears
    lastFound = -1
    while True:
        #Iterate through word, searching for letter.
        lastFound = word.find(letter, lastFound + 1)
        if(lastFound != -1):
            index.append(lastFound)
        else:
            break
    if (len(index) == 0):
        #If the letter couldnt be found in word, lose a life.
        LoseLife()
    else:
        #Reveal
        RevealLetters(letter, index)

def LoseLife():
    global lives
    lives -= 1
    if(lives == 0):
        GameOver(True)
    else:
        Draw()
        GuessLetter()

def GameOver(lost):
    if (lost):
        Draw()
        print("Game over, du tabte!")
    else:
        print("Tillyke, du vandt!")

def RevealLetters(letter, index):
    global shownLetters
    for i in range(len(index)):
        shownLetters[index[i]] = letter
    Draw()
    if("_" not in shownLetters):
        GameOver(False)
    else:
        GuessLetter()

def Draw():
    Clear()
    print("Ord:", end=" ")
    for i in range(len(word)):
        print(shownLetters[i], end=" ")
    print("")
    print("")
    print("Liv tilbage: ", lives)
    print("")
    #Calling hangman drawing
    hangmanascii.hangman(7 - lives)
    print("")

def Clear():
    os.system("cls")

#Initialize game
StartGame()

#Dont exit before user presses enter
input("Enter to exit")