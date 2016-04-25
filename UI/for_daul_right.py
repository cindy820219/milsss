import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse, Element, dump

global fileaString
### count the all the words
# def wordCount(name):
#     all = 0
#     file = open(name, 'r')
#     sa = file.readlines()   # 將檔案文字讀進陣列
#     for x in sa:
#         sa1 = x.split(' ')  # 處理空白字元
#         for y in sa1:
#             sa2 = y.split('\n') # 處理換行字元
#             for z in sa2:
#                 all += len(z)   # 將所有字數相加

#     # print('all the words: ',all)

# def file():
#     filea = open('chord.xml', 'r')
#     chord_part = open('chord_part.xml','w')
#     chord_up = open('chord_up.xml','w')

#     fileaString = filea.read()

#     ### find measure location and count the site
#     idFilter = 'measure'
#     idPosition = fileaString.find(idFilter)
#     count = filea.seek(idPosition,0)
#     wordCount('chord.xml')

#     # print(fileaString[0:count-1])
#     chord_up.write(fileaString[0:count-1])

#     # print(fileaString[count-1:-28])
#     chord_part.write(fileaString[count-1:-28])
#     # filea.write('hahahhahahahahahah') 
#     # chord_part = open('chord-part.xml', 'w')


#     filea.close()
#     chord_up.close()
#     chord_part.close()
    


# def sim_daul():
#     tree = parse('chord_part.xml')
#     root = tree.getroot()

#     # root.remove(root.find('note'))
#     for note in root.iter('note'):
#         # dump(note)
#         #duration = note.find('duration').text
#         #print(duration)

        
#         ### 要刪除的音
#         chord =  note.find('chord')
#         if(chord != None):
#             print(chord)
#             # dump(note)
#             root.remove(note)
#             print('##########################################')
#             print('note deleted')
#             print('##########################################')
            

#     tree.write('chord_sim.xml')

    

# def create_newxml():
#     create_newxml = open('chord_up.xml', 'a+')
#     chord_sim = open('chord_sim.xml', 'r')

#     # print(chord_sim.read())
#     create_newxml.write(chord_sim.read())
#     create_newxml.write('</part> </score-partwise>')
#     create_newxml.close()
#     chord_sim.close()


if __name__ == '__main__':
    # file()
    # sim_daul()
    # create_newxml()
    chord_sim = open('chord_sim.xml', 'w')

    tree = parse('two-hand-2.xml')
    root = tree.getroot()

    # root.remove(root.find('note'))
    for measure in root.iter('measure'):
        #dump(measure)
        print('###########################')

        for note in measure.iter('note'):
            ### 要刪除的音
            chord =  note.find('chord')
            print('find chord')
            if(chord != None):
                print(chord)
                # dump(note)
                measure.remove(note)
                print('##########################################')
                print('note deleted')
                print('##########################################')
            

    tree.write('chord_sim.xml')

    

# def create_newxml():
#     create_newxml = open('chord_up.xml', 'a+')
#     chord_sim = open('chord_sim.xml', 'r')

#     # print(chord_sim.read())
#     create_newxml.write(chord_sim.read())
#     create_newxml.write('</part> </score-partwise>')
#     create_newxml.close()
#     chord_sim.close()