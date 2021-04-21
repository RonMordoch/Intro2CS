from wordsearch import search_for_words

##############
# This function will check the check_for_words function from wordsearch.py.
# For explanation please refer to the README.
##############

WORD_LST1 = ['cat', 'cow', 'dog']
WORD_LST2 = []
WORD_LST3 = ['cat', 'Cat', 'cAt', 'caT']
ALL_WORDS_LIST = [WORD_LST1, WORD_LST2, WORD_LST3]


MATRIX1 = [['a', 'b', 'c', 'a', 't'],
           ['c', 'A', 't', 'A', 't'],
           ['c', 'a', 'd', 'o', 'g']
           ]
MATRIX2 = []
MATRIX3 = [['C', 'A', 'T', 'C'],
           ['A', 'T', 'A', 'T'],
           ['C', 'a', 't', 'W'],
           ['X', 'Y', 'Z', 'O']
           ]

EMPTY_LST = []


def check_search_matrix1():
    if search_for_words(WORD_LST1, MATRIX1) == ['cat', 'dog']:
        if search_for_words(WORD_LST2, MATRIX1) == EMPTY_LST:
            if search_for_words(WORD_LST3, MATRIX1) == ['cat', 'cAt']:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def check_search_matrix2():
    for word_lst in ALL_WORDS_LIST:
        if search_for_words(word_lst, MATRIX2) == EMPTY_LST:
            return True
        else:
            return False


def check_search_matrix3():
    if search_for_words(WORD_LST1, MATRIX3) == EMPTY_LST:
        if search_for_words(WORD_LST2, MATRIX3) == EMPTY_LST:
            if search_for_words(WORD_LST3, MATRIX3) == ['Cat']:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def check_search_for_words():
    if check_search_matrix1() is True:
        if check_search_matrix2() is True:
            if check_search_matrix3() is True:
                print("All tests succeed! Das ist Wunderbar!")
                return True
            else:
                print("MATRIX3 test failed!")
                return False
        else:
            print("MATRIX2 test failed!")
            return False
    else:
        print("MATRIX1 test failed!")
        return False


if __name__ == "__main__":
    check_search_for_words()
