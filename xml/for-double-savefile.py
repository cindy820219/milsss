from xml.dom.minidom import parse
import xml.dom.minidom
import math

file = open('parse-result.txt','w') 

# Open XML document using minidom parser
open_filename = input('Plz input the file name: ')
# DOMTree = xml.dom.minidom.parse('two-hand-1.xml')
DOMTree = xml.dom.minidom.parse(open_filename)

### root
collection = DOMTree.documentElement

pre_staff = 0
measure = 1

pre_x_1 = pre_x_2 = ''
pre_step_data = pre_octave_data = ''

mini_rhythm = 6

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
Str += ('\n'+'pitch		duration	type 		staff 		rhythm' + '\n')

### notes is a list
notes = collection.getElementsByTagName('note')
# print('1=======================================================================')
Str += ('\n'+'1======================================================================='+'\n')

for note in notes:
	# if note.hasAttribute('default-x'):
	#	print('default-x: %s' % note.getAttribute('default-x'))
	daul = ''
	close_daul = 0

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
		pre_step_data = pre_x_1 = pre_x_2 = ''

	if (type_data == ''):
		type_data = '---'

	### to reguar the right-hand or left-hand
	if (note.getElementsByTagName('staff')):	
		staff = note.getElementsByTagName('staff')[0]
		staff_data = staff.childNodes[0].data			

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
						# daul = 'there is a right daul: '+pre_step_data+pre_octave_data+' and '+step_data+octave_data
						Str += ('there is a right daul: '+pre_step_data+pre_octave_data+' and '+step_data+octave_data+'\n')
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
						#daul = 'there is a left daul: '+pre_step_data+pre_octave_data+' and '+step_data+octave_data
						Str += ('there is a left daul: '+pre_step_data+pre_octave_data+' and '+step_data+octave_data+'\n')
		# next measure
		if (int(staff_data)== 1):
			if(pre_staff == 2): 
				# print('pre_staff == 2 and staff_data == 1')
				#print(measure)
				measure = measure+1
				# print(measure,'=======================================================================')
				Str += '\n'+str(measure)+'======================================================================='+'\n'
			
				
				pre_staff = 1
				pre_step_data = pre_x_1 = pre_x_2 = ''

		if(int(staff_data)== 1):	
			pre_staff = 1
			pre_x_1 = note.getAttribute('default-x')
			pre_step_data = step_data
			pre_octave_data = octave_data
			# print(staff_data_1_x)
		
		if(int(staff_data)== 2):	
			pre_staff = 2	
			pre_x_2 = note.getAttribute('default-x')
			pre_step_data = step_data
			pre_octave_data = octave_data
			# print(staff_data_2_x)	

	if (staff_data == ''):
		staff_data = ''

	rhythm = str(float(duration.childNodes[0].data)/float(divisions))
	# print(rhythm)

	#print(step_data
	#	+octave_data
	#	+'		'+duration.childNodes[0].data
	#	+'		'+type_data
	#	+'		'+staff_data
	#	+'		'+rhythm)

	Str += (step_data
		+octave_data
		+'		'+duration.childNodes[0].data
		+'		'+type_data
		+'		'+staff_data
		+'		'+rhythm+'\n')


	if (daul != ''):
		print(daul)

	if(float(rhythm) < float(mini_rhythm)):
		mini_rhythm = rhythm
		

# print('mini rhythm is : ',mini_rhythm)
Str += ('\n'+'mini rhythm is : '+ str(mini_rhythm) +'\n')
		
file.write(Str)
print(' Finished! \n ', 'the file-name is "parse-result.txt"')