#!/usr/bin/python3

""" Base Geometry """


class BaseGeometry:
    """ A class """

    def area(self):
        """ Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """_summary_

        Args:
            name (_type_): _description_
            value (_type_): _description_

        Raises:
            TypeError: _description_
            ValueError: _description_
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    """ Rectangle """


class Rectangle(BaseGeometry):

    """ A class """

    def __init__(self, width, height):
        """ Init method """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
