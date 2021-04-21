import math


##############################################################################
#                   S U D O K U   S O L V E R                                #

# In the following functions:
# i,j represent indexes of row, column respectively

def is_empty(board, lst):
    """
    Checks if board is empty.
    :param board: 2d list representing sudoku board
    :param lst: index list
    :return: True if board is empty, else board is solved - return True
    """
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:  # empty cell
                lst[0] = i  # row index
                lst[1] = j  # column index
                return True
    # else board is solved
    return False


def search_rows(board, i, num):
    """
    Checks if a number placement is valid within a row.
    :param board: 2d list representing sudoku board
    :param i: row index
    :param num: integer
    :return: False if num already in row, else True
    """
    for j in range(len(board)):
        if board[i][j] == num:  # num already in row
            return False
    # else num is a valid placement
    return True


def search_columns(board, j, num):
    """
    Checks if a number placement is valid within a column.
    :param board: 2d list representing sudoku board
    :param j: colum index
    :param num: integer
    :return: False if num already in column, else True
    """
    for i in range(len(board)):
        if board[i][j] == num:  # num already in column
            return False
    # else num is a valid placement
    return True


def search_grids(board, i, j, num):
    """
    Checks if a number placement is valid within a squared grid.
    :param board: 2d list representing sudoku board
    :param i: row index
    :param j: col index
    :param num: integer
    :return:False if num already in grid, else True
    """
    for row in range(int(math.sqrt(len(board)))):
        for column in range(int(math.sqrt(len(board)))):
            if board[i + row][j + column] == num:
                return False
    # else num is a valid placement
    return True


def valid_location(board, i, j, num):
    """
    Checks if a the given location for a number is valid using the
    previous functions.
    :param board: 2d list representing sudoku board
    :param i: row index
    :param j: column index
    :param num: integer
    :return: True if number can be placed, else location is invalid and
    return False.
    """
    squared_value = int(math.sqrt(len(board)))  # grid size
    grid_border1 = i - i % squared_value  # grid row border
    grid_border2 = j - j % squared_value  # grid column border

    # If number is valid inside the row, column and squared grid:
    if search_rows(board, i, num) and search_columns(board, j, num) \
            and search_grids(board, grid_border1, grid_border2, num):
        return True
    # else num is an invalid choice for either row, column or grid
    return False


def board_solver(board):
    """
    This function attempts to solve the sudoku if possible.
    If sudoku is solvable, return the solved board and True.
    Else, sudoku has no solution, return False.
    :param board:
    :return:
    """
    lst = [0, 0]  # initialize indexes

    # checks if board is empty
    if is_empty(board, lst) is False:
        return True  # board is already solved, return True

    # else, set the starting position at the top left corner of board
    i = lst[0]  # row index
    j = lst[1]  # column index

    # iterate over the numbers that are possible insertions to board
    for num in range(1, len(board) + 1):  # 1 to 'n' including 'n'
        if valid_location(board, i, j, num):  # valid placement for num
            board[i][j] = num

            # checks if board is solved after number placement.
            # if not, backtrack and continue.
            if board_solver(board):
                return board, True

            # backtracking step
            board[i][j] = 0
    # no solution was found, return False
    return False


def solve_sudoku(board):
    """
    This function runs the board_solver.
    If a solution was found, empty board will be changed to a solved one,
    and the function will return True.
    Else - function returns False.
    :param board: sudoku board
    :return: True is solved, else False
    """
    # If board_solver returned 2 values, it means board is solvable.
    # Set board to become the solved board, and return the True value
    try:
        board, value = board_solver(board)
        return value

    # is board_solver returned only 1 element, and can't unpack 2 out of 1,
    # the only option is that board_solver returned False.
    # therefore, no solution was found - return False
    except TypeError:
        return False


##############################################################################
#                         K _ S U B S E T                                    #
# Function #1

def print_set(cur_set):
    """
    Prints the sub-set.
    :param cur_set: Current set
    :return: None
    """
    lst = []
    for idx, in_cur_set in enumerate(cur_set):
        if in_cur_set:
            lst.append(idx)
    print(lst)  # print the sub set


def print_k_subset_helper(cur_set, k, index, picked):
    """
    Runs recursively to and uses the print_set to print the subsets.
    :param cur_set: Current set
    :param k: Subset length
    :param index: given index
    :param picked: numbers picked
    :return:
    """
    if k == picked:  # base case
        print_set(cur_set)
        return
    if index == len(cur_set):
        return
    cur_set[index] = True
    print_k_subset_helper(cur_set, k, index + 1, picked + 1)
    cur_set[index] = False
    print_k_subset_helper(cur_set, k, index + 1, picked)


def print_k_subsets(n, k):
    """
    Prints all sub-sets of (0,1,..,n-1) of k-length.
    :param n: integer
    :param k: integer
    :return: None
    """
    if k <= n:
        cur_set = [False] * n
        print_k_subset_helper(cur_set, k, 0, 0)


# Function #2

def append_set(cur_set, lst):
    """
    Append all subsets to a list.
    :param cur_set: current set
    :param lst: list that will contain all sub sets
    :return: list will all sub sets
    """
    subset = []
    for idx, in_cur_set in enumerate(cur_set):
        if in_cur_set:
            subset.append(idx)
    lst.append(subset)


def fill_k_subset_helper(cur_set, k, index, picked, lst):
    """
    Runs recursively to and uses the append_set to append the subsets.
    :param cur_set: current set
    :param k: length
    :param index: integer
    :param picked: integer
    :param lst: a lst with subsets
    :return: None
    """
    if k == picked:
        append_set(cur_set, lst)
        return
    if index == len(cur_set):
        return
    cur_set[index] = True
    fill_k_subset_helper(cur_set, k, index + 1, picked + 1, lst)
    cur_set[index] = False
    fill_k_subset_helper(cur_set, k, index + 1, picked, lst)


def fill_k_subsets(n, k, lst):
    """Fill a list with all sub-sets of (0,1,..,n-1) of k-length."""
    if k <= n:
        cur_set = [False] * n
        fill_k_subset_helper(cur_set, k, 0, 0, lst)


# Function #3

def return_k_subsets_helper(n, k, picked, start):
    """
    A helper function that return a list of subsets
    :param n: numbers from 1 to n - 1
    :param k: length of desired subset
    :param picked: items picked
    :param start: starting point
    :return: list of subsets
    """
    if k == picked:
        return [[]]

    res = []
    for i in range(start, n):
        lists_with_i = return_k_subsets_helper(n, k, picked + 1, i + 1)
        for lst in lists_with_i:
            lst.append(i)
            lst.sort()
        res += lists_with_i

    return res


def return_k_subsets(n, k):
    """
    Uses the recursive helper function to return all subsets inside a list.
    :param n: integer
    :param k: subset length
    :return: all subsets inside a list
    """
    return return_k_subsets_helper(n, k, 0, 0)
