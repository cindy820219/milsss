### import parsing
from xml.dom.minidom import parse
import xml.dom.minidom

### import ElementTree
from xml.etree.ElementTree import ElementTree, Element, parse

def simple_dual(DOMTree, collection, level):
    ### ????
    a = 0

    # new_for_parse.py


    ### to count the number of three dual notes
    chord_pre = 0
    chord_now = 0
    chord_three = 0
    
    ### to count the total PI
    total_PI = 1

    ### test !!! not on the on-beat dual notes
    count_rest = 0

    ### parsing the file
    tree = parse('change_parse.xml')
    root = tree.getroot()
    print(' is in the simple_dual function !')

    ### pre notes
    daul_pre_note = ''
    daul_pre_pre_note = ''
    daul_staff_data = ''


    ### default measure_max and measure_num
    measure_max = 0
    measure_num = 0

    for measure in root.iter('measure'):
        measure_max = measure_max +1

    print('innnnnnnnnnnnnnnnnnnnnnnn level', level)
    ### write to the test_dual.xml
    if(level == 2):
        high_dual_fun(root, tree)
    # if(level == 1):
        # low_dual_func(root, tree)
    

def high_dual_fun(root, tree):
    ### high !!!
    daul_pre_note = ''
    ### count all the chord notes
    chord_num = 0

    ### to count the number of three dual notes
    chord_pre = 0
    chord_now = 0
    chord_three = 0

    is_three_chord = 0 

    
    ### to get the divisions :(((
    DOMTree = xml.dom.minidom.parse('change_parse.xml')
    collection = DOMTree.documentElement

    attrs = collection.getElementsByTagName('attributes')
    for attr in attrs:
        times = collection.getElementsByTagName('time')
        
        for time in times:
            beats = time.getElementsByTagName('beats')[0]
            beats = beats.childNodes[0].data

    # print(beats)

    for measure in root.iter('measure'):
        for note in measure.iter('note'):
            # print('here note: ',note)

            is_three_chord = 0

            for staff in note.iter('staff'):
                daul_staff_data = staff.text
                # print('daul_staff_data: ',daul_staff_data)
            
            chord_now = 0

            ### must delete notes
            chord = note.find('chord')

            ### count all the chord
            if (chord != None):
                chord_num = chord_num + 1
                chord_now = 1
            
             ### count the number of chord we need to keep


            ### three notes
            if(chord_pre == 1 and chord_now == 1):
                chord_three = chord_three + 1
                is_three_chord = 1
            # print('chord_three: ', chord_three)

            ### left hand delete 'chord'
            if(is_three_chord == 1):
                if(chord != None):
                    if(daul_staff_data == '1'):
                        xml.etree.ElementTree.SubElement(daul_pre_note, 'must_chord_delete')
                        daul_pre_note.find('must_chord_delete').text = 'yes'    
                        

                        #### delete pre_pre_note chord_delete
                        # for measure in root.iter('measure'):
                        #     for note in measure.iter('note'):
                        #         if(note.find('chord_delete') != None):
                        #             measure.remove(note)

                        if(daul_pre_pre_note.find('chord_delete') != None):
                            chord_delete = daul_pre_pre_note.find('chord_delete')
                            daul_pre_pre_note.remove(chord_delete)
                        #     # daul_pre_pre_note.remove(chord_delete)
                    
                    if(daul_staff_data == '2'):
                        xml.etree.ElementTree.SubElement(daul_pre_note, 'must_chord_delete')
                        daul_pre_note.find('must_chord_delete').text = 'yes'    
                is_three_chord = 0


            if(chord != None and daul_staff_data == '2' and is_three_chord == 0):
                # xml.etree.ElementTree.SubElement(note, 'rest')

                xml.etree.ElementTree.SubElement(note, 'chord_delete')
                note.find('chord_delete').text = 'yes'

            ### right hand delete 'chord'
            if(chord != None and daul_staff_data == '1' and is_three_chord == 0):
                xml.etree.ElementTree.SubElement(daul_pre_note, 'chord_delete')
                daul_pre_note.find('chord_delete').text = 'yes'                            
                
                ### is important
                # if(note.find('chord') != None):
                #     chord =  note.find('chord')
                #     note.remove(chord)
            
            if(daul_pre_note != ''):
                daul_pre_pre_note = daul_pre_note
            daul_pre_note = note
            chord_pre = chord_now

    # ### here is delete the notes !!!
    # for measure in root.iter('measure'):
    #     for note in measure.iter('note'):
    #         if(note.find('must_chord_delete') != None):
    #             measure.remove(note)

    # for measure in root.iter('measure'):
    #     for note in measure.iter('note'):
    #         if(note.find('must_chord_delete') != None):
    #             measure.remove(note)
    print('delete_high_dual.xml')
    tree.write('change_temp.xml')
    tree.write('delete_high_dual.xml')

    chord_num = chord_num - chord_three
    # print(chord_num)
    # print(chord_three)
    ### count chord_min and chord_max
    chord_min = chord_num *2 // 5 - chord_three
    chord_max = chord_num *3 // 5 - chord_three

    if(chord_min < 0):
        chord_min=0
    
    if(chord_max < 0):
        chord_max=0


    print(chord_min,chord_max)

    case(chord_max, chord_min)

