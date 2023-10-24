#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """A class that creates a square object"""

    def __init__(self, size=0):
        """Initialize a class Square.

        Args:
            size (int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of a square

        Returns:
            int: A number that represents an area of a square
        """
        return self.__size ** 2
