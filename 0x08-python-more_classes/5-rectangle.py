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
    """Return height"""
    def height(self):
        return self.__height

    @height.setter
    """height"""
    def height(self, value):
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

    def area(self):
        """Returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.__width + self.__height)

    def __str__(self) -> str:
        """Returns a string rep"""
        if self.__width == 0 or self.__height == 0:
            return (" ")

        empty = []

        for i in range(self.__height):
            [empty.append("#") for x in range(self.__width)]
            if i != self.__height - 1:
                empty.append("\n")
        return ("".join(empty))

    def __repr__(self) -> str:
        """Return a string rep of a rectangle"""
        rectangle_rep = "Rectangle(" + str(self.__width)
        rectangle_rep += ", " + str(self.__height) + ")"
        return rectangle_rep

    def __del__(self) -> str:
        """prints bye when an instance is deleted"""
        print("Bye rectangle...")
