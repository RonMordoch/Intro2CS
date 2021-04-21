##############################################################################
# This file contains 2 function:
# The first function calculates the value of 2 given numbers and
# a given operator, as described in its docstring.
# The second function receives a string containing a mathematical
# expression and splits the string into different parameters
# whom the first function is then called to calculate.
# The function returns the value and prints nothing to the screen.
##############################################################################


def calculate_mathematical_expression(a, b, c):
    """"This function receives three parameters, 2 numbers and
    1 mathematical operator, and returns the calculation result."""
    if c == "+":
        return float(a) + float(b)
    elif c == "-":
        return float(a) - float(b)
    elif c == "*":
        return float(a) * float(b)
    elif c == "/":
        if float(b) == 0:  # can not divide by zero
            return None
        else:
            return float(a) / float(b)
    else:  # if the third parameter is not a defined operator.
        return None


def calculate_from_string(calculate_string):
    """This function receives a string in the form of
    'Number Operator Number' and returns the calculation result.
    The function splits the given strings and then call
    the previously defined function to carry out the calculation"""
    a, c, b = calculate_string.split(" ")  # sorts the parameters
    return calculate_mathematical_expression(a, b, c)
