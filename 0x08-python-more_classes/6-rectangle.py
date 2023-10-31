#!/usr/bin/python3

"""Define a rectangle"""


class Rectangle:
    """Creates an instance of a rectangle object"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Creates an instance of a rectangle object"""
        """Initializes a Rectangle

        Args
        width (int): The width of a rectangle
        width (int): The width of a rectangle """
        self.__height = height
        self.__width = width
        type(self).number_of_instances += 1

    @property
    def height(self):
        """Return height"""
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
    """Return width"""
    def width(self):
        """Creates an instance of a rectangle object"""
        return self.__width

    @width.setter
    """width"""
    def width(self, value):
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
        """Return the printable representation of the Rectangle.
        """
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
        """print message for deletion"""

        print("Bye rectangle...")
        type(self).number_of_instances -= 1
