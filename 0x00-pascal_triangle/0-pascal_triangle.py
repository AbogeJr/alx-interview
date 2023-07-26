#!/usr/bin/python3
"""
A Pascal's triangle is a triangular array of integers
 constructed with the following formula:
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n
    """
    if n <= 0:
        return []

    res = [[1]]

    for i in range(n - 1):  # n - 1 because we already have the first row
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1):
            row.append(
                temp[j] + temp[j + 1]
            )  # sum of the two numbers above the current cell
        res.append(row)
    return res
