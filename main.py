from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt6.QtCore import QSize, Qt

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Music reader")

        button = QPushButton("Hello world! Click me to close this window.")
        self.setFixedSize(QSize(800, 600))
        button.pressed.connect(self.close)

        self.setCentralWidget(button)
        self.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
