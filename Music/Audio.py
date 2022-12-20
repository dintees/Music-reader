from pysine import sine
import json
from Music.Notes import Notes

class Audio:
    def __init__(self):
        self.samples = {}
        self.loadFrequencies()

    def loadFrequencies(self):
        with open('Music/frequencies.json') as f:
            self.samples = json.load(f)

    def play(self, sound, notename=Notes.QUARTER_NOTE):
        freq = self.samples.get(sound, None) 
        if freq is None: raise Exception("The specified sound does not exist")
        sine(frequency=freq, duration=notename.value[0]) # tempo * duration beat *** TODO ***