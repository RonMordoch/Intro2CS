##############################################################################
# We call the function with 3 numbers and the function returns
# the largest and smallest numbers by checking if the number is either
# larger than or equal to the other numbers for max_val, and
# smaller than or equal to the other numbers for min_val.
# max_val = the largest number min_val = the smallest number.
# The function returns the value and prints nothing to the screen.
##############################################################################


def largest_and_smallest(num_1, num_2, num_3):
    """This function, given three numbers, returns the maximum
    number and the minimum number out of the given numbers."""
    if num_1 >= num_2 and num_1 >= num_3:  # num_1 is the maximum
        max_val = num_1
    elif num_2 >= num_1 and num_2 >= num_3:  # num_2 is the maximum
        max_val = num_2
    else:  # num_3 is the maximum
        max_val = num_3
    if num_1 <= num_2 and num_1 <= num_3:  # num_1 is the minimum
        min_val = num_1
    elif (num_2 <= num_1) and (num_2 <= num_3):  # num_2 is the minimum
        min_val = num_2
    else:  # num_3 is the minimum
        min_val = num_3
    return max_val, min_val
