#Project Name: "Python Hangman Game" 
#Author: Jacob Møller & Oliver Thejl Eriksen
#Updated: 2/10 2018

import random

dkWordList = ["Sporvogn", "Skole"]
dkWordNumberChosen = random.randint(0, len(dkWordList)-1)
dkWord = dkWordList[dkWordNumberChosen]
print(dkWord)
for i in range(len(dkWord)):
    print("_", end=" ")
def hangmanOne():
    print("")
    print("    ————--")
    print("    |    |")
    print("    |           ")
    print("    |        ")
    print("    |     ")
    print("  / | \       ")
    print("/   |   \ ")
hangmanOne()
