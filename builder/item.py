import abc
import packing


class IItem(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def name(self):
        pass

    @abc.abstractmethod
    def packing(self):
        pass

    @abc.abstractmethod
    def price(self):
        pass




