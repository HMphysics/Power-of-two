def power_of_two(x):

    # We will define a list with each possible result of raising 2 to each number from 0 to 100.
    # We could use more numbers but I consider the number 100 like a very big number.
    number_exp_two = [
        2**i for i in range(101)]

    # If the the number is bellow 0 or it is not in our list, the function will return 'False'.
    # In the other hand it will return 'True'.
    if x < 0:

        return False

    elif x in number_exp_two:

        return True

    else:

        return False
