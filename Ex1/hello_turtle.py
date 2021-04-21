##############################################################################
# The following functions draw three flowers by using the turtle module.
# For more information about the turtle module please refer to:
#    https://docs.python.org/3.3/library/turtle.html
# We first define a basic function , and gradually adds three more
# functions who call the previous ones in order to draw a
# three-flowers bed.
##############################################################################

import turtle


def draw_petal():
    """"This function draws a single petal."""
    turtle.circle(100, 90)
    turtle.left(90)
    turtle.circle(100, 90)


def draw_flower():
    """This function draws a single flower:
    four petals and then proceeds to draw a stem."""
    turtle.setheading(0)
    draw_petal()
    turtle.setheading(90)
    draw_petal()
    turtle.setheading(180)
    draw_petal()
    turtle.setheading(270)
    draw_petal()
    turtle.setheading(270)
    turtle.forward(250)


def draw_flower_advance():
    """"This function draws a single flower and also moves the
    turtle head to a new location in order to allow more drawing."""
    draw_flower()
    turtle.right(90)
    turtle.up()
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(250)
    turtle.left(90)
    turtle.down()


def draw_flower_bed():
    """"This function draws three flowers one by one."""
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    draw_flower_advance()
    draw_flower_advance()
    draw_flower_advance()


if __name__ == "__main__":
    draw_flower_bed()
    turtle.done
