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
bannedLetters = ["",",",".","*"]
lives = 6 #Number of lives left.


def StartGame():
    #Import word-list
    f = open("words.txt","r") #Opens our list file and defines that we would like to read (r)
    dkWordList = [] #Makes an empty array
    for line in f: #Splits each line into a value in our array
        dkWordList.append(line.rstrip()) #Insert each line as value and strips new line
    #Chooses a random word in the wordlist array
    index = random.randint(0, len(dkWordList)-1)
    #Selects the text based on the number
    global word
    global shownLetters
    
    word = dkWordList[index].upper()
    shownLetters = ["_"]*len(word)
    #Draw gamescreen and start game algorhytm with GuessLetter()
    Draw()
    GuessLetter()

def GuessLetter():
    letter = input("Gæt et bogstav: ")[0] #Prompt a guess from user.
    letter = letter.upper() #Make letter uppercase (to match word).
    while (letter in usedLetters or letter in bannedLetters):
        #If letter has already been used, prompt for a new one.
        Draw()
        letter = input("Gæt et bogstav: ")[0]
        letter = letter.upper()

    usedLetters.append(letter)
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
    global word
    if (lost):
        Draw()
        print("Game over, du tabte!")
        print("Ordet var: " + word)
    else:
        print("Tillykke, du vandt!")

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
    print("Brugte bogstaver:", end=" ")
    for i in range(len(usedLetters)):
        print(usedLetters[i], end=" ")
    print("")
    print("")

def Clear():
    os.system("cls")

#Initialize game
StartGame()

#Dont exit before user presses enter
print("")
input("Enter to exit")
