"""
ref: https://refactoring.guru/design-patterns/factory-method
"""
import dialog

if __name__=='__main__':
    print("===Win===")
    win_dialog = dialog.WindowsDialog()
    win_dialog.render()
    print("===Web===")
    win_dialog = dialog.WebDialog()
    win_dialog.render()