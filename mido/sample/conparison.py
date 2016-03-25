import mido
from mido import Message
from mido.midifiles import MidiFile, MidiTrack

print('note:	',Message('note_on',note=60) == Message('note_on',note=120))


a = Message('note_on',time = 1)
b = Message('note_on',time = 2)
print('time:	',(a,a.time) == (b,b.time))