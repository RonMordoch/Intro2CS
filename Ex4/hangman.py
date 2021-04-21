import hangman_helper
from hangman_helper import *
import string

alphabet = list(string.ascii_lowercase)
CHAR_A = 97
UNDERSCORE = '_'


def update_word_pattern(word, pattern, letter):
    """
    Updates a given pattern depending if the word includes the letter.
    :param word: a given word
    :param pattern: a given pattern of equal length to word, made out of
            underscores : '_'
    :param letter: a single lowercase letter
    :return: If letter is in word, updates the given pattern into a new one
     containing the letter. Else, the pattern will not change.
    """
    # for every index in the word, if the index is the letter, update the
    # pattern the following way: up until the letter remains the same, insert
    # the letter, and print the rest.
    for i in range(len(word)):
        if word[i] == letter:
            pattern = pattern[:i] + letter + pattern[i + 1:]
    return pattern


def filter_words_list(words, pattern, wrong_guess_lst):
    """"Returns a filtered word list containing to most probable words
    out of the current list to give hints for."""
    new_words_list = []
    counter = 0
    for word in words:
        if len(word) != len(pattern):  # equal word length
            continue
        # else, equal length
        for i in range(len(word)):
            if word[i] != pattern[i] and pattern[i] != UNDERSCORE:
                counter += 1
                break  # word is not equal to pattern
            if word[i] in wrong_guess_lst:
                counter += 1
                break  # letter was guessed before
        if counter == 0:
            new_words_list.append(word)
        else:
            counter = 0
    return new_words_list


def letter_to_index(letter):
    """ Return the index of the given letter in an alphabet list. """
    return ord(letter.lower()) - CHAR_A


def index_to_letter(index):
    """ Return the letter corresponding to the given index. """
    return chr(index + CHAR_A)


def choose_letter(words, pattern):
    """" Return the most common letter out of a list of words."""
    new_list = [0] * 26
    for word in words:
        for letter in word:
            if letter not in pattern:  # letter not already in pattern
                index = letter_to_index(letter)  # turns letter to index
                new_list[index] += 1  # add 1 for each letter appearance
    largest_number = new_list.index(max(new_list))  # most common letter
    letter_hint = index_to_letter(largest_number)  # convert back to letter
    return letter_hint


def run_single_game(word_list):
    """"This function runs a single game of the classic 'Hangman.'
    Don't know how to play? please refer to:
    https://en.wikipedia.org/wiki/Hangman_(game)
    """

    # STAGE 1 #
    # sets the basic variables #
    word = get_random_word(word_list)  # use a built in function to get a word
    pattern = UNDERSCORE * len(word)  # pattern's length is same as word, hidden
    wrong_guess_lst = []  # wrong guesses list
    error_count = 0  # error count, corresponds to length of wrong_guess_lst
    already_guess_lst = []  # includes all the correct guesses
    msg = DEFAULT_MSG
    # changes depending on the situation, set to default built-in message

    # STAGE 2 #
    # starts the game #
    # game will continue will error count is smaller than built in variable
    # for max errors, and while the pattern is still part-hidden
    while error_count < MAX_ERRORS and UNDERSCORE in pattern:
        display_state(pattern, error_count, wrong_guess_lst, msg,
                      ask_play=False)  # shows the current status of the game
        # get_input returns a tuple of 2, the first one is the user choice
        choice, letter = get_input()
        if choice == HINT:  # if user asked for hint using GUI
            word_lst = filter_words_list(word_list, pattern, wrong_guess_lst)
            hint = choose_letter(word_lst, pattern)
            msg = HINT_MSG + hint
            display_state(pattern, error_count, wrong_guess_lst, msg,
                          ask_play=False)
        elif choice == LETTER:  # if user inserted a letter
            if len(letter) != 1:  # if user did not insert a single letter
                msg = NON_VALID_MSG
                continue  # wait for a valid input
            elif letter not in alphabet:  # if letter is not lowercase a-z
                msg = NON_VALID_MSG
                continue  # wait for a valid input
            elif letter in already_guess_lst:  # if letter was inserted before
                msg = ALREADY_CHOSEN_MSG + letter
            elif letter in word:  # if letter is indeed in word
                pattern = update_word_pattern(word, pattern, letter)
                already_guess_lst.append(letter)
                msg = DEFAULT_MSG
            elif letter not in word:
                if letter not in wrong_guess_lst:
                    wrong_guess_lst.append(letter)  # list of wrong guesses
                    error_count += 1  # add 1 to the error count
                msg = DEFAULT_MSG

    # STAGE 3 #
    # ENDGAME #
    if pattern == word:  # if user has successfully guessed the word
        msg = WIN_MSG  # built in message of winning
    else:  # the user failed and error_count >= MAX_ERRORS
        msg = LOSS_MSG + word  # built in message of losing, revealing the word
    ask_play = True  # shows the player the option to play again
    display_state(pattern, error_count, wrong_guess_lst, msg, ask_play)


def main():
    """"
    This is the main function. The function loads word from a given file,
    runs a single game, and then prompts the user if it wants to play a new
    game.
    """
    word_list = load_words()  # load words from given file
    run_single_game(word_list)  # runs a single game
    user_choice = get_input()  # test user for input
    while user_choice[0] == PLAY_AGAIN:
        if user_choice[1]:  # if user picks play again
            run_single_game(word_list)  # starts a new game
            user_choice = get_input()
        else:
            break


if __name__ == "__main__":
    hangman_helper.start_gui_and_call_main(main)
    hangman_helper.close_gui()
