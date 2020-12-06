import abc


class IButton(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'paint') and 
                callable(subclass.paint))

    @abc.abstractmethod
    def paint(self):
        raise NotImplementedError


class WinButton(IButton):
    def paint(self):
        print("paint button on Win OS")


class MacButton(IButton):
    def paint(self):
        print("paint button on Mac OS")
