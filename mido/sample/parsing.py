import mido
from mido import Message
from mido.midifiles import MidiFile, MidiTrack
import operator
# from mido.ports import Multiport
from mido import MidiFile

print('mido-parse:	',mido.parse([0x92,0x10,0x20]))
print('mido-parse-all:	',mido.parse_all([0x92,0x10,0x20,0x82,0x10,0x20]))

#####################
p = mido.Parser()
p.feed([0x90, 0x10,0x20])
print('pend:	',p.pending())

print('get message:	',p.get_message())

q = mido.Parser()
q.feed([0x90, 0x10,0x20,0x82, 0x10,0x20])
for message in q:
	print(message)