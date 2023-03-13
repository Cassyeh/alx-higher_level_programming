#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    c = length
    length = -1
    if my_list is not None:
        for i in range(0, c):
            print("{:d}".format(my_list[length]))
            length = length - 1
