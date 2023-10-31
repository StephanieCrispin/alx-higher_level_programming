#!/usr/bin/python3

"""Define a rectangle"""


class Rectangle:
    """Creates an instance of a rectangle object"""

    def __init__(self, width=0, height=0):
        """Creates an instance of a rectangle object"""
        """Initializes a Rectangle

        Args
        width (int): The width of a rectangle
        width (int): The width of a rectangle """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """Returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width"""
        if not isinstance(value, int):
            raise TypeError(" width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
