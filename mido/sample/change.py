import mido
from mido import Message
from mido.midifiles import MidiFile, MidiTrack
import operator
# from mido.ports import Multiport

msg = Message('note_on',note=60,velocity=3, tine=6.2)

print('msg:	',msg)
print('type:	',msg.type)
print('note:	',msg.note)
print('Vel:	',msg.velocity)
print('---------------------')

print('channel:	',msg.channel)
# we can't change the type of the message.