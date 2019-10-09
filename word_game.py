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
    return random_word.lower()

# fix it so that the guess count goes down with every wrong guess, and that the game ends when guess-count = 0

def run_game():
    game_over = False
    game_board = []
    user_guesses = []
    wrong_guesses = []

    random_word = choose_random_word(word_bank)
    print(random_word)

    if len(user_guesses) == 0:
        game_board.append('_ ' * len(random_word))
        print(' '.join(game_board))

    while game_over == False:

        guess_count = 8 - len(wrong_guesses)
        print("Remaining guesses: ", guess_count)
        print(wrong_guesses)

        guess = input("Give me a letter. ANY letter! - " )
        user_guesses.append(guess)
        game_board = []

        for letter in random_word:
            if letter in user_guesses:
                game_board.append(letter)
            else:
                game_board.append('_')

        for guess in user_guesses:
            if guess not in random_word and guess not in wrong_guesses:
                wrong_guesses.append(guess)

        print(' '.join(game_board))

        if guess_count < 1:
            game_over = True
            print("Game Over. Play again.")
        if "_" not in game_board:
            game_over = True
            print("Game Over. You win.")
    
run_game()
