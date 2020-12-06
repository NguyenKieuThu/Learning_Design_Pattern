import abc


class IButton(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'render') and
                callable(subclass.render) and
                hasattr(subclass, 'on_click') and
                callable(subclass.on_click))

    @abc.abstractmethod
    def render(self):
        raise NotImplementedError

    @abc.abstractmethod
    def on_click(self):
        raise NotImplementedError


class WinButton(IButton):
    def render(self):
        print("Render button on Win OS")

    def on_click(self):
        print("Onclick button on Win OS")


class HTMLButton(IButton):
    def render(self):
        print("Render button on HTML")

    def on_click(self):
        print("Onclick button on HTML")