"""
Using when we want to create an object belong to their family or objects have relative together.
References: 
- https://refactoring.guru/design-patterns/abstract-factory
"""

from application import Application
import factory

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