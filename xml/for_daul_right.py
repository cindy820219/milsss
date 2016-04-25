import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse, Element, dump

if __name__ == '__main__':
    # file()
    # sim_daul()
    # create_newxml()
    chord_sim = open('chord_sim.xml', 'w')

    tree = parse('two-hand-2.xml')
    root = tree.getroot()

    # root.remove(root.find('note'))
    # for measure in root.iter('measure'):
    #     #dump(measure)

    #     for note in measure.iter('note'):
    #         ### 要刪除的音
    #         chord =  note.find('chord')
    #         print('find chord')

    #         if(chord != None):
    #             print(chord)
    #             # dump(note)
    #             measure.remove(note)
    #             print('##########################################')
    #             print('note deleted')
    #             print('##########################################')
    
    # tree.write('chord_sim.xml')
    
    queue = []

    for measure in root.iter('measure'):
        for note in measure.iter('note'):
            ### 要刪除的音
            chord =  note.find('chord')
            

            if(chord != None):
                print('find chord')
                queue.append(note)
                # print(queue)
        print('queue: ',queue)
        #print('append size: ',queue.qsize())
        
        for i in queue:
            measure.remove(i)
            # measure.remove(queue.pop())
            print('deleted queue[0]: ',queue)
            #print('deleted size: ',queue.qsize())

        queue = []
        #print('[] size: ',queue.qsize())
    tree.write('chord_sim.xml')
