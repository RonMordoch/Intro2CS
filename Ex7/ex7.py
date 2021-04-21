def print_to_n(n):
    """
    Prints all the integers from 1 to n.
    :param n: integer, last number printed.
    """
    if n < 1:  # function not defined for values less than 1
        return
    if n == 1:  # base case
        print(n)
    if n > 1:
        print_to_n(n - 1)  # run recursively to print 1 and then the rest
        print(n)


def print_reversed(n):
    """
    Print all the integers from n to 1
    :param n: integer, first number printed
    """
    if n < 1:
        return
    if n == 1:  # base case
        print(n)
    if n > 1:
        print(n)  # prints the number
        print_reversed(n - 1)  # recursively prints next number, n - 1, to 1


def has_divisor_smaller_than(n, i):
    """
    Check if number has a divisor smaller than i.
    :param n: integer
    :param i: integer
    :return: True if there is a larger divisor than 1, else false.
    """
    if i > 1:
        if n % i == 0:
            return True
        return has_divisor_smaller_than(n, i - 1)
    else:  # we reached base case of i = 1, no divisor other than 1
        return False


def is_prime(n):
    """
    Checks if a number is prime.
    :param n: integer
    :return: True if number is prime, False is number is not prime or <=1.
    """
    if n <= 1:  # under the assumption 1 is not prime
        return False
    return not has_divisor_smaller_than(n, int(n / 2))  # see helper function


def factorial(n):
    """
    :param n: integer
    :return: n!
    """
    if n < 2:  # per instructions, we can assume n >= 0.
        return 1  # by definition 0! = 1 and 1! = 0.
    return n * factorial(n - 1)


def exp_n_x(n, x):
    """
    Calculates the exponential sum.
    :param n: integer
    :param x: number
    :return: The exponential sum.
    """
    if n == 0 or x == 0:
        return 1  # 0**x = 1 for all x, x**0 = 1 for all x
    return (x ** n) / factorial(n) + exp_n_x(n - 1, x)


def play_hanoi(hanoi, n, src, dest, temp):
    """
    :param hanoi: the graphics we use to change the GUI
    :param n: integer, number of discs the function moves
    :param src: source, the pole which the discs move from
    :param dest: destination, the pole which the discs move to
    :param temp: the remaining pole
    :return: None is n<=0, else runs game.
    #"""
    # hanoi.move(src, dest) - moves discs from source to destination
    # if src is empty or upper disc in src is larger than dest's upper disc,
    # we will receive an error.
    if n <= 0:
        return
    elif n == 1:
        hanoi.move(src, dest)  # from src to dest
    elif n == 2:
        hanoi.move(src, temp)  # from src to temp
        hanoi.move(src, dest)  # from src to dest
        hanoi.move(temp, dest)  # from temp to dest
    else:  # n > 2
        play_hanoi(hanoi, n - 1, src, temp,
                   dest)  # runs recursively until n = 2
        hanoi.move(src, dest)  # moves the third disc to dest
        play_hanoi(hanoi, n - 1, temp, dest, src)
        # runs recursively with temp as source, destination, and src as temp


def print_sequences_helper(n, start, char_list):
    """
    Prints all possible n-length sequences of char list
    :param n: integer
    :param start: first char, will be an empty string in main function
    :param char_list: list containing different chars
    """
    if len(start) == n:  # base case
        print(start)
    else:
        for char in char_list:
            print_sequences_helper(n, start + str(char), char_list)


def print_sequences(char_list, n):
    """
    Runs the helper function to print all sequences.
    :param char_list: list containing different chars
    :param n: integers
    :return: None if n = 0
    """
    if n == 0:
        return
    print_sequences_helper(n, "", char_list)
    #  runs with empty string as the first char


