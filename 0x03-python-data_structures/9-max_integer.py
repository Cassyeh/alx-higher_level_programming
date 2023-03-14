#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    big = my_list[0]
    for i in range(0, length):
        if i != length -1 and my_list[i] >= big:
            if my_list[i] >= my_list[i+1]:
                big = my_list[i]
            else:
                big = my_list[i+1]
    return (big)
