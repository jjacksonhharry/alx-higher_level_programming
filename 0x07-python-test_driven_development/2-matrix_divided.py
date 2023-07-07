#!/usr/bin/python3
# 2-matrix_divided.py by Harry Muriithi
""" Module that defines the divide function """


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number

    Args:
        matrix (list): The matrix represented as a list
        div (int or float): The number to divide the matrix

    Returns:
        list: A new matrix with all elements divided by div

    Raises:
        TypeError: If matrix is not a list
        ZeroDivisionError: If div is equal to 0
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    divided_matrix = []

    for row in matrix:
        divided_row = []
        for element in row:
            divided_value = round(element / div, 2)
            divided_row.append(divided_value)
        divided_matrix.append(divided_row)

    return divided_matrix
