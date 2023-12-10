import Software_Track_Controller.Block
from Software_Track_Controller.Block import *
def plc(blocks:Block = []):
    loop1 = False
    loop2 = False
    loop1 = loop1 or blocks[76].getOccupancy()
    for i in range(0, 16):
        loop1 = loop1 or blocks[i].getOccupancy()
    for i in range(43, 67):
        loop2 = loop2 or blocks[i].getOccupancy()

    #Switch C10 - YARD(T77) , C10 - D11
    if((True) or blocks[76].getOccupancy()):
        blocks[9].setSwitch(False)
    if(not (True) or blocks[8].getOccupancy()):
        blocks[9].setSwitch(True)

    #Switch F16 - E15 , F16 - A1
    if(blocks[16].getOccupancy() or blocks[14].getOccupancy()):
        blocks[15].setSwitch(False)
    if(blocks[1].getOccupancy()):
        blocks[15].setSwitch(True)

    #Switch H27 - H28 , H27 - T76
    if(blocks[25].getOccupancy() or blocks[27].getOccupancy()):
        blocks[26].setSwitch(False)
    elif(blocks[75].getOccupancy()):
        blocks[15].setSwitch(True)

    #Switch H33 - R72 , H33 - H32
    if(blocks[33].getOccupancy() or blocks[71].getOccupancy()):
        blocks[32].setSwitch(False)
    elif(blocks[31].getOccupancy()):
        blocks[32].setSwitch(True)

    #Switch H38 - H39 , H38 - Q71
    if(blocks[36].getOccupancy() or blocks[38].getOccupancy()):
        blocks[37].setSwitch(False)
    elif(blocks[70].getOccupancy()):
        blocks[37].setSwitch(True)

    #Switch H44 - O67 , H44 - H43
    if(blocks[44].getOccupancy() or blocks[66].getOccupancy()):
        blocks[43].setSwitch(False)
    elif(blocks[42].getOccupancy()):
        blocks[43].setSwitch(True)

    #Switch J52 - J53 , J52 - N66
    if(blocks[50].getOccupancy()):
        blocks[43].setSwitch(False)
    if(blocks[50].getOccupancy()):
        blocks[65].setSwitch(True)

def plcc(blocks:Block = []):
    return []
