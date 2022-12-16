from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QFileDialog
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPalette, QColor, QPixmap

import sys

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class Image(QWidget):
    def  __init__(self, src, width, height):
        super(Image, self).__init__()
        pixmap = QPixmap(src)
        self.label = QLabel(self)
        self.label.setMargin(0)
        # self.label.setScaledContents(True) # do skalowania
        self.label.resize(width, height)
        # self.label.setStyleSheet("background-color: blue")
        self.label.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)

        if src != '': self.label.setPixmap(pixmap)#.scaled(width, 400, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

    def setImage(self, src, width):
        self.label.clear()
        pixmap = QPixmap(src)
        self.label.setPixmap(pixmap.scaledToWidth(width - 60, mode=Qt.TransformationMode.SmoothTransformation))

    def getLabel(self):
        return self.label


class Button(QPushButton):
    def __init__(self, text, action):
        super().__init__(text)
        self.text = text
        self.action = action
        self.clicked.connect(action)

    def exec(self):
        self.action()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Music reader")
        self.resize(1000, 600)
        self.windowWidth = self.frameGeometry().width()
        self.windowHeight = self.frameGeometry().height()
        self.readImage = Image('', int(1000 * .42), self.windowHeight)

        # print(self.frameGeometry().width())
        # self.setGeometry(100, 100, 600, 400)

        # button = QPushButton("Hello world! Click me to close this window.")
        # self.setFixedSize(QSize(800, 600))
        # button.pressed.connect(self.close)

        # self.setCentralWidget(button)
        layout = QHBoxLayout()

        layout.addWidget(self.readImage, 40)
        layout.addWidget(Color('gray'), 40)

        menuLayout = QVBoxLayout()
        btn = Button("Load image", self.loadImage)
        menuLayout.addWidget(btn)

        btn = Button("Play music", self.playMusic)
        btn.setEnabled(False)
        menuLayout.addWidget(btn)

        btn = Button("Close application", self.close)
        menuLayout.addWidget(btn)
        menuLayout.addStretch()


        layout.addLayout(menuLayout)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()

    def loadImage(self):
        fname = QFileDialog.getOpenFileName(self, "Open file", "${HOME}", "PNG Files (*.png);; JPG Files(*.jpg)")
        print(f'Loading image {fname[0]}')
        self.readImage.setImage(fname[0], 500)

    def playMusic(self):
        print("I'm playing the music")
        # ### TODO ###


app = QApplication(sys.argv)
w = MainWindow()
# w.show()
app.exec()
