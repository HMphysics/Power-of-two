def power_of_two(num):
    #We will transform the number in a binary number and we will coount how many 'ones' exist.
    #If there is only one 'one' mean the number is a power of two.
    return bin(num).count('1') == 1
