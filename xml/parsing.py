from xml.dom.minidom import parse
import xml.dom.minidom

import pprint
pp = pprint.PrettyPrinter(indent=4)

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse('two-hand-2.xml')

### root
collection = DOMTree.documentElement
if collection.hasAttribute('shelf'):
    print('Root element : %s' % collection.getAttribute('shelf'))

attrs = collection.getElementsByTagName('attributes')

for attr in attrs:

	divs = collection.getElementsByTagName('divisions')
	for div in divs:
		divisions = div.childNodes[0].data
		print('divisions:' ,divisions)

	keys = collection.getElementsByTagName('key')
	for key in keys:
		fifths = key.getElementsByTagName('fifths')[0]

		fifths = fifths.childNodes[0].data
		print('key:' ,fifths)

	times = collection.getElementsByTagName('time')
	for time in times:
		beats = time.getElementsByTagName('beats')[0]
		beattype = time.getElementsByTagName('beat-type')[0]

		beats = beats.childNodes[0].data
		beattype = beattype.childNodes[0].data
		print('times: ',beats+'/'+beattype+' ')

### about the tempo
directions = collection.getElementsByTagName('direction')
for direction in directions:

	per_minute = collection.getElementsByTagName('per-minute')[0]
	per_minute = per_minute.childNodes[0].data
	print('view_tempo: ',per_minute)

sounds = collection.getElementsByTagName('sound')
# print(sounds)
for sound in sounds:
	if (sound.hasAttribute('tempo')):
		sound = sound.getAttribute('tempo')
		print('tempo: ',sound)

print('pitch		duration	type 		staff 		rhythm')

# Get all the measures in the collection
#measures = collection.getElementsByTagName('measure')
pre_staff = 0
measure = 1

'''for measure in measures:
	if measure.hasAttribute('number'):
		#print(measure)
		print('--------------------------------------------------------------------')
		print('measure: %s' % measure.getAttribute('number'))
'''	

### notes is a list
notes = collection.getElementsByTagName('note')
print('1=======================================================================')
for note in notes:
	# if (note.hasAttribute('default-x')):
	#	print('default-x: %s' % note.getAttribute('default-x'))
	
	pitch = step_data = octave_data = type_data = staff_next_data  = staff_data = ''

	duration = note.getElementsByTagName('duration')[0]

	# type = note.getElementsByTagName('type')[0]
	if (note.getElementsByTagName('type')):	
		type = note.getElementsByTagName('type')[0]
		type_data = type.childNodes[0].data

	if (note.getElementsByTagName('pitch')):
		pitch = note.getElementsByTagName('pitch')[0]

		step = pitch.getElementsByTagName('step')[0]
		octave = pitch.getElementsByTagName('octave')[0]

	#if (step.childNodes):
		step_data = step.childNodes[0].data
	#if (octave.childNodes):
		octave_data = octave.childNodes[0].data

	if (step_data == ''):
		step_data = '[  ]'

	if (type_data == ''):
		type_data = '---'


	if (note.getElementsByTagName('staff')):	
		staff = note.getElementsByTagName('staff')[0]
		staff_data = staff.childNodes[0].data			

		# next measure
		if (int(staff_data)== 1):
			if(pre_staff == 2): 
				# print('pre_staff == 2 and staff_data == 1')
				#print(measure)
				measure = measure+1
				print(measure,'=======================================================================')
				pre_staff = 1

		if(int(staff_data)== 1):	
			pre_staff = 1
		
		if(int(staff_data)== 2):	
			pre_staff = 2			

	### to count the number measures
	# if(staff.childNodes[0].data == '1'):
	#	measures = measures+1
	#	print(measures,'-------------------------------------------')

	if (staff_data == ''):
		staff_data = ''

	### tie has not finished yet
	#if (note.getElementsByTagName('tie')):

	#pp.pprint(step.childNodes[0].data)
	#print('print!!!!!!!!!!!')
	print(step_data
		+octave_data
		+'		'+duration.childNodes[0].data
		+'		'+type_data
		+'		'+staff_data
		+'		'+str(float(duration.childNodes[0].data)/float(divisions)))
		