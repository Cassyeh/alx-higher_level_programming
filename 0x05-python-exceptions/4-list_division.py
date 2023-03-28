#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(0, list_length):
        try:
            result.append(my_list_1[i] / my_list_2[i])
        except (ZeroDivisionError, TypeError, ValueError, IndexError):
            result.append(0)
        finally:
            if i < len(my_list_1):
                if type(my_list_1[i]) != int and type(my_list_1[i]) != float:
                    print("wrong type")
            if i < len(my_list_2):
                if type(my_list_2[i]) != int and type(my_list_2[i]) != float:
                    print("wrong type")
            if i < len(my_list_2):
                if my_list_2[i] == 0:
                    print("division by 0")
    if len(my_list_1) < list_length or len(my_list_2) < list_length:
        print("out of range")
    return(result)
