#!/usr/bin/env python3
"""Contain add_arrays function"""


def matrix_shape(matrix):
    """calculates the shape of a matrix"""
    if matrix:
        size = [len(matrix)]
        return matrix_shape_recursion(matrix, size)
    else:
        return 0


def matrix_shape_recursion(matrix, size):
    """recursion to calculates the shape of a matrix"""
    if type(matrix) == int:
        return size
    else:
        for element in matrix:
            new = element
            """print("current matrix {}".format(element))"""
            if type(element) != int:
                current_len = len(element)
                size.append(current_len)
            break
        return (matrix_shape_recursion(new, size))


def add_arrays(arr1, arr2):
    """adds two arrays element-wise"""

    shape1 = matrix_shape(arr1)
    shape2 = matrix_shape(arr2)


    if shape1[0] != shape2[0]:
        return None
    else:
        new_array = []

        for i in range(shape1[0]):
            new_array.append(arr1[i] + arr2[i])
        return new_array
