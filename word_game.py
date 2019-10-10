
import random

# turn words.txt into a list of words
with open ("words.txt") as file:
    word_bank = file.read().split()

easy_words =[]
medium_words = []
hard_words = []

def easy_medium_hard (word_bank):
    for word in word_bank:
        if len(word) > 3 and len(word) < 7:
            easy_words.append(word)
        if len(word) > 6 and len(word) < 9:
            medium_words.append(word)
        if len(word) > 8:
            hard_words.append(word)

easy_medium_hard(word_bank)

# function to choose a random number between 0 and the end of the word bank list, and make that the word index I wish to grab, then return the word
def choose_random_word(list):
    random_index = (random.randrange(0, len(list), 1))
    random_word = list[random_index]
    return random_word.lower()

def run_game():
    game_over = False
    game_board = []
    user_guesses = []
    wrong_guesses = []
    guess_count = 8

    print("Word Guess: where I know a word, and you don't!")

    level = input("Choose difficulty level: [E]asy [M]edium or [H]ard: " )

    if level == "e" or level == "E":
        random_word = choose_random_word(easy_words)
    elif level == "m" or level == "M":
        random_word = choose_random_word(medium_words)
    elif level == "h" or level == "H":
        random_word = choose_random_word(hard_words)


    if len(user_guesses) == 0:
        game_board.append('_ ' * len(random_word))
        print('')
        print('')
        print(' '.join(game_board))
        print('')

    while game_over == False:
        print('')
        print("Remaining guesses: ", guess_count)
        print('')
        print("Wrong guesses: ", wrong_guesses)
        print('')

        guess = input("Give me a letter. ANY letter! - " )
        print('')
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

        guess_count = 8 - len(wrong_guesses)

        if guess_count == 0:
            game_over = True
            print('')
            print("Game Over. You did not win.")
            print('')
            print("The word was", random_word)
            print('')
        if "_" not in game_board:
            game_over = True
            print('')
            print("Game Over. You win.")
            print('')
    
run_game()
