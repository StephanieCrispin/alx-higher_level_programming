#!/usr/bin/python3
""" Inherits Rectangle class from 9"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class """

    def __init__(self, size):
        """ Init method """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
