#!/usr/bin/python3
"""
Module
Please refer to the documentation in the README.md
"""

import json


def load_from_json_file(filename):
    """
    function that creates an Object from a “JSON file”
    """
    with open(filename, 'r') as json_file:
        return json.load(json_file)
