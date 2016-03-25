import mido
from mido import Message
from mido.midifiles import MidiFile, MidiTrack
import operator
from mido.ports import Multiport


msg = mido.Message('note_on')
print('msg:		',msg)

print('msg byte:	',msg.bytes())
print('msg bin:	',	msg.bin())
print('msg hex:	', msg.hex())


