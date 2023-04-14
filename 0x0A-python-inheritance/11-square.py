#!/usr/bin/python3
"""
Module
Please refer to the documentation in the README.md
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that inherits from Rectangle
    """
    def __init__(self, size):
        """
        Instantiation with size
        """
        self.__width = size
        self.__height = size
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """
        A function that calculates area
        """
        area = self.__width * self.__height
        return area

    def __str__(self):
        """
        Prints the class
        """
        msg = "[Square] {}/{}".format(self.__width, self.__height)
        return msg
