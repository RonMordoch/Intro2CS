##############################################################################
# We first import the function we want to test.
# We then define a function to test if the function
# indeed work by comparing it to the values that we are
# supposed to receive by the function.
# We run the function of 5 different sets of values and if the
# result is indeed True, the function prints a success message.
# Else, i.e. at least one or all the functions are giving the wrong
# value, the function print a fail message.
##############################################################################
from largest_and_smallest import largest_and_smallest


def test_largest_and_smallest():
    """"This functions test 5 different iterations
    of the largest_and_smallest function.
    If the results of the function are indeed
    true the function prints a test success message
    and return a True value. Else, the function prints
    a test fail message and returns False."""
    if largest_and_smallest(-3, -2, -1) == (-1, -3):
        if largest_and_smallest(-2, -1, 0) == (0, -2):
            if largest_and_smallest(-1, 0, 1) == (1, -1):
                if largest_and_smallest(0, 1, 2) == (2, 0):
                    if largest_and_smallest(1, 2, 3) == (3, 1):
                        print("Function 4 test success!")
                    return True
                else:
                    print("Function 4 test fail")
                    return False
            else:
                print("Function 4 test fail!")
                return False
        else:
            print("Function 4 test fail!")
            return False
    else:
        print("Function 4 test fail!")
        return False


if __name__ == "__main__":
    test_largest_and_smallest()
