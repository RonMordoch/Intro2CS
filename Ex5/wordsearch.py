import sys
import os
import re
from copy import deepcopy

VALID_DIRECTIONS = ['u', 'd', 'r', 'l',
                    'w', 'x', 'y', 'z']
MAX_ARGS_MESSAGE = "You have entered an invalid number of parameters." \
                   "Please enter 4 parameters, in addition to the script."
WRONG_DIRECTION_PARAMETER = "You have entered a wrong direction parameter. " \
                            "Please enter a valid choice."
NO_FILE_EXISTS = "File does not exist. Please choose a valid file."
MAX_ARGS_NUM = 5


def check_parameter_count(args):
    """
    :param args: Arguments supplied by the user through sys.argv.
    :return: Error message if not 5 arguments were received, else None.
    """
    if len(args) != MAX_ARGS_NUM:
        return MAX_ARGS_MESSAGE
    else:
        return None


def does_file_exist(file):
    """
    :param file: a file that either exists or not.
    :return: True if file exist, else False.
    """
    return os.path.exists(file)


def check_existing_file_word(args):
    """
    Checks is word file exist.
    :param args: Supplied by the user through sys.argv.
    :return: None is file exists, error message if file does not exist.
    """
    if does_file_exist(args[1]):  # if file exists
        return None
    else:  # file does not exist
        return NO_FILE_EXISTS


def check_existing_file_matrix(args):
    """
    Checks is matrix file exist.
    :param args: Supplied by the user through sys.argv.
    :return: None is file exists, error message if file does not exist.
    """
    if does_file_exist(args[2]):  # if file exists
        return None
    else:  # file does not exist
        return NO_FILE_EXISTS


def check_direction_parameter(args):
    """
    Check if direction string is valid - i.e., containing letter only out
    of the constant list VALID_DIRECTIONS.
    :param args: Supplied by the user through sys.argv.
    :return: None is direction string is correct, error message if not.
    """
    direction_string = args[4]
    for letter in direction_string:
        if letter not in VALID_DIRECTIONS:  # not a valid direction
            return WRONG_DIRECTION_PARAMETER
        else:  # a valid direction
            return None


def check_input_args(args):
    """
    Runs the previously defined functions one by one. If all pass
    successfully, i.e. all return None, the function will return none.
    Else is will return the appropriate message of the test that failed.
    :param args: Supplied by the user through sys.argv.
    :return: None if all tests passed else the matching error message.
    """
    if check_parameter_count(args) is None:
        if check_existing_file_word(args) is None:
            if check_existing_file_matrix(args) is None:
                if check_direction_parameter(args) is None:
                    return None  # all tests passed
                else:
                    return check_direction_parameter(args)  # this test failed
            else:
                return check_existing_file_matrix(args)  # this test failed
        else:
            return check_existing_file_word(args)  # this test failed
    else:
        return check_parameter_count(args)  # this test failed


##############################################################################


def read_wordlist_file(filename):
    """
    Reads a file with words and return a list of words.
    :param filename: Supplied by the user through sys.argv, contains words,
    each word separated by new line.
    :return: A new list, each element in the list is a word from the file.
    """
    word_list = []
    with open(filename, 'r') as words:
        for line in words:
            word = line.strip()  # removes '\n'
            word_list.append(word)
    return word_list


def read_matrix_file(filename):
    """
    Reads a file with matrix-formatted letters and return a list of lists.
    :param filename: Supplied by the user through sys.argv, contains lines
    of letters seperated by commas, each line is of equal length.
    :return: A list of list, each sub-list is a line from the file.
    """
    matrix = []
    with open(filename, 'r') as matrix_letters:
        for line in matrix_letters:
            line = line.strip().split(',')  # split the lines and remove '\n'
            matrix.append(line)
    return matrix


##############################################################################
# The following 7 functions receives the original matrix and re-position the
# letters and lines to accommodate a specific search direction.
# The original matrix is left to right.
# For explanation on diagonal matrix calculations please use the README.


def right_to_left_matrix(matrix):  # LEFT TO RIGHT
    """Receives LTR matrix and returns RTL matrix."""
    rtl_matrix = deepcopy(matrix)
    for row in rtl_matrix:
        rtl_matrix[:] = row[::-1]  # reverse rows
    return rtl_matrix


def down_direction_matrix(matrix):  # DOWNWARD
    """Receives LTR matrix and returns downward matrix."""
    return [[letter[i] for letter in matrix] for i in range(len(matrix[0]))]


def up_direction_matrix(matrix):  # UPWARD
    """Receives LTR matrix, reverse it, and returns upward matrix."""
    reverse_matrix = deepcopy(matrix[::-1])
    return [[letter[i] for letter in reverse_matrix]
            for i in range(len(reverse_matrix[0]))]


def right_down_matrix(matrix):  # RIGHT UP#
    """Receives LTR matrix and returns right-down diagonal matrix."""
    row_count = len(matrix)
    column_count = len(matrix[0])
    return [[matrix[row_count - p + q - 1][q]
             # -1 removes the longest diagonal appearing twice
             for q in
             range(max(p - row_count + 1, 0), min(p + 1, column_count))]
            for p in range(row_count + column_count - 1)]


