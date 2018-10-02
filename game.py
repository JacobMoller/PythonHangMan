#Project Name: "Python Hangman Game" 
#Author: Jacob Møller & Oliver Thejl Eriksen
#Updated: 2/10 2018

import random
import hangmanascii

dkWordList = ["Sporvogn", "Skole"]
dkWordNumberChosen = random.randint(0, len(dkWordList)-1)
dkWord = dkWordList[dkWordNumberChosen]
print(dkWord)
for i in range(len(dkWord)):
    print("_", end=" ")

hangmanascii.hangmanOne()
