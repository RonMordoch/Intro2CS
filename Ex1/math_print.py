##############################################################################
# The following code uses the math module for mathematical calculations.
# The code defines six different mathematical functions.
# For more information about the math module, please refer to:
#    https://docs.python.org/3/library/math.html
##############################################################################

import math


# Two positive quantities are in the golden ratio if
# their ratio equals to the ratio of their sum to the
# larger of the two quantities. For more information
# refer to: https://en.wikipedia.org/wiki/Golden_ratio

def golden_ratio():
    """"The following function prints the algebraic value
     of the golden ratio."""
    print((1 + math.sqrt(5)) / 2)


def six_cubed():
    """"The following function prints the number six multiplied
    by six , three times."""
    print(6 ** 3)


def hypotenuse():
    """"The following function prints the length of the hypotenuse
    in a right angled triangle wherein 'a' and 'b' are the legs, using
    the Pythagorean triple: a*2 + b*2 = c*2."""
    a = 3
    b = 5
    c = math.sqrt(a ** 2 + b ** 2)
    print(c)


def pi():
    """""The following function prints the value of the irrational
    number pi, also called 'Archimedes' constant'."""
    print(math.pi)


def e():
    """"The following function prints the irrational number e."""
    print(math.e)


def triangular_area():
    """"This function prints the area of ten isosceles right-angled
    triangles wherein the legs equal one to ten."""
    print(1 * 1 / 2, 2 * 2 / 2, 3 * 3 / 2, 4 * 4 / 2, 5 * 5 / 2,
          6 * 6 / 2, 7 * 7 / 2, 8 * 8 / 2, 9 * 9 / 2, 10 * 10 / 2)


if __name__ == "__main__":
    golden_ratio()
    six_cubed()
    hypotenuse()
    pi()
    e()
    triangular_area()
