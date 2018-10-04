#Project Name: "Python Hangman Game"
#Author: Jacob Møller & Oliver Thejl Eriksen
#Updated: 2/10 2018

import random
import hangmanascii

#Global variables.
word = "placeholder" #The word to guess, value will be overwritten.
lives = 6 #Number of lives left

def GameOver(Lost):
    if (Lost):
        Print("Game over, you lost!")
    else:
        Print("Congratulations, you won!")

def LoseLife():
    lives -= 1
    if(lives == 0):
        GameOver(True)

def RevealLetters():
    print("hey")

def GuessLetter(letter):
    letter = letter.upper() #Make letter uppercase
    index = [] #List of indexes for where the letter appears
    lastFound = -1
    while True:
        lastFound = word.find(letter, lastFound + 1)
        if(lastFound != -1):
            index.append(lastFound)
        else:
            break
    print(index)
    if (len(index) == 0):
        LoseLife();
    else:
        RevealLetters(letter, index)

def StartGame():
    #Import wordlist
    dkWordList = ["sporvogn", "SKOLE", "HEJ"]
    for i in range(len(dkWordList)):
        dkWordList[i] = dkWordList[i].upper()
    #Chooses a random word in the wordlist array
    index = random.randint(0, len(dkWordList)-1)
    #Selects the text based on the number
    word = dkWordList[index]

    #Prints underscores the number of letters
    print("Word to guess:")
    for i in range(len(word)):
        print("_", end=" ")
    print("")
    print("")
    wrongLetters = []
    #Calling hangman animation after 7 errors (wrong letters)
    hangmanascii.hangman(6)
    GuessLetter(input("Guess a letter"))

StartGame()



input("Enter to exit") #Dont exit before user presses enter
#Prints the word that the user should guess TEMPORARY
#print(dkWord)
