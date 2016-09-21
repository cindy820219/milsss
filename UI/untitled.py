######### Original #########
            ### left hand delete 'chord'
            if(chord != None and daul_staff_data == '2'):
                queue.append(note)

            ### right hand delete 'chord'
            if(chord != None and daul_staff_data == '1'):
                queue.append(daul_pre_note)
            
            daul_pre_note = note

            ### print('queue: ',queue)
######### Original #########


	for i in queue:
            measure.remove(i)

    queue_delete = []