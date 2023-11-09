#!/usr/bin/python3
"""
11-student module that contains a class Student
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

    def to_json(self, attrs=None):
        """
        dictionary representation
        """
        if type(attrs) == list:
            for val in attrs:
                if type(val) != str:
                    return self.__dict__
            new_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict.update({key: value})
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        """
        attribute update
        """
        for key, value in json.items():
            setattr(self, key, value)
