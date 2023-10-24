#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """A class that creates a square object"""

    def __init__(self, size=0):
        """Initialize a class Square.

        Args:
            size (int): The size of the square
        """
        self.__size = size

    @property
    def size(self):
        """Returns the new updated size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the new size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of a square

        Returns:
            int: A number that represents an area of a square
        """
        return self.__size ** 2