def case(chord_max, chord_min):
    # print(chord_max, chord_min)
    lenth_1 = 0
    lenth_2 = 0
    lenth_3 = 0
    lenth_4 = 0

    ### parsing the file
    tree = parse('delete_high_dual.xml')
    root = tree.getroot()
    b = 0
    for measure in root.iter('measure'):
        for note in measure.iter('note'):

            if(note.find('chord_delete') != None):
                if(note.find('must_chord_delete') != None):
                    # print('here')
                    # b = 1
                    break
                else:
                    for staff in note.iter('staff'):
                        staff_text = staff.text
                        # print(staff_text)
                    for TotalPI in note.iter('TotalPI'):
                        TotalPI_text = TotalPI.text
                        TotalPI_text = float(TotalPI_text)

                        if(float(TotalPI_text) == 1.0):
                            lenth_1 = lenth_1 +1
                        
                        if(float(TotalPI_text) == 2.0):
                            lenth_2 = lenth_2 +1
                            
                        if(float(TotalPI_text) == 3.0):
                            lenth_3 = lenth_3 +1
                            
                        if(float(TotalPI_text) == 4.0):
                            lenth_4 = lenth_4 +1

    print(lenth_1)
    print(lenth_2)
    print(lenth_3)
    print(lenth_4)

    case = 0

    if(chord_min <= lenth_1):
        if( lenth_1 <= chord_max):
            case = 1
        elif( lenth_1 > chord_max):
            case = 2
            # case = 1

    elif(chord_min <= lenth_1 + lenth_3):
        if( lenth_1+lenth_3 <= chord_max):
            case = 3
    
        elif( lenth_1+lenth_3 > chord_max):
            case = 4
    

    elif(chord_min <= lenth_1 + lenth_3 + lenth_2):
        if( lenth_1+lenth_3+lenth_2 <= chord_max):
            case = 5
        
        elif( lenth_1+lenth_3+lenth_2 > chord_max):
            case = 6

    elif(chord_min <= lenth_1 + lenth_3 + lenth_2+lenth_4):
        if( lenth_1+lenth_3+lenth_2+lenth_4 <= chord_max):
            case = 7
        
        elif( lenth_1+lenth_3+lenth_2+lenth_4 > chord_max):
            case = 8

    elif(chord_min > lenth_1 + lenth_3 + lenth_2+lenth_4):
        case = 9

    # print(lenth_1 + lenth_3 + lenth_2+lenth_4)

    print('case: ',case)

    case_delete_function(case)

