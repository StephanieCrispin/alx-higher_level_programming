#!/usr/bin/python3
"""A python function: That loads from json file"""
import json


def load_from_json_file(filename):
    """imports an object from a json file"""
    with open(filename, "r", encoding="utf-8") as f:
        x = json.load(f)
        return (x)
