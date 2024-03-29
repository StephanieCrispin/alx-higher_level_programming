#!/usr/bin/python3
"""A python Function: That saves to a json file"""
import json


def save_to_json_file(my_obj, filename):
    """Saves an file as a json object"""
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
