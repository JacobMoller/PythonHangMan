#Project Name: "Python Hangman Game" 
#Author: Jacob Møller & Oliver Thejl Eriksen
#Updated: 2/10 2018

import random
import hangmanascii

#Wordlist to choose from
dkWordList = ["Sporvogn", "Skole", "hej"]
#Chooses a random word in the wordlist array
dkWordNumberChosen = random.randint(0, len(dkWordList)-1)
#Selects the text based on the number
dkWord = dkWordList[dkWordNumberChosen]

#Prints underscores the number of letters
print("Word to guess:")
for i in range(len(dkWord)):
    print("_", end=" ")

print("")
print("")
wrongLetters = []
#Calling hangman animation after 7 errors (wrong letters)
hangmanascii.hangman(6)



#Prints the word that the user should guess TEMPORARY
#print(dkWord)
