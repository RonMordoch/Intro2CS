from ex3 import maximum  # import the function we are testing


def check_maximum():
    """"This function checks the maximum function over 4 lists.
    The lists are edge cases, meant to test the function over different
    circumstances.
    The function prints a message for each test telling the user
    whether the test succeeded or failed. If and only if all 4 tests passed,
    the function will return True. Else it will return false."""
    a = []  # an empty list
    b = [0, 0, 0, 0]  # list containing only zeros
    c = [0, 1, 0, 1]  # list containing zero and positives
    d = [1, 3, 4, 2]  # list containing different positives
    if maximum(a) is None:
        print("Test 0 success!")
        if maximum(b) == 0:
            print("Test 1 success!")
            if maximum(c) == 1:
                print("Test 2 success!")
                if maximum(d) == 4:
                    print("Test 3 success!")
                    return True
                else:
                    print("Test 3 fail!")
                    return False
            else:
                print("Test 2 fail!")
                return False
        else:
            print("Test 1 fail!")
            return False
    else:
        print("Test 0 fail!")
        return False


if __name__ == "__main__":
    check_maximum()