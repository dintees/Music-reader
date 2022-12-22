from pysine import sine
import json
from Music.Notes import Notes
import threading

class Audio:
    def __init__(self):
        self.samples = {}
        # self.notes = notes
        # self.durations = durations
        self.loadFrequencies()
        self.event = threading.Event()
        self.musicThread = None

    def loadFrequencies(self):
        with open('Music/frequencies.json') as f:
            self.samples = json.load(f)

    def set(self, notes, durations):
        self.notes = notes
        self.durations = durations

    def setEvent(self):
        self.event.set()

    def play(self, playButton, stopButton):
        self.musicThread = threading.Thread(target=self._play, args=(self.event, playButton, stopButton, ))
        self.musicThread.start()

    def stop(self):
        self.setEvent()
        self.musicThread.join()
        self.event.clear()
        # self.event.wait()

    def _play(self, event, playButton, stopButton):
        for i in range(len(self.notes)):
            if event.is_set(): break
            freq = self.samples.get(self.notes[i], None) 
            # if freq is None: raise Exception("The specified sound does not exist")
            if freq is None: freq = 0
            sine(frequency=freq, duration=self.durations[i].value[0]) # tempo * duration beat *** TODO ***
        playButton.setEnabled(True)
        stopButton.setEnabled(False)
            