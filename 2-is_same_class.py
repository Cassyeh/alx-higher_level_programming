#!/usr/bin/python3
"""
Module 0-square
Defines class Square
"""


def is_same_class(obj, a_class):
  """
  An empty class that defines a square
  """
    result = isinstance(obj, a_class)
    c = type(obj)
    if c == a_class:
        d = True
    else:
        d = False
    if result == d:
        return result
