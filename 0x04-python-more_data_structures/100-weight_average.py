#!/usr/bin/python3
def weight_average(my_list=[]):
    length = len(my_list)
    total = 0
    nums = 0
    for i in range(0, length):
        a = my_list[i]
        mul = 1
        for j in range(0, len(a)):
            mul = mul * a[j]
        total = total + mul
        nums = nums + a[-1]
    avg = total/nums
    return (avg)
