#Project Name: "Python Hangman Game" 
#Author: Jacob Møller & Oliver Thejl Eriksen
#Updated: 2/10 2018

import random
import hangmanascii

#Wordlist to choose from
dkWordList = ["Sporvogn", "Skole"]
#Chooses a random word in the wordlist array
dkWordNumberChosen = random.randint(0, len(dkWordList)-1)
#Selects the text based on the number
dkWord = dkWordList[dkWordNumberChosen]
#Prints underscores the number of letters
for i in range(len(dkWord)):
    print("_", end=" ")
    
#Calling hangman animation after 7 errors (wrong letters)
hangmanascii.hangman(7)



#Prints the word that the user should guess TEMPORARY
print(dkWord)
