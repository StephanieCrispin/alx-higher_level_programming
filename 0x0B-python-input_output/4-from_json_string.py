#!/usr/bin/python3
"""A python Function: returns an object"""
import json


def from_json_string(my_str):
    """Returns an object from a JSON string"""
    return json.loads(my_str)
