#!/usr/bin/python3
"""Defines a function; string to JSON"""
import json


def to_json_string(my_obj):
    """A python that returns an object as a Json"""
    return json.dumps(my_obj)
