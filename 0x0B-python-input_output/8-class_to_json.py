#!/usr/bin/python3
"""
8-class_to_json module for dictionary description
"""


def class_to_json(obj):
    """
    Dictionary representation of object instance function

    Args:
        obj: object that is instance of a class

    Returns:
        dictionary of object
    """
    return obj.__dict__