def case_delete_function(case):
    tree = parse('delete_high_dual.xml')
    root = tree.getroot()

    must_delete = 0

    quene_delete = []

    if(case == 1 or case == 2):
    # if(case == 1):
        print('case 1 in')
        for measure in root.iter('measure'):
            for note in measure.iter('note'):
                if(must_delete == 1):
                    # print('^^^^^^^')
                    # for MIDI in note.iter('MIDI'):
                    #     print('must_delete', MIDI.text)
                    # for TotalPI in note.iter('TotalPI'):
                    #     print('must_delete',TotalPI.text)
                    # print('^^^^^^^')
                    # for MIDI in pre_note.iter('MIDI'):
                    #     print('aaa', MIDI.text)
                    # for TotalPI in pre_note.iter('TotalPI'):
                    #     print('aaa',TotalPI.text)
                    # print('========')

                    # if(note.find('must_chord_delete') != None):
        
                    if(note.find('chord') != None):
                        if(pre_note.find('must_chord_delete') != None):
                            print('here 1')
                        else:
                            chord = note.find('chord')
                            note.remove(chord)

                    # measure.remove(pre_note)
                    quene_delete.append(pre_note)


                must_delete = 0

                if(note.find('chord_delete') != None):
                    for staff in note.iter('staff'):
                        staff_text = staff.text
                        for TotalPI in note.iter('TotalPI'):
                            TotalPI_text = TotalPI.text
                            TotalPI_text = float(TotalPI_text)
                            
                            if(TotalPI_text == 4.0 or TotalPI_text == 2.0 or TotalPI_text == 3.0):
                                if(staff_text == '1'):
                                    must_delete = 1
                                elif(staff_text == '2'):
                                    # measure.remove(note)
                                    quene_delete.append(note)


                            ### ### ### 
                            if(1.0 < TotalPI_text < 2.0):
                                if(staff_text == '1'):
                                    must_delete = 1
                                    
                                elif(staff_text == '2'):
                                    # measure.remove(note)
                                    quene_delete.append(note)


                            if(2.0 < TotalPI_text < 3.0):
                                if(staff_text == '1'):
                                    must_delete = 1
                                    print('here !!!!')


                                elif(staff_text == '2'):
                                    # measure.remove(note)
                                    quene_delete.append(note)



                            if(3.0 < TotalPI_text < 4.0):
                                if(staff_text == '1'):
                                    must_delete = 1
                                elif(staff_text == '2'):
                                    # measure.remove(note)
                                    quene_delete.append(note)


                            if(4.0 < TotalPI_text):
                                if(staff_text == '1'):
                                    must_delete = 1
                                elif(staff_text == '2'):
                                    # measure.remove(note)
                                    quene_delete.append(note)


                            ### ### ###
                            pre_note = note



            for i in quene_delete:
                measure.remove(i)
            quene_delete = []



        # for measure in root.iter('measure'):
        #     for note in measure.iter('note'):
        #         if(must_delete == 1):
        #             if(note.find('chord') != None):
        #                 if(pre_note.find('must_chord_delete') != None):
        #                     print('here')
        #                 else:
        #                     chord = note.find('chord')
        #                     note.remove(chord)
        #             measure.remove(pre_note)
        #         must_delete = 0

        #         if(note.find('chord_delete') != None):
        #             for staff in note.iter('staff'):
        #                 staff_text = staff.text
        #                 for TotalPI in note.iter('TotalPI'):
        #                     TotalPI_text = TotalPI.text
        #                     TotalPI_text = float(TotalPI_text)
                            
        #                     if(TotalPI_text == 4.0 or TotalPI_text == 2.0 or TotalPI_text == 3.0):
        #                         if(staff_text == '1'):
        #                             must_delete = 1
        #                         elif(staff_text == '2'):
        #                             measure.remove(note)
                            
        #                     ### ### ### 
        #                     if(1.0 < TotalPI_text < 2.0):
        #                         if(staff_text == '1'):
        #                             must_delete = 1
        #                         elif(staff_text == '2'):
        #                             measure.remove(note)

        #                     if(2.0 < TotalPI_text < 3.0):
        #                         if(staff_text == '1'):
        #                             must_delete = 1
        #                         elif(staff_text == '2'):
        #                             measure.remove(note)

        #                     if(3.0 < TotalPI_text < 4.0):
        #                         if(staff_text == '1'):
        #                             must_delete = 1
        #                         elif(staff_text == '2'):
        #                             measure.remove(note)
        #                     if(4.0 < TotalPI_text):
        #                         if(staff_text == '1'):
        #                             must_delete = 1
        #                         elif(staff_text == '2'):
        #                             measure.remove(note)
        #                     ### ### ###

        #                     pre_note = note

    if(case == 2):
        print('case 2 in')

    if(case == 3 or case == 4):
    # if(case == 2):
        print('case 3 in')
        for measure in root.iter('measure'):
            for note in measure.iter('note'):
                if(must_delete == 1):
                    # print('^^^^^^^')
                    # for MIDI in note.iter('MIDI'):
                    #     print('must_delete', MIDI.text)
                    # for TotalPI in note.iter('TotalPI'):
                    #     print('must_delete',TotalPI.text)
                    # print('^^^^^^^')
                    # for MIDI in pre_note.iter('MIDI'):
                    #     print('aaa', MIDI.text)
                    # for TotalPI in pre_note.iter('TotalPI'):
                    #     print('aaa',TotalPI.text)
                    # print('========')

                    # if(note.find('must_chord_delete') != None):
        
                    if(note.find('chord') != None):
                        if(pre_note.find('must_chord_delete') != None):
                            print('here')

                        else:
                            chord = note.find('chord')
                            note.remove(chord)

                    # measure.remove(pre_note)
                    quene_delete.append(pre_note)

                must_delete = 0

                if(note.find('chord_delete') != None):
                    for staff in note.iter('staff'):
                        staff_text = staff.text
                        for TotalPI in note.iter('TotalPI'):
                            TotalPI_text = TotalPI.text
                            TotalPI_text = float(TotalPI_text)
                            
                            if(TotalPI_text == 4.0 or TotalPI_text == 2.0):
                                if(staff_text == '1'):
                                    must_delete = 1
            
                                elif(staff_text == '2'):
                                    # measure.remove(note)
                                    quene_delete.append(note)

                            ### ### ### 
                            if(1.0 < TotalPI_text < 2.0):
                                if(staff_text == '1'):
                                    must_delete = 1
                                
                                elif(staff_text == '2'):
                                    # measure.remove(note)
                                    quene_delete.append(note)

                            if(2.0 < TotalPI_text < 3.0):
                                if(staff_text == '1'):
                                    must_delete = 1
                                elif(staff_text == '2'):
                                    # measure.remove(note)
                                    quene_delete.append(note)

                            if(3.0 < TotalPI_text < 4.0):
                                if(staff_text == '1'):
                                    must_delete = 1
                                elif(staff_text == '2'):
                                    # measure.remove(note)
                                    quene_delete.append(note)

                            if(4.0 < TotalPI_text):
                                if(staff_text == '1'):
                                    must_delete = 1
                                elif(staff_text == '2'):
                                    # measure.remove(note)
                                    quene_delete.append(note)

                            ### ### ###
                            pre_note = note

            for i in quene_delete:
                measure.remove(i)
            quene_delete = []


    if(case == 4):
        print('case 4')
    
    if(case == 5 or case == 6):
    # if(case == 3):
        print('case 5')
        for measure in root.iter('measure'):
            for note in measure.iter('note'):
                if(must_delete == 1):
                    # print('^^^^^^^')
                    # for MIDI in note.iter('MIDI'):
                    #     print('must_delete', MIDI.text)
                    # for TotalPI in note.iter('TotalPI'):
                    #     print('must_delete',TotalPI.text)
                    # print('^^^^^^^')
                    # if(note.find('chord') != None):
                    #     chord =  note.find('chord')
                    #     note.remove(chord)

                    # for MIDI in pre_note.iter('MIDI'):
                    #     print('aaa', MIDI.text)
                    # for TotalPI in pre_note.iter('TotalPI'):
                    #     print('aaa',TotalPI.text)
                    # print('========')
                    # measure.remove(pre_note)


                    if(note.find('chord') != None):
                        if(pre_note.find('must_chord_delete') != None):
                            print('here')
                        else:
                            chord = note.find('chord')
                            note.remove(chord)
                    # measure.remove(pre_note)
                    quene_delete.append(pre_note)

                must_delete = 0


                if(note.find('chord_delete') != None):
                    for staff in note.iter('staff'):
                        staff_text = staff.text
                        for TotalPI in note.iter('TotalPI'):
                            TotalPI_text = TotalPI.text
                            TotalPI_text = float(TotalPI_text)
                            if(TotalPI_text == 4.0):
                                if(staff_text == '1'):
                                    must_delete = 1
                                elif(staff_text == '2'):
                                    # measure.remove(note)
                                    quene_delete.append(note)
                            
                                # if(staff_text == '1'):
                                    ### next note must delete the 'chord' !!!
                                    # must_delete = 1
                                    # print('must_delete == 1', must_delete)
                                    # if(note.find('chord') != None):
                                    #     chord =  note.find('chord')
                                    #     note.remove(chord)
                                    # print('------')
                                    # for MIDI in note.iter('MIDI'):
                                    #     print(MIDI.text)
                                    # for TotalPI in note.iter('TotalPI'):
                                    #     print(TotalPI.text)
                                    # print('------')

                                # else:
                                #     # print('must_delete == 0', must_delete)
                            
                            ### ### ### 
                            if(1.0 < TotalPI_text < 2.0):
                                if(staff_text == '1'):
                                    must_delete = 1
                                elif(staff_text == '2'):
                                    # measure.remove(note)
                                    quene_delete.append(note)

                            if(2.0 < TotalPI_text < 3.0):
                                if(staff_text == '1'):
                                    must_delete = 1
                                elif(staff_text == '2'):
                                    # measure.remove(note)
                                    quene_delete.append(note)

                            if(3.0 < TotalPI_text < 4.0):
                                if(staff_text == '1'):
                                    must_delete = 1
                                elif(staff_text == '2'):
                                    # measure.remove(note)
                                    quene_delete.append(note)

                            if(4.0 < TotalPI_text):
                                if(staff_text == '1'):
                                    must_delete = 1
                                elif(staff_text == '2'):
                                    # measure.remove(note)
                                    quene_delete.append(note)
                            ### ### ###
                            
                            pre_note = note
          
            for i in quene_delete:
                measure.remove(i)
            quene_delete = []



    if(case == 6):
        print('case 6')

    if(case == 7 or case == 8 or case == 9):
        print('case 7')
        for measure in root.iter('measure'):
            for note in measure.iter('note'):
                if(must_delete == 1):
                    if(note.find('chord') != None):
                        if(pre_note.find('must_chord_delete') != None):
                            print('here')
                        else:
                            chord = note.find('chord')
                            note.remove(chord)
                    # measure.remove(pre_note)
                    quene_delete.append(pre_note)

                must_delete = 0

                if(note.find('chord_delete') != None):
                    for staff in note.iter('staff'):
                        staff_text = staff.text
                        for TotalPI in note.iter('TotalPI'):
                            TotalPI_text = TotalPI.text
                            TotalPI_text = float(TotalPI_text)
                            
                            if(TotalPI_text == 5.0):
                            # if(TotalPI_text == 4.0):
                                if(staff_text == '1'):
                                    must_delete = 1
                                elif(staff_text == '2'):
                                    # measure.remove(note)
                                    quene_delete.append(note)

                            ### ### ### 
                            if(1.0 < TotalPI_text < 2.0):
                                if(staff_text == '1'):
                                    must_delete = 1
                                elif(staff_text == '2'):
                                    # measure.remove(note)
                                    quene_delete.append(note)

                            if(2.0 < TotalPI_text < 3.0):
                                if(staff_text == '1'):
                                    must_delete = 1
                                elif(staff_text == '2'):
                                    # measure.remove(note)
                                    quene_delete.append(note)

                            if(3.0 < TotalPI_text < 4.0):
                                if(staff_text == '1'):
                                    must_delete = 1
                                elif(staff_text == '2'):
                                    # measure.remove(note)
                                    quene_delete.append(note)

                            if(4.0 < TotalPI_text):
                                if(staff_text == '1'):
                                    must_delete = 1
                                elif(staff_text == '2'):
                                    # measure.remove(note)
                                    quene_delete.append(note)
                            ### ### ###

                            pre_note = note

            for i in quene_delete:
                measure.remove(i)
            quene_delete = []



    if(case == 8):
        print('case 8')

    # if(case == 9):
    #     print('case 9')
    #     for measure in root.iter('measure'):
    #         for note in measure.iter('note'):
    #             if(must_delete == 1):
    #                 if(note.find('chord') != None):
    #                     if(pre_note.find('must_chord_delete') != None):
    #                         print('here')
    #                     else:
    #                         chord = note.find('chord')
    #                         note.remove(chord)
    #                 # measure.remove(pre_note)
    #                 quene_delete.append(pre_note)

    #             must_delete = 0

    #             if(note.find('chord_delete') != None):
    #                 for staff in note.iter('staff'):
    #                     staff_text = staff.text
    #                     for TotalPI in note.iter('TotalPI'):
    #                         TotalPI_text = TotalPI.text
    #                         TotalPI_text = float(TotalPI_text)
                            
    #                         if(TotalPI_text == 4.0 or TotalPI_text == 2.0 or TotalPI_text == 3.0 or TotalPI_text == 1.0):
    #                         # if(TotalPI_text == 4.0):
    #                             if(staff_text == '1'):
    #                                 must_delete = 1
    #                             elif(staff_text == '2'):
    #                                 # measure.remove(note)
    #                                 quene_delete.append(note)

    #                         ### ### ### 
    #                         if(1.0 < TotalPI_text < 2.0):
    #                             if(staff_text == '1'):
    #                                 must_delete = 1
    #                             elif(staff_text == '2'):
    #                                 # measure.remove(note)
    #                                 quene_delete.append(note)

    #                         if(2.0 < TotalPI_text < 3.0):
    #                             if(staff_text == '1'):
    #                                 must_delete = 1
    #                             elif(staff_text == '2'):
    #                                 # measure.remove(note)
    #                                 quene_delete.append(note)

    #                         if(3.0 < TotalPI_text < 4.0):
    #                             if(staff_text == '1'):
    #                                 must_delete = 1
    #                             elif(staff_text == '2'):
    #                                 # measure.remove(note)
    #                                 quene_delete.append(note)

    #                         if(4.0 < TotalPI_text):
    #                             if(staff_text == '1'):
    #                                 must_delete = 1
    #                             elif(staff_text == '2'):
    #                                 # measure.remove(note)
    #                                 quene_delete.append(note)
    #                         ### ### ###

    #                         pre_note = note

    #         for i in quene_delete:
    #             measure.remove(i)
    #         quene_delete = []





    for measure in root.iter('measure'):
        for note in measure.iter('note'):
            if(note.find('must_chord_delete') != None):
                measure.remove(note)

    # pre_note = ''
    # for measure in root.iter('measure'):
    #     for note in measure.iter('note'):
    #         if(note.find('chord_delete') != None):
    #             # measure.remove(note)
    #             for TotalPI in note.iter('TotalPI'):
    #                 TotalPI_text = TotalPI.text
    #                 TotalPI_text = float(TotalPI_text)
                    
    #                 if(TotalPI_text != 4.0 or TotalPI_text == 2.0 or TotalPI_text != 1.0 or TotalPI_text == 3.0):
    #                     if(staff_text == '1'):
    #                         measure.remove(pre_note)
    #                     elif(staff_text == '2'):
    #                         measure.remove(note)
    #                 pre_note = note




    tree.write('delete_high_dual.xml')
    tree.write('change_temp.xml')
    # print('delete_high_dual.xml')
    print(' ---------->  have change high dual')

