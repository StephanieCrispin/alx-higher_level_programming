#!/usr/bin/python3
"""My rectangle class"""
from models.base import Base


class Rectangle(Base):
    """A rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """

        Initializes a new rectangle instance

        Args:
            width (int): Defines the width of the new Rectangle.
            height (int): Defines the height of the new Rectangle.
            x (int): Defines the x coordinate of the new Rectangle.
            y (int): Defines the y coordinate of the new Rectangle.
            id (int): Defines the identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        if x < 0:
            raise ValueError("x must be >= 0")
        self.x = x
        if y < 0:
            raise ValueError("y must be >= 0")
        self.y = y

    @property
    def width(self):
        """Gets the width of a square"""
        return self.__width

    @width.setter
    def set_width(self, width):
        """Sets the width of a square"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Defines the height of a square"""
        return self.__height

    @height.setter
    def set_height(self, height):
        """sets the new size of a hieght"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """area of a rectangle"""
        return self.__height * self.__width

    def display(self):
        """Displays a representation of the square with # symbol"""
        if self.__width or self.__height == 0:
            print("")
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """Returns print() and str() representations of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def to_dictionary(self):
        """Returns a dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def update(self, *args, **kwargs):
        """Updates the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument stands for id attribute
                - 2nd argument stands for width attribute
                - 3rd argument stands for height attribute
                - 4th argument stands for x attribute
                - 5th argument stands for y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
