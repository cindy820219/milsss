'''f = open('chord.xml','r+')
count = len(open('chord.xml','rU').readlines())

for line in f:
	print(f.readline().strip())
print(count)
'''

filea = open('chord.xml', 'r+')
fileaString = filea.read()
idFilter = 'measure'
idPosition = fileaString.find(idFilter)

count = filea.seek(idPosition,0)
print(count)
# filea.write('hahahhahahahahahah') 

filea = open('chord_part.xml', 'w')
filea.write('hahahhahahahahahah') 
# chord_part = open('chord-part.xml', 'w')
filea.close()


