import mido
from mido import Message
from mido.midifiles import MidiFile, MidiTrack
import operator
# from mido.ports import Multiport

msg = Message('note_on',note=60)

## input port
inport = 

## output port
outport = mido.open_output()
outport.send(msg)
