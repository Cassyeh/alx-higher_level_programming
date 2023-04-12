#!/usr/bin/python3
"""
Module 0-square
Defines class Square
"""


def is_same_class(obj, a_class):
  """
  A simple function to check same class
  """
    result = isinstance(obj, a_class)
    c = type(obj)
    if c == a_class:
        d = True
    else:
        d = False
    if result == d:
        return result
