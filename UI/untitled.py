### import ElementTree for parsing 
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse, Element, ElementTree

def change_Tonation(filename, Tona):

    tree = parse(filename)
    root = tree.getroot()

    print('Tona: ', Tona)


    ### #1 G    #2 D    #3 A    #4 E   
    ### b1 F   b2 bB   b3 bE   b4 bA
    dict = {'C': 0, 'G': 7, 'D': 2, 'A': 9, 'E': 4, 'F': 5, 'Bb': 10, 'Eb': 3, 'Ab': 8}
    # print('dict!!!!!' ,dict[Tona])
    # if(Tona == 'C'):

# Tona = 'C'
# change_Tonation(filename, Tona)
