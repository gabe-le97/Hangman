"""
------------------------------------------
File: Hangman.py
Author: Gabe Le
Note: Plays the game hangman with a computer which randomly
 picks the letters and has a predetermined amount of tries until it loses
------------------------------------------
"""
#------------------------------------------
import string
import random

# makes a blank representation of the word with dashes -
def fillBlanks(word):
    blank = []
    for i in range(0, len(word)):
        blank.append('-')
    return blank


# if a letter is correctly guessed place it where it belongs
def addLetter(letter, word, blanks):
    guess = list(word)
    count = 0
    for i in guess:
        if (i == letter):
            blanks[count] = letter
        count += 1
    return blanks


# check if the word is solved
def wordGuessed(word, B):
    if word == ''.join(B):
        return 1
    else:
        return 0

# show the blanks every time the computer guesses
def displayBlanks(blanks):
    print("The word you are guessing looks like this: ")
    print(" ")
    print(''.join(blanks))
    print(" ")
    return

# computer will pick a random letter to guess
def computerPlayer(myList):
    guess = random.randrange(0, len(myList)-1)
    return myList[guess]


# removes a letter from the computer so it doesn't pick it twice
def removeLetter(myList, letter):
    myList.remove(letter)
    return


def main():
    alpha = list(string.ascii_lowercase)
    word = input("Player 1 choose a word: ")
    myList = fillBlanks(word)
    maxGuesses = 10
    guesses = 0
    found = 0

    while (found == 0) and (guesses < maxGuesses):
        displayBlanks(myList)
        letter = computerPlayer(alpha)
        if letter in word:
            myList = addLetter(letter, word, myList)
            found = wordGuessed(word, myList)
        else:
            guesses = guesses + 1
        removeLetter(alpha, letter)

    if guesses >= maxGuesses:
        print("Too many guesses. You lose, the word was", word)
    else:
        print("Nice job! Good Guessing")
        displayBlanks(myList)

main()