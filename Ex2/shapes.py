##############################################################################
# We first import the math module in order to use the value of pi,
# We then define 3 functions that calculate the circumference
# of different geometric shapes : circle, rectangle, and equilateral triangle.
# We then define the constant input message the function asks the user.
# We then define a function that asks the user to pick a shape.
# The function then waits for the user to type the necessary
# values for the calculation. The function returns None if no shape
# was chosen.
##############################################################################
import math


def calculate_circle_circumference(r):
    """"This function calculates a circle circumference
    given the radius value of the circle"""
    return math.pi * (float(r) ** 2)


def calculate_rectangle_circumference(a, b):
    """"This function calculates a rectangle circumference
    given the value of the rectangle's 2 sides 'a' and ''b"""
    return float(a) * float(b)


def calculate_triangle_circumference(c):
    """"This function calculates a equilateral triangle
    circumference given the value of the triangle's side"""
    return (math.sqrt(3) / 4) * (float(c)**2)


MESSAGE_INPUT_REQUEST = 'Choose shape (1=circle, 2=rectangle, 3=triangle): '
# The constant message for the input


def shape_area():
    """"This function receives input from the user who decides
    which area he would like to calculate the circumference of.
    The function then proceeds to receive the necessary
    geometric values needed for the calculation and returns the result."""
    print(MESSAGE_INPUT_REQUEST)
    shape = input()
    if shape == "1":  # if user choose circle
        r = input()  # the circle's radius
        return calculate_circle_circumference(float(r))
    elif shape == "2":  # if user choose rectangle
        a = input()  # the rectangle's first side
        b = input()  # the rectangle's second side
        return calculate_rectangle_circumference(float(a), float(b))
    elif shape == "3":   # if user choose triangle
        c = input()  # the triangles side
        return calculate_triangle_circumference(float(c))
    else:  # if the user choose an undefined option
        return None


if __name__ == "__main__":
    print(shape_area())
