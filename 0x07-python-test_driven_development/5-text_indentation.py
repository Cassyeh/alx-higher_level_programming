#!/usr/bin/python3
"""
Module
Please refer to the documentation in the README.md
"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    a = 0
    for i in text:
        if i == '.' or i == '?' or i == ':':
            print("{:s}\n".format(i))
            a = a + 1
            continue
        if text[a - 1] == '.' or text[a - 1] == '?' or text[a - 1] == ':':
            if i == ' ':
                a = a + 1
                continue
        print("{:s}".format(i), end="")
        a = a + 1
