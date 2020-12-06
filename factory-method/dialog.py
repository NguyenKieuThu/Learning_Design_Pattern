import button
import abc


class Dialog(abc.ABC):
    @abc.abstractmethod
    def create_button(self):
        pass

    def render(self):
        button_instance = self.create_button()
        button_instance.on_click()
        button_instance.render()


class WindowsDialog(Dialog):
    def create_button(self):
        return button.WinButton()


class WebDialog(Dialog):
    def create_button(self):
        return button.HTMLButton()


