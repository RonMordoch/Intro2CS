def input_list():
    """"This function receives input from the user, converts it to string
     and insert it into a list containing all the inputs received. If the
     user inserts an empty input, the function ends and returns the list."""
    string_list = []
    while True:
        string_from_user = input()
        if string_from_user == "":  # if user typed an empty string
            break
        else:  # the loop checks every time if the user typed an empty string.
            string_list.append(string_from_user)
    return string_list


def concat_list(str_list):
    """"This function receives a list of strings and returns the
    concatenation of the list's items in a single string, each word
     separated by a single space excluding the last one."""
    new_string = ""  # the newly created string
    for item in str_list:
        new_string += item + " "  # adds each item in the list to the string
    new_string = new_string[:-1]  # excluding the last space
    return new_string


def maximum(num_list):
    """"This function receives a list containing nubmers, and returns
    the largest number out of the list. If an empty list is given as a
    parameter, the function returns None."""
    if len(num_list) == 0:  # if the function is given an empty list
        return None
    else:
        max_num = num_list[0]  # we set the first number to be the maximum
        for i in num_list:  # the function then iterates over all the items
            if i > max_num:  # if a larger number is found it is set to be
                max_num = i  # the maximum num.
        return max_num


def cyclic(lst1, lst2):
    """"This function receives 2 lists and return True if one list is a
    cyclic permutation of the other. Else it returns False."""
    if lst1 == [] and lst2 == []:  # empty list are cyclic permutations
        return True
    if len(lst1) == len(lst2):  # permutation possible only in equal lengths
        for i in range(len(lst1)):  # for each index in the range of length
            for j in range(len(lst1)):  # for each index in range of length
                if lst1[j] != lst2[(j + i) % len(lst1)]:
                    break  # not a cyclic permutation
            else:  # if the indexes are indeed moved in a cyclic permutations
                return True
        else:
            return False  # not a cyclic permutation
    else:
        return False  # if the list or of different lengths


def seven_boom(n):
    """This function receives a number and created a list containing
    all the natural numbers from 1 to the given number.
    If a number if divisible by 7 or contains the digit 7, the function
    replaces its value with the string 'boom'. The function returns a new
    list with the changed applied."""
    num_list = []  # newly created list
    for num in range(1, n+1):  # all the natural numbers from 1 to n
        string = str(num)
        if num % 7 == 0:  # if number is divisible by 7
            num_list.append("boom")
        elif "7" in string:  # if number contains the digit 7
            num_list.append("boom")
        else:  # if number does not meet any of the two requirements
            num_list.append(str(num))
    return num_list


def histogram(n, num_list):
    """""This function receives an integer and a list containing numbers.
    The function creates an empty list with length of 'n', and creates
    a histogram of the given list, which is a new list where the amount of
     times a number has appeared on the given list is counted and displayed
     at the corresponding index of the new list."""
    lst = [0] * n  # create a list of zeros in size of n
    for i in range(len(num_list)):  # input for the loop
        var = num_list[i]  # variable equals the index number of the list
        lst[var] = lst[var] + 1  # add 1 every time a variable is counted
    return lst  # returns the histogram


def prime_factors(n):
    """"This function receives an integer that is larger or equal to one.
    The function then breaks down the number into prime numbers and
    keeps dividing until the smallest prime number is reached."""
    num = 2  # our range of divisors starts at 2
    factors_list = []  # newly created list of prime factors
    while num * num <= n:  # while the products are smaller than the number
                            # keeps going til the smallest product is reached
        # if n % num == 0 we know that num divides n without any remainder,
        # and we floor divide n by num to receive a new value of n to keep
        # dividing. Num starts from 2 and if it divides without modulo, it is
        # a prime number.
        if n % num == 0:
            n = n // num  # create a new value of n to keep dividing
            factors_list.append(num)
    # append the first and smallest prime so the list is from min to max
        else:
                # if num is not a prime factor,
                # keep adding 1 until a prime factor is found
            num = num + 1
    if n > 1:
        # if the while loop does not find any prime factors, or it reached
        # the smallest prime factors possible, then in each of the two cases
        # we are left with a prime number. If it is larger than 1,
        # the number will be inserted into the list.
        factors_list.append(n)
    else:  # n = 1 according to parameter assumptions, return an empty list
        return []
    return factors_list


def cartesian(lst1, lst2):
    """This function receives two lists and returns a new list
    containing the cartesian product.
    The first element in every list is an item from the ls1, and the
    second element is an item from lst2.
    for more information please refer to:
    https://en.wikipedia.org/wiki/Cartesian_product"""
    cartesian_list = []  # newly created list
    for i in lst1:  # for each element in the first list
        for j in lst2:  # for each element in the second list
            cartesian_list.append([i, j])  # insert the cartesian product
    return cartesian_list


def pairs(num_list, n):
    """This function receives a list of numbers and an integer 'n',
    and returns a list of all the pairs of numbers from the given list
    that their sums equal to 'n'."""
    pairs_list = []  # newly created list
    for num1 in num_list:
        for num2 in num_list:
            if num1 + num2 == n:  # if their sum is n
                if num1 < num2:  # avoid printing reverse duplicates
                    pairs_list.append([num1, num2])  # pair inserted to list
    return pairs_list
