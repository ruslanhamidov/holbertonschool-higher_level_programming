#!/usr/bin/python3
"""
Module with Square class
"""


class Square:
    """
    Square class that contains private size attribute
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initilaize method
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        elif not isinstance(value, tuple) or tuple[0] < 0 or tuple[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

    @property
    def position(self):
        """
        position attribute getter
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        position attribute setter 
        """
        if not isinstance(value, tuple) or tuple[0] < 0 or tuple[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @property
    def size(self):
        """
        size getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size setter
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        returns current square area
        """
        return self.__size * self.__size

    def my_print(self):
        """
        prints square with # character
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print('#', end='')
                print()
