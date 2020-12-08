import abc
from copy import deepcopy


class Shape(abc.ABC):
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    @abc.abstractmethod
    def clone(self):
        pass

    @abc.abstractmethod
    def show_object(self):
        pass

    def change_central(self, x, y):
        self._x = x
        self._y = y


class Rectangle(Shape):
    def __init__(self, x, y, color, width, height):
        Shape.__init__(self, x, y, color)
        self._width = width
        self._height = height

    def clone(self):
        return type(self)(self._x, self._y, self._color, self._width, self._width)

    def show_object(self):
        print("Rectangle with center is ({}, {}), w = {}, h = {} and {} color".format(self._x,
                                                                                      self._y,
                                                                                      self._width,
                                                                                      self._height,
                                                                                      self._color))


class Circle(Shape):
    def __init__(self, x, y, color, radius):
        Shape.__init__(self, x, y, color)
        self._radius = radius

    def clone(self):
        return type(self)(self._x, self._y, self._color, self._radius)

    def show_object(self):
        print("Rectangle with center is ({}, {}), radius = {} and {} color".format(self._x,
                                                                                   self._y,
                                                                                   self._radius,
                                                                                   self._color))




