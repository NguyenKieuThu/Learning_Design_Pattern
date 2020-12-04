import abc
import button
import checkbox

class IGuiFactory(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'createButton') and 
                callable(subclass.createButton) and
                hasattr(subclass, 'createCheckbox') and 
                callable(subclass.createCheckbox))

    @abc.abstractmethod
    def createButton(self):
        raise NotImplementedError

    @abc.abstractmethod
    def createCheckbox(self):
        raise NotImplementedError


class WinFactory(IGuiFactory):
    def createButton(self):
        return button.WinButton()
    
    def createCheckbox(self):
        return checkbox.WinCheckbox()

class MacFactory(IGuiFactory):
    def createButton(self):
        return button.MacButton()
    
    def createCheckbox(self):
        return checkbox.MacCheckbox()

