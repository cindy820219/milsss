import mido
import operator
from mido import Message
from mido.midifiles import MidiFile, MidiTrack
from mido import MidiFile, MetaMessage  

  
with MidiFile() as f:
	track = MidiTrack()
	f.tracks.append(track)

	track.append(MetaMessage('time_signature', numerator=4, denominator=4, clocks_per_click=24, notated_32nd_notes_per_beat=8, time=0))
	track.append(MetaMessage('key_signature', key='C',time=0))
	## 500000 == (60 / 120.0) * 1000000
	track.append(MetaMessage('set_tempo', tempo=500000, time=0))


	track.append(mido.Message('control_change', channel=0, control=121, value=0, time=0))
	track.append(mido.Message('program_change', channel=0, program=0, time=0))
    
	track.append(mido.Message('control_change', channel=0, control=7, value=100, time=0))
	track.append(mido.Message('control_change', channel=0, control=10, value=64, time=0))
	track.append(mido.Message('control_change', channel=0, control=91, value=0, time=0))
	track.append(mido.Message('control_change', channel=0, control=93, value=0, time=0))

	track.append(MetaMessage('midi_port', port=0, time=0))

	track.append(mido.Message('note_on', channel=0, note=67, velocity=80, time=0))
	track.append(mido.Message('note_on', channel=0, note=67, velocity=0, time=911))

	track.append(mido.Message('note_on', channel=0, note=67, velocity=80, time=49))
	track.append(mido.Message('note_on', channel=0, note=67, velocity=0, time=455))
	
	track.append(mido.Message('note_on', channel=0, note=67, velocity=80, time=25))
	track.append(mido.Message('note_on', channel=0, note=67, velocity=0, time=455))
	
	track.append(mido.Message('note_on', channel=0, note=60, velocity=80, time=25))
	track.append(mido.Message('note_on', channel=0, note=60, velocity=0, time=455))
	
	track.append(mido.Message('note_on', channel=0, note=60, velocity=80, time=25))
	track.append(mido.Message('note_on', channel=0, note=60, velocity=0, time=455))
	
	track.append(mido.Message('note_on', channel=0, note=60, velocity=80, time=25))
	track.append(mido.Message('note_on', channel=0, note=64, velocity=80, time=0))

	track.append(mido.Message('note_on', channel=0, note=60, velocity=0, time=911))
	track.append(mido.Message('note_on', channel=0, note=64, velocity=0, time=0))

	track.append(MetaMessage('end_of_track', time=1))

	f.save('one-hand-output.mid')
  