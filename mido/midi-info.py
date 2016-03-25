import mido
import operator
from mido import Message
from mido.midifiles import MidiFile, MidiTrack
from mido import MidiFile, MetaMessage

i = 0

name = input('Input the file name: ')

mid = MidiFile(name)
for i, track in enumerate(mid.tracks):
	print('Track {}: {}'.format(i, track.name))
	for message in track:
		i=i+1
		# print(i,' ',message)
		string = message
		print(i,' ',string)