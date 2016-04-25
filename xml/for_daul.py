import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse, Element

global fileaString
### count the all the words
def wordCount(name):
    all = 0
    file = open(name, 'r')
    sa = file.readlines()   # 將檔案文字讀進陣列
    for x in sa:
        sa1 = x.split(' ')  # 處理空白字元
        for y in sa1:
            sa2 = y.split('\n') # 處理換行字元
            for z in sa2:
                all += len(z)   # 將所有字數相加
    return all
    # print('all the words: ',all)

def file():
    filea = open('chord.xml', 'r')
    chord_part = open('chord_part.xml','w')
    chord_up = open('chord_up.xml','w')

    fileaString = filea.read()


    ### find measure location and count the site
    '''
    idFilter = 'measure'
    idPosition = fileaString.find(idFilter)
    count = filea.seek(idPosition,0)
#   wordCount('chord.xml')
    '''

    tatol = wordCount('chord.xml')
    print('tatol: ',tatol)

    count = 0
    pre = 0
    idFilter = 'measure'
    
    #print(fileaString.center('measure'))

    
    for count in range(tatol):
        idPosition = fileaString.find(idFilter, count, tatol)
        # idPosition2 = fileaString.find(endd, count2, tatol)

        if(pre != idPosition):
                # print(idPosition)
            if (idPosition != -1):
                count = filea.seek(idPosition,0)
                print('count: ',count)

            else:
                print('count break: ',tatol)
                break

        pre = idPosition

    # print(fileaString[0:count-1])
    chord_up.write(fileaString[0:count-1])

    # print(fileaString[count-1:-28])
    # chord_part.write(fileaString[count-1:-28])

    # chord_part.write(fileaString[2221-1:5543+8])
    chord_part.write(fileaString[5557-1:7129])

    


    # filea.write('hahahhahahahahahah') 
    # chord_part = open('chord-part.xml', 'w')


    filea.close()
#    chord_up.close()
#    chord_part.close()
    


def sim_daul():
    tree = parse('chord_part.xml')
    root = tree.getroot()

    # root.remove(root.find('note'))
    for note in root.iter('note'):
        print('note')
        #duration = note.find('duration').text
        #print(duration)

        chord =  note.find('chord')
    ### 要刪除的音
        if(chord != None):
            print(chord)
            print(note)
        #    root.remove(note)
        #    print('delete')

    tree.write('chord_sim.xml')


def create_newxml():
    create_newxml = open('chord_up.xml', 'a+')
    chord_sim = open('chord_sim.xml', 'r')

    # print(chord_sim.read())
    create_newxml.write(chord_sim.read())
    create_newxml.write('</part> </score-partwise>')
    create_newxml.close()
    chord_sim.close()


if __name__ == '__main__':
    file()
#    sim_daul()
    create_newxml()
