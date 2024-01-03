#!/usr/bin/python3
'''
A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    '''
    Creates a list of lists of integers representing
    Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows for Pascal's triangle.

    Returns:
        list of lists: Pascal's triangle represented as a list of lists.

    Note:
        Returns an empty list if n is not a positive integer.
    '''
    triangle = []

    if not isinstance(n, int) or n <= 0:
        return triangle

    for i in range(n):
        line = []

        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        triangle.append(line)

    return triangle
