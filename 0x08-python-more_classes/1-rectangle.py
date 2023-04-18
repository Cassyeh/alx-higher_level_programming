#!/usr/bin/python3
"""
Module
Please refer to the documentation in the README.md
"""


class Rectangle:
    """
    A class with Private instance attribute: width
    Private instance attribute: height
    and property setters for width and height
    """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            message = "width must be an integer"
            raise TypeError(message)
        if value < 0:
            msg = "width must be >= 0"
            raise ValueError(msg)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            message = "height must be an integer"
            raise TypeError(message)
        if value < 0:
            msg = "height must be >= 0"
            raise ValueError(msg)
        self.__height = value
