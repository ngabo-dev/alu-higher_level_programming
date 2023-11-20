#!/usr/bin/python3
""" no module imported"""


class Rectangle:
    """Represent a rectangle."""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height
    def height(self):
        return self.__height

    @height.detter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Must be an int")
        if value < 0:
            raise ValueError("Must be >= 0")
        self.__height = value
