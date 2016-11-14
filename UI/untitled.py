### import ElementTree for parsing 
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse, Element, ElementTree

def change_Tonation(filename, fifths, Tona):

    tree = parse(filename)
    root = tree.getroot()

    print('Tona: ', Tona)


    ### #1 G    #2 D    #3 A    #4 E   
    ### b1 F   b2 bB   b3 bE   b4 bA
    dict = {'C': 0, 'G': 7, 'D': 2, 'A': -3, 'E': 4, 'F': 5, 'Bb': -2, 'Eb': 3, 'Ab': -4}

    # print('dict!!!!!' ,dict[Tona])
    print( 'add key: ' , dict[Tona]- int(fifths))

    tree.write('change_temp.xml')

# Tona = 'C'
# change_Tonation(filename, Tona)
