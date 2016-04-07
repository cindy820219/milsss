from xml.dom.minidom import parse
import xml.dom.minidom
import math

# Open XML document using minidom parser
file = open('parse-result.txt','w') 

# Open XML document using minidom parser
open_filename = input('Plz input the file name: ')

DOMTree = xml.dom.minidom.parse('one-hand-1.xml')

file = open('parse-result.txt','w') 

### root
collection = DOMTree.documentElement

pre_staff = 0
measure = 1

pre_x_1 = pre_x_2 = ''
pre_step_data = pre_octave_data = ''

# about the mini_rhythm for the simple
mini_rhythm = 6

# about the ID
# ID = ''

# about the (time.rhythm / measure)
timing = 0
flag_of_daul = 0

single_measure = 1
single_time = 0
single_pre_x = ''

single_flag_of_daul = 0

hand = 1

note_num = 0

### to defind the sheet: key && divs && time
attrs = collection.getElementsByTagName('attributes')
for attr in attrs:

	divs = collection.getElementsByTagName('divisions')
	for div in divs:
		divisions = div.childNodes[0].data
		# print('divisions:' ,divisions)
		Str = ('divisions: '+ divisions+'\n')

	keys = collection.getElementsByTagName('key')
	for key in keys:
		fifths = key.getElementsByTagName('fifths')[0]
		fifths = fifths.childNodes[0].data
		# print('key:' ,fifths)
		Str += ('key:' +fifths+'\n')
		# file.write(Str)

	times = collection.getElementsByTagName('time')
	for time in times:
		beats = time.getElementsByTagName('beats')[0]
		beattype = time.getElementsByTagName('beat-type')[0]

		beats = beats.childNodes[0].data
		beattype = beattype.childNodes[0].data
		# print('times: ',beats+'/'+beattype+' ')
		Str += (beats + '/' + beattype +'\n')
		# file.write(Str)

	if ((int(beats) == 6) and (int(beattype) ==8)):
		beats = 3

### about the tempo
directions = collection.getElementsByTagName('direction')
for direction in directions:

	per_minute = collection.getElementsByTagName('per-minute')[0]
	per_minute = per_minute.childNodes[0].data
	# print('view_tempo: ',per_minute)
	Str += ('view_tempo: ' + per_minute +'\n')

sounds = collection.getElementsByTagName('sound')
# print(sounds)
for sound in sounds:
	if (sound.hasAttribute('tempo')):
		sound = sound.getAttribute('tempo')
		# print('tempo: ',sound)
		Str += ('tempo: '+ sound +'\n')

# print('pitch		duration	type 		staff 		rhythm')
Str += ('ID		pitch		type 		staff 	rhythm')

### notes is a list
notes = collection.getElementsByTagName('note')
# print('1=======================================================================')
Str += ('\n'+'1======================================================================='+'\n')

