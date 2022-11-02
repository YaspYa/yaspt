# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
from tkinter.tix import Tree

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
      if letter not in letters_guessed:
        return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    word = ''

    for letter in secret_word:
      if letter in letters_guessed:
        word += letter
      else:
        word += '_ '

    return word



def get_available_letters(letters_guessed):
    all_letter = string.ascii_lowercase 
    avalible_letters = ''

    for letter in all_letter:
      if letter not in letters_guessed:
        avalible_letters += letter
    return avalible_letters



def minus_points (warnings_remainning,guess_remaining):
    if warnings_remainning != 0:
      warnings_remainning -=1
      reaction = f"Oops! You've already guessed that letter. You have {warnings_remainning} warnings left:"
    else:
      guess_remaining -=1
      reaction = f"Oops! You've already guessed that letter. You have no warnings left:"
    return  warnings_remainning, guess_remaining, reaction


def hangman(secret_word):
    letters_guessed = []
    guess_remaining = 6
    warnings_remainning = 3

    print(f'Welcome to the game Hangman!\nI am thinking of a word that is {len(secret_word)} letters long.\nYou have {warnings_remainning} warnings left.')
    print('-'*13)

    while guess_remaining != 0:
      print(f'You have {guess_remaining} left.')
      print(f'Available letters: {get_available_letters(letters_guessed)}')
      reaction = 'Good guess:'
      input_letter = input('Please guess a letter: ').lower()

      if input_letter in ['a','e','i','o','u']:
        minus_guess = 2
      else:
        minus_guess = 1

      if input_letter not in letters_guessed:
        if str.isalpha(input_letter) and len(input_letter) == 1:
          letters_guessed.append(input_letter)
          if input_letter not in secret_word:
            guess_remaining -=minus_guess
            reaction = 'Oops! That letter is not in my word:'
        else:
          warnings_remainning, guess_remaining, reaction = minus_points (warnings_remainning,guess_remaining)
      else:
        warnings_remainning, guess_remaining, reaction = minus_points (warnings_remainning,guess_remaining)
      
      print(reaction, get_guessed_word(secret_word, letters_guessed))
      print('-'*13)

      if is_word_guessed(secret_word, letters_guessed):
        print(f'Congratulations, you won! Your total score for this game is: {guess_remaining*len(set(secret_word))}')
        break
    
    if guess_remaining == 0:
      print(f'Sorry, you ran out of guesses. The word was {secret_word}')




def match_with_gaps(my_word, other_word):
    my_word = my_word.replace(' ','')
    if len(my_word) == len(other_word):
      set_Letters = set(my_word.replace('_',''))
      for letter in set_Letters:
        if my_word.count(letter) != other_word.count(letter):
          return False
      for i in range(len(my_word)):
        if my_word[i] != '_' and my_word[i] != other_word[i] :
          return False
      return True

    else:
      return False



def show_possible_matches(my_word):
    result = ''
    for other_word in wordlist:
      if match_with_gaps(my_word, other_word):
        result += other_word + ' '
    if result == '':
      result = 'No matches found'
    return result


def hangman_with_hints(secret_word):
    letters_guessed = []
    guess_remaining = 6
    warnings_remainning = 3

    print(f'Welcome to the game Hangman!\nI am thinking of a word that is {len(secret_word)} letters long.\nYou have {warnings_remainning} warnings left.')
    print('-'*13)

    while guess_remaining != 0:
      print(f'You have {guess_remaining} left.')
      print(f'Available letters: {get_available_letters(letters_guessed)}')
      reaction = 'Good guess:'
      input_letter = input('Please guess a letter: ').lower()

      if input_letter in ['a','e','i','o','u']:
        minus_guess = 2
      else:
        minus_guess = 1

      if input_letter != '*':
        if input_letter not in letters_guessed:
          if str.isalpha(input_letter) and len(input_letter) == 1:
            letters_guessed.append(input_letter)
            if input_letter not in secret_word:
              guess_remaining -=minus_guess
              reaction = 'Oops! That letter is not in my word:'
          else:
            warnings_remainning, guess_remaining, reaction = minus_points (warnings_remainning,guess_remaining)
        else:
          warnings_remainning, guess_remaining, reaction = minus_points (warnings_remainning,guess_remaining)
        print(reaction, get_guessed_word(secret_word, letters_guessed))     

      else:
        print('Possible word matches are:', show_possible_matches(get_guessed_word(secret_word, letters_guessed)))

      print('-'*13)
      
      if is_word_guessed(secret_word, letters_guessed):
        print(f'Congratulations, you won! Your total score for this game is: {guess_remaining*len(set(secret_word))}')
        break
    
    if guess_remaining == 0:
      print(f'Sorry, you ran out of guesses. The word was {secret_word}')



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    #hangman(secret_word)
    hangman_with_hints(secret_word)
