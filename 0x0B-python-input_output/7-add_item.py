#!/usr/bin/python3
"""
Module
Please refer to the documentation in the README.md
"""

import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    new_list = load_from_json_file("add_item.json")
    import sys
    for i in range(1, len(sys.argv)):
        new_list.append(sys.argv[i])
    save_to_json_file(new_list, "add_item.json")
except FileNotFoundError:
    new_list = []
    import sys
    for i in range(1, len(sys.argv)):
        new_list.append(sys.argv[i])
    save_to_json_file(new_list, "add_item.json")
