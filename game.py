#Project Name: "Python Hangman Game"
#Author: Jacob Møller & Oliver Thejl Eriksen
#Updated: 25/10 2018

#Import libraries and hangman textfunction.
import random
import hangmanascii
import os

#Global variables.
word = "placeholder" #The word to guess, value will be overwritten.
shownLetters = [] #Array that stores what letters of the word has been shown.
usedLetters = [] #Array that stores the letters already guessed.
bannedLetters = ["",",",".","*"," "] #Array of symbols that dont exist in words.
lives = 10 #Number of lives left. Start at 10, game over when 0.

def StartGame():
    global word
    global shownLetters
    #Opens our wordlist file and defines that we would like to read (r)
    f = open("longlist.txt","r")
    wordList = [] #Makes an empty array
    for line in f: #Splits each line into a value in our array
        #Insert each line as value and strips new line
        wordList.append(line.rstrip())
    #Chooses a random word in the wordlist array
    index = random.randint(0, len(wordList)-1)
    #Selects the word based on the number
    word = wordList[index].upper()
    #Make sure showLetters is contains entries equal to letters in the word.
    #Default is "_" which are substituted as letters are guessed later on.
    shownLetters = ["_"]*len(word)
    #Draw gamescreen and start game algorhytm with GuessLetter()
    Draw()
    GuessLetter()

def GuessLetter():
    #Prompt a single character guess from user.
    letter = input("Gæt et bogstav: ")[0]
    letter = letter.upper() #Make letter uppercase (to match word).
    #If letter is invalid, prompt for a new one. Repeat if neccesary.
    while (letter in usedLetters or letter in bannedLetters):
        Draw()
        letter = input("Gæt et bogstav: ")[0]
        letter = letter.upper()
    #Add letter to array of usedLetters
    usedLetters.append(letter)
    index = [] #List of indexes for where the letter appears.
    lastFound = -1 #Temporary variable for iterating through word.
    #Iterate through word, searching for letter.
    while True:
        #First Loop: Go through entire word, find first instance of letter.
        #Next Loops: Update lastFound to be the index of previous word, and
        #search word from this spot forward for more instances of letter.
        #Do until all instances of letter are found, then lastFound returns -1.
        lastFound = word.find(letter, lastFound + 1)
        #If a letter was found (when lastfound is not -1), note index.
        if(lastFound != -1):
            index.append(lastFound)
        #When all letters (or none) have been found, break out of loop.
        else:
            break
    #If the letter couldnt be found in word, lose a life.
    if (len(index) == 0):
        LoseLife()
    #Else reveal the letters by calling RevealLetters function with index(es).
    else:
        RevealLetters(letter, index)

def LoseLife():
    global lives
    lives -= 1 #Subtract one from lives.
    #If no lives are left, call gameover loss.
    if(lives == 0):
        GameOver(True)
    #Else continue guessing.
    else:
        Draw()
        GuessLetter()

def GameOver(lost):
    #lost is a boolean that determines if the player lost or won.
    global word
    #If lost is true, print loss screen and reveal word.
    if (lost):
        Draw()
        print("Game over, du tabte!")
        print("Ordet var: " + word)
    #Else print congratulations.
    else:
        print("Tillykke, du vandt!")

def RevealLetters(letter, index):
    #letter is the letter that has been guessed.
    #index is where in the word that letter exists.
    global shownLetters
    #Iterate through shownLetters array, revealing the guessed ones.
    for i in range(len(index)):
        shownLetters[index[i]] = letter
    Draw()
    #If there are no blank spaces left in showLetters, you won.
    if("_" not in shownLetters):
        GameOver(False)
    #Else continue playing by guessing a new word.
    else:
        GuessLetter()

def Draw():
    #The Draw function clears screen and prints gamestate based on glabal variables.
    os.system("cls") #Clears screen
    print("Ord:", end=" ")
    #Print all showLetters, this includes "_" for letters not guessed yet.
    for i in range(len(word)):
        print(shownLetters[i], end=" ")
    print("")
    print("")
    #Print number of lives
    print("Liv tilbage: ", lives)
    print("")
    #Calling hangman drawing
    hangmanascii.hangman(11 - lives)
    print("")
    print("Brugte bogstaver:", end=" ")
    #Print all usedLetters
    for i in range(len(usedLetters)):
        print(usedLetters[i], end=" ")
    print("")
    print("")

#Initialize game
StartGame()

#Dont exit before user presses enter
print("")
input("Enter to exit")
