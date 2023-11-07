#!/usr/bin/python3
""" Inherits Base Geometry class from 7"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """ A class """

    def __init__(self, width, height):
        """ Init method """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
