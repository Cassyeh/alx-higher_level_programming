#!/usr/bin/python3
"""
100-matrix_mul module that contains function for matrix
"""


def matrix_mul(m_a, m_b):
    """
    Matrix multiplication function

    Args:
        m_a: matrix 1
        m_b: matrix 2

    Returns:
        new matrix equal to (m_a * m_b)

    Raises:
        TypeError: Raises an exception for input of wrong type
        ValueError: Raises an exception
    """
    for key, matrix in {"m_a": m_a, "m_b": m_b}.items():
        if type(matrix) != list:
            raise TypeError("{} must be a list".format(key))
    for key, matrix in {"m_a": m_a, "m_b": m_b}.items():
        for row in matrix:
            if type(row) != list:
                raise TypeError("{} must be a list of lists".format(key))
    for key, matrix in {"m_a":  m_a, "m_b": m_b}.items():
        if len(matrix) == 0:
            raise ValueError("{} can't be empty".format(key))
    # to run this line, that means len of m_a and m_2 > 0
    for key, matrix in {"m_a": m_a, "m_b": m_b}.items():
        for row in matrix:
            if len(row) == 0:
                raise ValueError("{} can't be empty".format(key))
    for key, matrix in {"m_a": m_a, "m_b": m_b}.items():
        type_matr = [int, float]
        err_msg = "should contain only integers or floats"
        for row in matrix:
            for value in row:
                if type(value) not in type_matr:
                    raise TypeError("{} {}".format(key, err_msg))
    for key, matrix in {"m_a": m_a, "m_b": m_b}.items():
        length = []
        for row in matrix:
            length.append(len(row))
            if len(length) > 1:
                set_row_length = set(length)
                if len(set_row_length) != 1:
                    er_msg = "must be of the same size"
                    raise TypeError("each row of {} {}".format(key, er_msg))
    # we are raising an error in case the user disobeyed the
    # matrix multiplication rule where number of columns of matrix a is equal
    # to number of rows of matrix b i.e len(m_a[0]) == len(m_b)
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result_matrix = []
    # instantiating the matrix to produce matrix of
    # len(m_a) rows and len(m_b[0]) columns
    for rows in range(len(m_a)):
        new_row = []
        for columns in range(len(m_b[0])):
            new_row.append(0)
        result_matrix.append(new_row)
    new_row = []
    count_rowa = 0
    for i in range(len(result_matrix)):
        mul_list = []
        count_rowb = 0
        for i in range(len(result_matrix[0])):
            count_columna = 0
            mul = 0
            count_columnb = 0
            for row_b in m_b:
                try:
                    mul = mul + (m_a[count_rowa][count_columna]
                                 * m_b[count_columnb][count_rowb])
                except Exception:
                    raise ValueError("m_a and m_b can't be multiplied")
                count_columnb = count_columnb + 1
                count_columna = count_columna + 1
            mul_list.append(mul)
            count_rowb = count_rowb + 1
        count_rowa = count_rowa + 1
        new_row.append(mul_list)
    return new_row
