import mido
import operator
from mido import Message
from mido.midifiles import MidiFile, MidiTrack
from mido import MidiFile, MetaMessage

i = 0

name = input('Input the file name: ')

outputfile = open('new.txt','w')

mid = MidiFile(name)
for i, track in enumerate(mid.tracks):
	print('Track {}: {}'.format(i, track.name))
	for message in track:
		i=i+1
		if not isinstance(message,MetaMessage):
			print(i,' ',message)
			outputfile.write(message)
			
		# print('  parse: ',pending(message))
		# outputfile.write(string)


outputfile.close()