def print_no_repetition_sequences_helper(n, start, char_list):
    """
    Prints all sequences with no repetition of chars
    :param n: integer
    :param start: First char
    :param char_list: list containing different chars
    """
    i = 0  # initialize index for loop
    while i < len(char_list):
        if i == len(char_list) - 1:
            pass  # execute the next statement
        else:
            new_pre = start + str(char_list[i])  # adds the next letter
            if len(new_pre) == n:  # word is n-length
                print(new_pre)
            else:
                sliced_list = char_list[:i] + char_list[
                                              i + 1:]  # a new char list
                print_no_repetition_sequences_helper(n, new_pre, sliced_list)
        i += 1  # add one to index in order to eventually stop the loop


def print_no_repetition_sequences(char_list, n):
    """
    Runs the helper function to print all sequences with chars appearing only
    once in each sequences
    :param char_list: list containing different chars
    :param n: integer
    :return: None if n = 0
    """
    if n == 0:
        return
    else:
        extended_char_list = char_list + [""]  # list for helper function
        print_no_repetition_sequences_helper(n, "", extended_char_list)
        #  runs the helper function with empty string as start and the
        # extended list as char list


def parentheses(n):
    """
    :param n: integer
    :return: all possible combinations of valid n-length pair of parentheses
    """
    return paren_helper(n, 0, 0, "")


def paren_helper(n, left, right, string, results=[]):
    """
    :param n: integer
    :param left:
    :param right:
    :param string:
    :param results:
    :return: list containing all possible combinations of valid n-length
    pairs of parentheses
    """
    if right == n:  # valid pair
        results.append(string)
    if left < n:  # recursively run with left + 1
        paren_helper(n, left + 1, right, string + "(")
    if right < left:  # recursively run with right + 1
        paren_helper(n, left, right + 1, string + ")")
    return results


def permutation_helper(lst):
    """
    A helper function for up_and_right.
    :param lst: a list containing characters, duplicates allowed
    :return: All possible permutations of the characters
    """
    if len(lst) <= 1:
        return [lst]
    result = []  # empty lst
    for char in set(lst):  # iterate over the unique characters to avoid dupes
        temp_lst = lst.copy()  # new lst
        temp_lst.remove(char)  # remove iterated char for next iteration
        result += [[char] + perm for perm in permutation_helper(temp_lst)]
        # add char + permutations of the next chars is added to result list
    return result


def up_and_right(n, k):
    """
    The valid directions from (0,0) to (n,k) are ( n * right steps ) +
    (k * up steps), i.e. the permutations of the list containing those.
    :param n: integer representing the amount of right step to target axis
    :param k: integer representing the amount of up step to target axis
    Prints all possible directions to target.
    """
    up = k * "u"  # all up-ward steps
    right = n * "r"  # all down-ward steps
    if n == 0 and k == 0:  # destination is target
        return None
    if n == 0 and k != 0:  # move only up-ward
        print(up)
    elif n != 0 and k == 0:  # move only right-ward
        print(right)
    else:
        directions_to_target = list(right) + list(up)  # all moves
        all_sequences = permutation_helper(directions_to_target)
        # all permutations of move list
        for sequence in all_sequences:
            if sequence.count("r") == n and sequence.count("u") == k:
                # validate the moves
                print("".join(sequence))  # prints string of each move


def flood_fill_helper(image, i_start, j_start):
    """
    Receives image and recursively fills empty cells per exercise definition
    :param image: 2d list
    :param i_start: row starting index
    :param j_start: column starting index
    """
    if image[i_start][j_start] != "*":  # empty cell
        image[i_start][j_start] = "*"  # fill cell

        if i_start != 0:  # runs on the previous row
            flood_fill_helper(image, i_start - 1, j_start)
        if j_start != 0:  # runs on the previous column
            flood_fill_helper(image, i_start, j_start - 1)
        if i_start != len(image) - 1:  # runs on the next row
            flood_fill_helper(image, i_start + 1, j_start)
        if j_start != len(image[0]) - 1:  # runs on the next column
            flood_fill_helper(image, i_start, j_start + 1)


def flood_fill(image, start):
    """
    The function changes a 2d list representing an image and returns nothing
    :param image: 2d list
    :param start: starting index
    """
    i_start, j_start = start
    flood_fill_helper(image, i_start, j_start)
