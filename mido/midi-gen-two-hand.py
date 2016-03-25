import mido
import operator
from mido import Message
from mido.midifiles import MidiFile, MidiTrack
from mido import MidiFile, MetaMessage  



with MidiFile(type=1) as f:
	track0 = MidiTrack()
	track1 = MidiTrack()
	f.tracks.append(track0)
	f.tracks.append(track1)

	## track 0
	track0.append(MetaMessage('time_signature', numerator=4, denominator=4, clocks_per_click=24, notated_32nd_notes_per_beat=8, time=0))
	track0.append(MetaMessage('key_signature', key='C',time=0))

	track0.append(mido.Message('control_change', channel=0, control=121, value=0, time=0))
	track0.append(mido.Message('program_change', channel=0, program=0, time=0))

	track0.append(mido.Message('control_change', channel=0, control=7, value=100, time=0))
	track0.append(mido.Message('control_change', channel=0, control=10, value=64, time=0))
	track0.append(mido.Message('control_change', channel=0, control=91, value=0, time=0))
	track0.append(mido.Message('control_change', channel=0, control=93, value=0, time=0))

	track0.append(MetaMessage('midi_port', port=0, time=0))

	track0.append(mido.Message('note_on', channel=0, note=60, velocity=80, time=0))
	track0.append(mido.Message('note_on', channel=0, note=60, velocity=0, time=455))
	track0.append(mido.Message('note_on', channel=0, note=60, velocity=80, time=25))
	track0.append(mido.Message('note_on', channel=0, note=60, velocity=0, time=455))
	track0.append(mido.Message('note_on', channel=0, note=67, velocity=80, time=25))
	track0.append(mido.Message('note_on', channel=0, note=67, velocity=0, time=455))
	track0.append(mido.Message('note_on', channel=0, note=67, velocity=80, time=25))
	track0.append(mido.Message('note_on', channel=0, note=67, velocity=0, time=455))
	track0.append(mido.Message('note_on', channel=0, note=69, velocity=80, time=25))
	track0.append(mido.Message('note_on', channel=0, note=69, velocity=0, time=455))
	track0.append(mido.Message('note_on', channel=0, note=69, velocity=80, time=25))
	track0.append(mido.Message('note_on', channel=0, note=69, velocity=0, time=455))
	track0.append(mido.Message('note_on', channel=0, note=67, velocity=80, time=25))
	track0.append(mido.Message('note_on', channel=0, note=67, velocity=0, time=911))
	
	track0.append(MetaMessage('end_of_track', time=1))

## Track 1: 
	
	track1.append(MetaMessage('key_signature', key='C', time=0))
	track1.append(MetaMessage('midi_port', port=0, time=0))

	track1.append(mido.Message('note_on', channel=0, note=48, velocity=80, time=0))
	track1.append(mido.Message('note_on', channel=0, note=48, velocity=0, time=911))
	track1.append(mido.Message('note_on', channel=0, note=52, velocity=80, time=49))
	track1.append(mido.Message('note_on', channel=0, note=52, velocity=0, time=911))
	track1.append(mido.Message('note_on', channel=0, note=48, velocity=80, time=49))
	track1.append(mido.Message('note_on', channel=0, note=48, velocity=0, time=911))
	
	track1.append(MetaMessage('end_of_track', time=1))


	f.save('two-hand-output.mid')
