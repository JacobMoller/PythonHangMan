#Project Name: "Python Hangman Game"
#Author: Jacob Møller & Oliver Thejl Eriksen
#Updated: 2/10 2018

import random
import hangmanascii
import os

#Global variables.
word = "placeholder" #The word to guess, value will be overwritten.
shownLetters = []
usedLetters = []
lives = 6 #Number of lives left

def StartGame():
    #TODO: Import wordlist
    dkWordList = ["sporvogn", "SKOLE"]
    for i in range(len(dkWordList)):
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
    letter = input("Guess a letter: ")
    letter = letter.upper() #Make letter uppercase
    index = [] #List of indexes for where the letter appears
    lastFound = -1
    while True:
        lastFound = word.find(letter, lastFound + 1)
        if(lastFound != -1):
            index.append(lastFound)
        else:
            break
    if (len(index) == 0):
        LoseLife()
    else:
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
        print("Game over, you lost!")
    else:
        print("Congratulations, you won!")

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
    for i in range(len(word)):
        print(shownLetters[i], end=" ")
    print("")
    print("Liv tilbage: ", lives)
    print("")
    #Calling hangman drawing
    hangmanascii.hangman(lives)

def Clear():
    os.system("cls")

#Initialize game
StartGame()

#Dont exit before user presses enter
input("Enter to exit")