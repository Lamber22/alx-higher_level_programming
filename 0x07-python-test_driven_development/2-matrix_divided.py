#!/usr/bin/python3


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        int(matrix) - The lists of matrix to divide
        int(div) - The divisor of the matrix

    Raises:
        TypeError: if the matrix is not int or float
        TypeError: if the size of the matrix are not the same
        TypeError: if div is not a number
        ZeroDivisionError: div cannot be zero

    Returns:
        A new matrix
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
