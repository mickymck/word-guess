# open the word file and turn it into a list - DONE
# computer must select a random word - DONE
# computer must hold the value of the random word - DONE
# computer must display Game Field - starting with an underscore for each letter of the random word - DONE
# computer must display Guess Count, starting at 8 - DONE
# computer must prompt user to make a guess
# user must be able to input a guess
# computer must compare guessed letter to each letter in list of letters that make up random word
# if guess is correct, computer must replace underscore with guessed letter at the same index at which the letter is found in the random word
# if guess is incorrect, computer must subtract "remaining guesses" by 1
# game ends when Guess Count = 0, or when there are no underscores remaining

import random

# turn words.txt into a list of words
with open ("words.txt") as file:
    word_bank = file.read().split()

# function to choose a random number between 0 and the end of the word bank list, and make that the word index I wish to grab, then return the word
def choose_random_word(word_bank):
    random_index = (random.randrange(0, len(word_bank), 1))
    random_word = word_bank[random_index]
    return random_word

# creates a list of underscores, one for each letter in the random word
def show_blanks(random_word):
    blanks = []
    blanks.append('_ ' * len(random_word))
    return blanks

# display the number of remaining guesses
def guess_count(guesses):
    remaining = (8 - guesses)
    return remaining

# computer must prompt the user to make a guess
def prompt_guess():
    letter_guess = input("Give me a letter. ANY letter! - " )
    return letter_guess

def run_game():
    # grab the word at word_bank[index] based on random number
    random_word = choose_random_word(word_bank)
    print(random_word)
    game_board = show_blanks(random_word)
    print(game_board)
    remaining_guesses = guess_count(0)
    print(remaining_guesses)
    opening_prompt = prompt_guess()
    print(opening_prompt)
    

run_game()
