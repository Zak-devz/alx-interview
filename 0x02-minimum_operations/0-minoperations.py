#!/usr/bin/python3
""" Minimum Operations
    """


def minOperations(n):
    """ Minimum Operations needed to get n H characters
        Args:
            n: input value
        Return: the sum of the operations """
    if n < 2:
        return 0

    factor_list = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                factor_list.append(i)

    return sum(factor_list)