def right_up_matrix(matrix):
    """Runs the right-down diagonal function on a reverse matrix,
    thus returning right-up matrix."""
    reverse_matrix = deepcopy(matrix[::-1])
    return right_down_matrix(reverse_matrix)


def left_down_matrix(matrix):
    """Receives RTL matrix and runs the right-down diagonal function on
    a RTL matrix, thus returning left-down-matrix."""
    rtl_matrix = right_to_left_matrix(matrix)
    return right_down_matrix(rtl_matrix)


def left_up_matrix(matrix):
    """Receives RTL matrix and runs the right-down diagonal function on
    a reverse-RTL matrix, thus returning left-up-matrix."""
    rtl_matrix = right_to_left_matrix(matrix)
    reverse_rtl_matrix = deepcopy(rtl_matrix[::-1])
    return right_down_matrix(reverse_rtl_matrix)


##############################################################################


def search_for_words(word_list, matrix):
    """
    Receives a word list and a matrix of letters and return a list of the
    words found.
    :param word_list: List of words.
    :param matrix: List of lists, each sub-list containing letters.
    :return: List all of the words found.
    """
    results = []  # create empty list
    for word in word_list:
        for line in matrix:
            line_string = ''.join(line)  # concatenate letters into string
            matches = re.findall(r'(?=(' + word + '))', line_string)
            # find all overlapping matches of word in line
            results.extend(matches)
    return results


def return_dictionary(lst):
    """
    Receives a list of words and returns a dictionary with the word
    appearances counted as the value, and word itself as key.
    :param lst: list of words.
    :return: Dictionary, key is a word, value is the word's number of
    appearances.
    """
    dictionary = dict()  # create empty dictionary
    for word in lst:
        if word in dictionary.keys():
            dictionary[word] += 1  # count +1
        else:
            dictionary[word] = 1  # already counted
    return dictionary


def find_words_in_matrix(word_list, matrix, directions):
    """
    Find words from list in matrix according to given directions.
    :param word_list: List containing words.
    :param matrix: List of lists, each sub-list containing letters.
    :param directions: A string of directions, each direction leads to
    changing the matrix for the appropriate search direction.
    Here there will be no need to check for invalid direction because in
    the main function we will run this only after running the arguments
    checking functions.
    :return: list of tuples, each tuple contain a word and the number of times
    the word appeared.
    """
    results = []
    if "r" in directions:  # search right
        results.append(search_for_words(word_list, matrix))
    if "l" in directions:  # search left
        results.append(search_for_words(word_list,
                                        right_to_left_matrix(matrix)))
    if "u" in directions:  # search up
        results.append(search_for_words(word_list,
                                        up_direction_matrix(matrix)))
    if "d" in directions:  # search down
        results.append(search_for_words(word_list,
                                        down_direction_matrix(matrix)))
    if "w" in directions:  # search right-up
        results.append(search_for_words(word_list,
                                        right_up_matrix(matrix)))
    if "x" in directions:  # search left-up
        results.append(search_for_words(word_list,
                                        left_up_matrix(matrix)))
    if "y" in directions:  # search right-down
        results.append(search_for_words(word_list,
                                        right_down_matrix(matrix)))
    if "z" in directions:  # search left-down
        results.append(search_for_words(word_list,
                                        left_down_matrix(matrix)))
    all_results = [word_found for lst in results for word_found in lst]
    # append all of the results into a one dimensional list
    word_dic = return_dictionary(all_results)
    # create a dictionary of all results with number of appearances
    return list(word_dic.items())
    # return a list of tuples containing word and appearances count


##############################################################################


def write_output_file(results, output_filename):
    """
    Receives result list of tuples and file name and create the file with
    each tuple written in a single line.
    :param results: List of tuples.
    :param output_filename: Desired output file name.
    :return: A new file with each tuples written as a string in a single
    line.
    """
    with open(output_filename, 'w') as output_file:  # open/override file
        list_results_string = [[str(result) for result in result_tuple]
                               for result_tuple in results]
        # convert tuples into lists inside list
        for lst in list_results_string:
            lst = " , ".join(lst)  # join each list into a single string
            output_file.write(lst + "\n")
            # write to file with new line after each result


##############################################################################


def main(args):
    """
    The following function is the main function, running all the previously
    defined function.
    :param args: Arguments received from the command prompt.
    :return: A new file with results inside.
    """
    if check_input_args(args) is None:  # all arguments tests passed
        word_list = read_wordlist_file(sys.argv[1])  # load word list
        matrix = read_matrix_file(sys.argv[2])  # load matrix
        directions = sys.argv[4]  # load directions
        results = find_words_in_matrix(word_list, matrix, directions)
        output_filename = sys.argv[3]  # desired output filename
        write_output_file(results, output_filename)  # create output file

    else:  # at least one of the arguments tests failed
        print(check_input_args(args))  # print the appropriate error message


if __name__ == "__main__":
    main(sys.argv)
