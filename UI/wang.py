MIDINote = [48, 50, 52, 53, 55, 57, 59,
            60, 62, 64, 65, 67, 69, 71,
            72, 74, 76, 77, 79, 81, 83,
            84, 86, 88, 89, 91, 93, 95]

tonality = {'C': 48, 'C#': 49, 'D': 50, 'D#': 51, 'E': 52, 'F': 53, 'F#': 54, 'G': 43, 'G#': 44, 'A': 45, 'A#': 46, 'B': 47}

Mn = {'major': [2, 2, 1, 2, 2, 2, 1],
      'natural minor': [2, 1, 2, 2, 1, 2, 2],
      'harmonic minor': [2, 1, 2, 2, 1, 3, 1],
      'melodic minor': [2, 1, 2, 2, 2, 2, 1]}

del MIDINote[:]
MIDINote.append(tonality[self.key_value.get()])
for index in range(0, 4):
    for index2 in range(0, 7):
        MIDINote.append(MIDINote[-1]+Mn[self.key_Mm_value.get()][index2])
        MIDINote[index2+index*7] = MIDINote[index2+index*7]+mode[self.mode_value.get()][index2]
generate_chord_note()
if (self.key_value.get() == "F" and self.key_Mm_value.get() == "major") or \
                (self.key_value.get() == "D" and self.key_Mm_value.get().find("minor") > 0):
            initial_setting.timeSignature = ["flat", 1]
        elif (self.key_value.get() == "G" and self.key_Mm_value.get() == "major") or \
                (self.key_value.get() == "E" and self.key_Mm_value.get().find("minor") > 0):
            initial_setting.timeSignature = ["sharp", 1]
        elif (self.key_value.get() == "A#" and self.key_Mm_value.get() == "major") or \
                (self.key_value.get() == "G" and self.key_Mm_value.get().find("minor") > 0):
            initial_setting.timeSignature = ["flat", 2]
        elif (self.key_value.get() == "D" and self.key_Mm_value.get() == "major") or \
                (self.key_value.get() == "B" and self.key_Mm_value.get().find("minor") > 0):
            initial_setting.timeSignature = ["sharp", 2]
        elif (self.key_value.get() == "D#" and self.key_Mm_value.get() == "major") or \
                (self.key_value.get() == "C" and self.key_Mm_value.get().find("minor") > 0):
            initial_setting.timeSignature = ["flat", 3]
        elif (self.key_value.get() == "A" and self.key_Mm_value.get() == "major") or \
                (self.key_value.get() == "F#" and self.key_Mm_value.get().find("minor") > 0):
            initial_setting.timeSignature = ["sharp", 3]
        elif (self.key_value.get() == "G#" and self.key_Mm_value.get() == "major") or \
                (self.key_value.get() == "F" and self.key_Mm_value.get().find("minor") > 0):
            initial_setting.timeSignature = ["flat", 4]
        elif (self.key_value.get() == "E" and self.key_Mm_value.get() == "major") or \
                (self.key_value.get() == "C#" and self.key_Mm_value.get().find("minor") > 0):
            initial_setting.timeSignature = ["sharp", 4]
        elif (self.key_value.get() == "C#" and self.key_Mm_value.get() == "major") or \
                (self.key_value.get() == "A#" and self.key_Mm_value.get().find("minor") > 0):
            initial_setting.timeSignature = ["flat", 5]
        elif (self.key_value.get() == "B" and self.key_Mm_value.get() == "major") or \
                (self.key_value.get() == "G#" and self.key_Mm_value.get().find("minor") > 0):
            initial_setting.timeSignature = ["sharp", 5]
        elif (self.key_value.get() == "F#" and self.key_Mm_value.get() == "major") or \
                (self.key_value.get() == "D#" and self.key_Mm_value.get().find("minor") > 0):
            initial_setting.timeSignature = ["flat", 6]
