from PyQt6.QtWidgets import QMainWindow, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QFileDialog
from GUI.Button import Button
from GUI.Image import Image
from GUI.Color import Color #dev
from Music.Audio import Audio
from Music.Notes import Notes
import threading

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Music reader")
        self.resize(1000, 600)
        self.windowWidth = self.frameGeometry().width()
        self.windowHeight = self.frameGeometry().height()
        self.readImage = Image('', int(1000 * .42), self.windowHeight)
        self.p = Audio()

        # print(self.frameGeometry().width())
        # self.setGeometry(100, 100, 600, 400)

        # self.setCentralWidget(button)
        layout = QHBoxLayout()

        layout.addWidget(self.readImage, 40)
        layout.addWidget(Color('gray'), 40)

        menuLayout = QVBoxLayout()
        btn = Button("Load image", self.loadImage)
        menuLayout.addWidget(btn)

        self.algorithmButton = Button("Make an ALG!", self.tempAlg)
        self.algorithmButton.setEnabled(False)
        menuLayout.addWidget(self.algorithmButton)

        self.playMusicButton = Button("Play", self.playMusic)
        self.playMusicButton.setEnabled(False)
        menuLayout.addWidget(self.playMusicButton)

        self.stopMusicButton = Button("Stop", self.stopMusic)
        self.stopMusicButton.setEnabled(False)
        menuLayout.addWidget(self.stopMusicButton)

        # *** TODO ***
        # self.rate = QLineEdit()
        # self.rate.setPlaceholderText("Rate [120]")
        # # self.rate.setText("120")
        # self.rate.setInputMask("099")
        # menuLayout.addWidget(self.rate)


        btn = Button("Close application", self.close)
        menuLayout.addWidget(btn)
        menuLayout.addStretch()

        layout.addLayout(menuLayout)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()

    def tempAlg(self):
        print("Im doing something with photo and after that...")
        self.playMusicButton.setEnabled(True)

    def loadImage(self):
        fname = QFileDialog.getOpenFileName(self, "Open file", "${HOME}", "PNG Files (*.png);; JPG Files(*.jpg)")
        print(f'Loading image {fname[0]}')
        self.readImage.setImage(fname[0], 500)
        self.algorithmButton.setEnabled(True) # after reading notes

    def playMusic(self):
        # print("I'm playing the music")
        
        self.playMusicButton.setEnabled(False)
        self.stopMusicButton.setEnabled(True)
        notes = ["E4", "E4", "E4", "E4", "E4", "E4", "-", "E4", "G4", "C4", "D4", "E4"]
        durations = [Notes.QUARTER_NOTE, Notes.QUARTER_NOTE, Notes.HALF_NOTE, Notes.QUARTER_NOTE, Notes.QUARTER_NOTE, Notes.HALF_NOTE, Notes.HALF_NOTE, Notes.QUARTER_NOTE, Notes.QUARTER_NOTE, Notes.QUARTER_NOTE, Notes.QUARTER_NOTE, Notes.WHOLE_NOTE]
        self.p.set(notes, durations)
        self.p.play(self.playMusicButton, self.stopMusicButton)

    def stopMusic(self):
        self.p.stop()
        self.playMusicButton.setEnabled(True)
        self.stopMusicButton.setEnabled(False)
