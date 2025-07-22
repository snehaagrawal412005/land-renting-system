#read.py
def readData():
    myDictionary = {}
    with open("data.txt", 'r') as file:
        kitta = 101
        for line in file:
            line = line.replace('\n', '')
            myDictionary[kitta] = line.split(',')
            kitta += 1
    return myDictionary
