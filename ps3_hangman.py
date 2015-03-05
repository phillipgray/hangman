# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secretWordList = []
    for char in secretWord:
        if char in secretWordList:
            pass
        else:
            secretWordList.append(char)
    #print secretWordList
    for i in secretWordList:
        if i not in lettersGuessed:
            #print i + " not in letters guessed"
            return False
        else:
            #print i + " in letters guessed"
            pass
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secretWordList = []
    guessedWordList = []

    for char in secretWord:
        secretWordList.append(char)
    #print secretWordList
    for i in secretWordList:
        if i not in lettersGuessed:
            #print i + " not in letters guessed"
            guessedWordList.append("_ ")
        else:
            #print i + " in letters guessed"
            guessedWordList.append(i + " ") 
    #print guessedWordList
    currentGuessedWord = "".join(guessedWordList)
    #print currentGuessedWord
    return currentGuessedWord



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    leftoverLettersList = []
    for char in string.ascii_lowercase:
        # print char
        if char not in lettersGuessed:
            # print "added %s" % (char)
            leftoverLettersList.append(char)
        # print leftoverLettersList
    leftoverLetters = "".join(leftoverLettersList)
    return leftoverLetters
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    import string

    # important variables
    keepPlayingTrigger = True
    livesNumber = 8
    availableLetters = string.ascii_lowercase
    lettersGuessedList = []
    endMessage = ""

    # game beginning sequence
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is %s letters long." % (str(len(secretWord)))

    # main game sequence
    while keepPlayingTrigger == True:
        print "-------------"
        print "You have %s guesses left." % (livesNumber)
        availableLetters = getAvailableLetters(lettersGuessedList)
        print "Available letters: %s" % (availableLetters)
        
        # take guessed letter, make it lowercase, and then check to see if it's already guessed 
        currentLetter = raw_input("Please guess a letter: ")
        currentLetterLower = currentLetter.lower()
        if currentLetterLower in lettersGuessedList:
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessedList)
            continue

        # add guessed letter to the list of guessed letters
        lettersGuessedList.append(currentLetterLower)

        # wrong letter guess
        if lettersGuessedList[-1] not in secretWord:
            print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessedList)
            livesNumber -= 1

        elif lettersGuessedList[-1] in secretWord:
            print "Good guess: " + getGuessedWord(secretWord, lettersGuessedList)
                
        keepPlayingTrigger = not isWordGuessed(secretWord, lettersGuessedList) and livesNumber != 0
    

    # end of game: two options: 1) out of guesses and 2) you guessed the word
    else:
        print "-------------"
        # print livesNumber
        if livesNumber == 0:
            endMessage = "Sorry, you ran out of guesses. The word was %s." % (secretWord)
        elif isWordGuessed(secretWord, lettersGuessedList):
            endMessage = "Congratulations, you won!"
    return endMessage

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = 'hello'
# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)