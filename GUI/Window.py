from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QFileDialog
from GUI.Button import Button
from GUI.Image import Image
from GUI.Color import Color #dev
from Music.Audio import Audio
from Music.Notes import Notes

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

        # self.setCentralWidget(button)
        layout = QHBoxLayout()

        layout.addWidget(self.readImage, 40)
        layout.addWidget(Color('gray'), 40)

        menuLayout = QVBoxLayout()
        btn = Button("Load image", self.loadImage)
        menuLayout.addWidget(btn)

        self.playMusicButton = Button("Play music", self.playMusic)
        self.playMusicButton.setEnabled(False)
        menuLayout.addWidget(self.playMusicButton)

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
        self.playMusicButton.setEnabled(True) #testing

    def playMusic(self):
        print("I'm playing the music")
        # self.playMusicButton.setText("Stop") # changes after the music ends :(
        self.p = Audio()
        notes = ["E4", "E4", "E4", "E4", "E4", "E4", "E4", "G4", "C4", "D4", "E4"]
        durations = [Notes.QUARTER_NOTE, Notes.QUARTER_NOTE, Notes.HALF_NOTE, Notes.QUARTER_NOTE, Notes.QUARTER_NOTE, Notes.HALF_NOTE, Notes.QUARTER_NOTE, Notes.QUARTER_NOTE, Notes.QUARTER_NOTE, Notes.QUARTER_NOTE, Notes.WHOLE_NOTE]

        for i in range(len(notes)):
            self.p.play(notes[i], durations[i])