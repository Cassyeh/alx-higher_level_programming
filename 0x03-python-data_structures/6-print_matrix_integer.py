#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    length = len(matrix)
    for i in range(0, length):
        lengtha = len(matrix[i])
        a = matrix[i]
        for j in range(0, lengtha):
            if j != lengtha - 1:
                print("{}".format(a[j]), end=" ")
            else:
                print("{}".format(a[j]), end = "")
        print()
