# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
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
    secretWord = secretWord.lower()
    secret_letters = []
    for i in range(0, len(secretWord)):
        secret_letters.append(secretWord[i])
    for letter in secret_letters:
        if letter in lettersGuessed:
            result = True
        else:
            return False
            break
    return result


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secretWord = secretWord.lower()
    secret_letters = []
    guess_result = ''
    for i in range(0, len(secretWord)):
        secret_letters.append(secretWord[i])
    for letter in secret_letters:
        if letter in lettersGuessed:
            guess_result = guess_result + letter
        else:
            result = False
            guess_result = guess_result + "_ "
    return guess_result


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    letters = ''
    for i in alphabet:
        if i not in lettersGuessed:
            letters = letters + i
    return letters


def check_letter(secretWord, letter):
    secretWord = secretWord.lower()
    if letter in secretWord:
        return True
    else:
        return False


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
    guesses_number = 8
    letters_guessed = []
    print("Welcome to the game, Hangman! \nI am thinking of a word that is " + str(
        len(secretWord)) + " letters long. \n-------------")
    while guesses_number > 0:
        print("You have " + str(guesses_number) + " guesses left.")
        print("Available letters: " + str(getAvailableLetters(letters_guessed)))
        letter = input("Please guess a letter: ").lower()
        if letter in getAvailableLetters(letters_guessed):
            letters_guessed.append(letter)
            if check_letter(secretWord, letter):
                print("Good guess: " + getGuessedWord(secretWord, letters_guessed) + "\n-------------")
            else:
                print("Oops! That letter is not in my word: " + getGuessedWord(secretWord,
                                                                               letters_guessed) + "\n-------------")
                guesses_number -= 1
        else:
            letters_guessed.append(letter)
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord,
                                                                                letters_guessed) + "\n-------------")
        if isWordGuessed(secretWord, letters_guessed):
            print("Congratulations, you won!")
            game_result = True
            break
        else:
            game_result = False
    if game_result is False:
        print("Sorry, you ran out of guesses. The word was " + secretWord)


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)