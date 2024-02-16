#!/usr/bin/python3
"""This mofule defines a class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a class square that inherits from class
    Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing class square
        Args:
            size: size of the square
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves the size of the square"""

        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Passing many arguments using args and kwargs"""

        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if kwargs is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ returns the dictionary representation of a Square"""

        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """Returns the string representation of a square"""

        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                self.id, self.x, self.y, self.height))