for note in notes:
	# if note.hasAttribute('default-x'):
	#	print('default-x: %s' % note.getAttribute('default-x'))
	note_num = int(note_num) + 1

	daul = ''
	close_daul = 0

	pitch = step_data = octave_data = type_data = staff_next_data  = staff_data = alter_data = ''

	duration = note.getElementsByTagName('duration')[0]
	rhythm = str(float(duration.childNodes[0].data)/float(divisions))

	if(timing >= int(beats) and (hand != 1)):
		# print('=======================================================================')
		# single_measure += 1
		timing = 0

	if (note.getElementsByTagName('accidental')):
		accidental = note.getElementsByTagName('accidental')[0]
		# alter_data = accidental.childNodes[0].data
		alter_data = '0'

	### about the type: type = note.getElementsByTagName('type')[0]
	if (note.getElementsByTagName('type')):	
		type = note.getElementsByTagName('type')[0]
		type_data = type.childNodes[0].data

	### about the pitch and octave
	if (note.getElementsByTagName('pitch')):
		pitch = note.getElementsByTagName('pitch')[0]

		step = pitch.getElementsByTagName('step')[0]
		octave = pitch.getElementsByTagName('octave')[0]

		#if (step.childNodes):
		step_data = step.childNodes[0].data
		
		#if (octave.childNodes):
		octave_data = octave.childNodes[0].data

		if(pitch.getElementsByTagName('alter')):
			alter = pitch.getElementsByTagName('alter')[0]
			alter_data = alter.childNodes[0].data
			# print(alter.childNodes[0].data)

	if (step_data == ''):
		step_data = '[ ]'
		pre_step_data = pre_x_1 = pre_x_2 = ''

	if (type_data == ''):
		type_data = '---'

	### to reguar the right-hand or left-hand
	if (note.getElementsByTagName('staff')):
		hand = 2
		staff = note.getElementsByTagName('staff')[0]
		staff_data = staff.childNodes[0].data			
		# flag_of_daul to 0
		flag_of_daul = 0

		### dual(int(staff_data),pre_staff)
		if(note.hasAttribute('default-x')):
			#if(int(staff_data) == pre_staff):
			now_x = note.getAttribute('default-x')
			
			### when daul very close 
			if(int(staff_data)==1):
				if(pre_x_1 != ''):
					pre_x_1_flaot = float(pre_x_1)
					if(now_x != ''):
						now_x_float = float(now_x)
						close_daul = math.fabs(pre_x_1_flaot-now_x_float)

				#if(pre_x_1==now_x):
				if(close_daul < 30):
					if(pre_x_1 != ''):
						daul = 'there is a right daul: '+pre_step_data+pre_octave_data+' and '+step_data+octave_data
						flag_of_daul = 1
			
			if(int(staff_data)==2):
				if(pre_x_2 != ''):
					pre_x_2_flaot = float(pre_x_2)
					if(now_x != ''):
						now_x_float = float(now_x)
						close_daul = math.fabs(pre_x_2_flaot-now_x_float)

				if(close_daul < 30):
					if(pre_x_2 != ''):
				# if(pre_x_2==now_x):
				#if(b <= 30):
					#print('there is a left daul: ', pre_step_data+pre_octave_data, 'and',step_data+octave_data)
						daul = 'there is a left daul: '+pre_step_data+pre_octave_data+' and '+step_data+octave_data
						flag_of_daul = 1

		# next measure
		if (int(staff_data)== 1):
			if(pre_staff == 2): 
				# print('pre_staff == 2 and staff_data == 1')
				#print(measure)
				timing = 0
				measure = measure+1
				Str += measure +'======================================================================='
				pre_staff = 1
				pre_step_data = pre_x_1 = pre_x_2 = ''
				

		if(int(staff_data)== 1):	
			pre_staff = 1
			pre_x_1 = note.getAttribute('default-x')
			pre_step_data = step_data
			pre_octave_data = octave_data
			# print(staff_data_1_x)
				### test!
			

		if(int(staff_data)== 2):
			pre_staff = 2	
			pre_x_2 = note.getAttribute('default-x')
			pre_step_data = step_data
			pre_octave_data = octave_data
			# print(staff_data_2_x)
		
		if(timing > int(beats)):
			timing = 0	

	### single hand
	if (hand == 1):	
		single_flag_of_daul = 0

		if(note.hasAttribute('default-x')):
			single_now_x = note.getAttribute('default-x')
			if(single_pre_x != ''):
				single_pre_x_flaot = float(single_pre_x)
				if(single_now_x != ''):
					single_now_x_float = float(single_now_x)
					close_daul = math.fabs(single_pre_x_flaot-single_now_x_float)

				if(close_daul < 30):
					if(single_pre_x != ''):
						daul='there is a daul: '+pre_step_data+pre_octave_data+' and '+step_data+octave_data
						single_flag_of_daul = 1

		pre_step_data = step_data
		pre_octave_data = octave_data

		single_pre_x = single_now_x
		#print(single_time,timing)
		
		if (single_flag_of_daul == 0):
			single_time += float(rhythm)

		if (single_time > int(beats)):
			single_measure += 1
			Str += str(single_measure) + '----------------------------------------------------------------------'+'\n'
			single_time = 0
			single_time += float(rhythm)
			timing = 0
			single_pre_x = ''

		timing = single_time


	if (staff_data == ''):
		staff_data = '0'

	# about the timing
	if(flag_of_daul == 0 and (hand != 1)):
		timing += float(rhythm)

	### About the PI		
	PI = math.floor(timing - float(rhythm) +1)
	
	# about the ID : note num(4) // measure(2) // staff(1) // timing(1)
	# ID: note_num 
	note_num = str(note_num).zfill(4)
	
	# ID: measure_id
	measure_id = str(measure) 
	measure_id = measure_id.zfill(2)
	# ID: measure_id of one-hand
	if staff_data == '0':
		measure_id = str(single_measure)
		measure_id = measure_id.zfill(2)

	# ID: staff_id
	staff_id = staff_data

	ID = note_num + measure_id + staff_id + str(PI)

	'''
	print(ID
		+'	'+step_data
		+octave_data
		+'  ' +alter_data
		+'		'+type_data
		+'		'+staff_data
		+'	'+rhythm)
	'''

	Str += (ID
		+'	'+step_data
		+octave_data
		+'  ' +alter_data
		+'		'+type_data
		+'		'+staff_data
		+'	'+rhythm+'\n')

	'''
	Str += (step_data
		+octave_data
		+'		'+duration.childNodes[0].data
		+'		'+type_data
		+'		'+staff_data
		+'		'+rhythm+'\n')
	'''

	if (daul != ''):
		#print(daul)
		Str += daul+'\n'

	if(float(rhythm) < float(mini_rhythm)):
		mini_rhythm = rhythm
		

# print('mini rhythm is : ',mini_rhythm)
Str += ('mini rhythm is : '+ str(mini_rhythm) +'\n')
		
file.write(Str)
print('\n'+' Finished! \n ', 'the file-name is "parse-result.txt"'+'\n')