#!/usr/bin/python3
"""
9-student module that contains a class Student
"""


class Student:
    """
    class that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiation of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        dictionary representation
        """
        return self.__dict__
