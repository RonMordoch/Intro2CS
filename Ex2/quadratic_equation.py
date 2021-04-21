##############################################################################
# The general formula for solving a quadratic equation is:
#   ax**2 + bx + c = 0.
# The discriminant is defined as the square root of:
#   b**2 - 4 * a * c
# For more information on quadratic equations please refer to:
#   https://en.wikipedia.org/wiki/Quadratic_formula
# The second function receives input from user and prints the
# results.
##############################################################################
import math


def quadratic_equation(a, b, c):
    """"This function receives three parameters
    a, b and c, the three coefficients of the quadratic
    equation, and returns the result using the quadratic formula"""
    d = float(b) ** 2 - 4 * float(a) * float(c)  # discriminant
    if d > 0:  # positive number inside the square root yields 2 numbers
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2
    elif d == 0:  # square root of zero is zero which is indifferent to sum
        x1 = (-b / (2*a))
        x2 = None
        return x1, x2
    else:  # discriminant<0, square root of a negative number is not defined
        x1 = None
        x2 = None
        return x1, x2


def quadratic_equation_user_input():
    """"This function receives the three coefficients as
    input from the user, calculates the equation result
    using the quadratic_equation defined previously, and
    then proceeds to print the results."""
    a, b, c = input("Insert coefficients a, b, and c: ").split(" ")
    # splits the input into separate numbers for the calculation
    x1, x2 = quadratic_equation(float(a), float(b), float(c))
    d = float(b) ** 2 - 4 * float(a) * float(c)  # discriminant
    if d > 0:  # positive number inside the square root yields 2 numbers
        print("The equation has 2 solutions:", x1, "and", x2)
    elif d == 0:  # square root of zero is zero which is indifferent to sum
        print("The equation has 1 solution:", x1)
    else:  # discriminant<0, square root of a negative number is not defined
        print("The equation has no solutions")
