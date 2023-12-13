#!/usr/bin/python3


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix (list): Matrix to be divided.
        div (int or float): Number to divide the matrix by.

    Returns:
        list: New matrix with divided elements.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If matrix is not a rectangle.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is 0.

    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    length = len(matrix[0])
    for row in matrix:
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    return new_matrix
