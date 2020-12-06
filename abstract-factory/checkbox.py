import abc


class ICheckbox(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'paint') and 
                callable(subclass.paint))
    
    @abc.abstractmethod
    def paint(self):
        raise NotImplementedError


class WinCheckbox(ICheckbox):
    def paint(self):
        print("paint checkbox on Win OS")


class MacCheckbox(ICheckbox):
    def paint(self):
        print("paint checkbox on Mac OS")