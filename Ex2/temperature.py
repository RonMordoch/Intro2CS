##############################################################################
# The function defines if it is summer yet by checking if a given
# temperature is larger than at least 2 of 3 given temperatures
# using the > < operators.
# The function returns the value and prints nothing to the screen.
##############################################################################

def is_it_summer_yet(a, b, c, d):
    """"This function receives 4 parameters:
    a = a given threshold temperature
    b, c, d = given temperatures from the last 3 days
    The function then returns True if the threshold temperature
    is larger than at least 2 of the temperatures from the
    last 3 days. Else, it returns false."""
    if b > a < c:
        return True
    elif b > a < d:
        return True
    elif c > a < d:
        return True
    else:
        return False
