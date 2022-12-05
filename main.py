#!/usr/bin/env python3

"""
Show the mouse position in a small GUI window.

It's a nice tool for pyautogui, for instance.

Start it in the terminal since it prints to the standard output.
"""

import os
import sys
import time

import pyautogui
import pyperclip
from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QMainWindow, QShortcut

import showMainGui

VERSION = "0.1.1"
GITHUB_URL = "https://github.com/jabbalaci/ShowMousePosition"
WAIT = 0.05

stop = False


def clear_screen():
    cmd = "cls" if os.name == "nt" else "clear"
    os.system(cmd)
    print("# tabula rasa")


def wait():
    time.sleep(WAIT)


class MousePosition(QObject):
    pos_ready = pyqtSignal(int, int)

    @pyqtSlot()
    def get_mouse_position(self):  # A slot takes no params
        while not stop:
            x, y = pyautogui.position()
            self.pos_ready.emit(x, y)
            wait()


class Main(QMainWindow, showMainGui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.printButton.clicked.connect(self.print_pos)
        self.sepButton.clicked.connect(self.print_sep)

        # 1 - create Worker and Thread inside the Form
        self.mp = MousePosition()  # no parent!
        # no parent!
        self.thread = QThread()  # type: ignore

        # 2 - Connect Worker`s Signals to Form method slots to post data.
        self.mp.pos_ready.connect(self.on_pos_ready)

        # 3 - Move the Worker object to the Thread object
        self.mp.moveToThread(self.thread)

        # 5 - Connect Thread started signal to Worker operational slot method
        self.thread.started.connect(self.mp.get_mouse_position)

        # * - Thread finished signal will close the app if you want!
        # self.thread.finished.connect(app.exit)

        quit_shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        quit_shortcut.activated.connect(self.close)

        help_shortcut = QShortcut(QKeySequence("Ctrl+H"), self)
        help_shortcut.activated.connect(print_help)

        enter_shortcut = QShortcut(QKeySequence("Ctrl+Return"), self)
        enter_shortcut.activated.connect(self.print_newline)

        print_shortcut = QShortcut(QKeySequence("Ctrl+P"), self)
        print_shortcut.activated.connect(self.print_pos)

        sep_shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        sep_shortcut.activated.connect(self.print_sep)
        sep_shortcut_2 = QShortcut(QKeySequence("Ctrl+-"), self)
        sep_shortcut_2.activated.connect(self.print_sep)

        copy_shortcut = QShortcut(QKeySequence("Ctrl+C"), self)
        copy_shortcut.activated.connect(self.copy_pos_to_clipboard)

        cls_shortcut = QShortcut(QKeySequence("Ctrl+L"), self)
        cls_shortcut.activated.connect(clear_screen)

        # 6 - Start the thread
        self.thread.start()

    def on_pos_ready(self, x: int, y: int) -> None:
        self.x_value.setText(str(x))
        self.y_value.setText(str(y))

    def copy_pos_to_clipboard(self) -> None:
        text = self.get_pos_as_text()
        pyperclip.copy(text)
        print(f"# '{text}' was copied to the clipboard")

    def get_pos_as_text(self) -> str:
        return "{0}, {1}".format(self.x_value.text(), self.y_value.text())

    def print_pos(self) -> None:
        text = self.get_pos_as_text()
        print(text)

    def print_sep(self) -> None:
        print("---")

    def print_newline(self) -> None:
        print()

    def closeEvent(self, event):
        global stop
        stop = True
        self.thread.quit()
        wait()


def print_help():
    text = f"""
Show Mouse Position v{VERSION}, {GITHUB_URL}

Shortcuts:
----------
Ctrl+H                    this help
Ctrl+Q                    quit
Ctrl+P                    print mouse coordinates on stdout
Ctrl+S, Ctrl+-            print separator on stdout
Ctrl+Enter                print a new line on stdout
Ctrl+L                    clear screen
Ctrl+C                    copy mouse coordinates to clipboard
""".strip()
    print(text)


def main():
    print_help()
    App = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(App.exec())


##############################################################################

if __name__ == "__main__":
    main()
