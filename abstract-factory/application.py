import factory

class Application:
    def __init__(self, object_factory):
      self.__factory = object_factory

    def createUI(self):
        self.__button = self.__factory.createButton()
        self.__checkbox = self.__factory.createCheckbox()

    def paint(self):
        self.__button.paint()
        self.__checkbox.paint()

if __name__=='__main__':
    # Create UI with Win OS
    win_factory = factory.WinFactory()
    app_win = Application(win_factory)
    print("="*20)
    print("===UI with Win Os===")
    app_win.createUI()
    app_win.paint()

    # Create UI with Mac OS
    mac_factory = factory.MacFactory()
    app_mac = Application(mac_factory)
    print("="*20)
    print("===UI with Mac Os===")
    app_mac.createUI()
    app_mac.paint()