def low_dual_func(root, tree):
    ### low !!!

    # tree = parse('sonatina2.xml')
    # root = tree.getroot()

    ### count all the chord notes
    chord_num = 0

    ### to count the number of three dual notes
    chord_pre = 0
    chord_now = 0
    chord_three = 0

    is_three_chord = 0

    for measure in root.iter('measure'):
        for note in measure.iter('note'):

            is_three_chord = 0

            # print('here note: ',note)
            for staff in note.iter('staff'):
                daul_staff_data = staff.text
                # print('daul_staff_data: ',daul_staff_data)
            
            chord_now = 0

            ### must delete notes
            chord = note.find('chord')

            ### count all the chord
            if (chord != None):
                chord_num = chord_num + 1
                chord_now = 1

            ### three notes
            if(chord_pre == 1 and chord_now == 1):
                chord_three = chord_three + 1
                is_three_chord = 1

            ### left hand delete 'chord'
            if(is_three_chord == 1):
                if(chord != None):
                    if(daul_staff_data == '1'):
                        xml.etree.ElementTree.SubElement(daul_pre_note, 'chord_delete')
                        daul_pre_note.find('chord_delete').text = 'yes'    
                         
                        if(note.find('chord') != None):
                            chord =  note.find('chord')
                            note.remove(chord)
            if(chord != None and daul_staff_data == '2'):
                xml.etree.ElementTree.SubElement(note, 'rest')

                xml.etree.ElementTree.SubElement(note, 'chord_delete')
                note.find('chord_delete').text = 'yes'

            ### right hand delete 'chord'
            if(chord != None and daul_staff_data == '1'):
                xml.etree.ElementTree.SubElement(daul_pre_note, 'chord_delete')
                daul_pre_note.find('chord_delete').text = 'yes'                            
                
                if(note.find('chord') != None):
                    chord =  note.find('chord')
                    note.remove(chord)
            

            daul_pre_note = note
            chord_pre = chord_now

    ### here is delete the notes !!!
    for measure in root.iter('measure'):
        for note in measure.iter('note'):
            if(note.find('chord_delete') != None):
                measure.remove(note)
    for measure in root.iter('measure'):
        for note in measure.iter('note'):
            if(note.find('chord_delete') != None):
                measure.remove(note)

    tree.write('delete_low_dual.xml')
    # print('  the file "delete_low_dual.xml" is save.')
    tree.write('change_temp.xml')
    print(' ---------->  have change low dual')

# DOMTree = xml.dom.minidom.parse('change-parse.xml')
# collection = DOMTree.documentElement
# level = 1
# hands = 0
# simple_dual(DOMTree, collection, level)

