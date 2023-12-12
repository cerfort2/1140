import Software_Track_Controller.Block
from Software_Track_Controller.Block import *
def plc(blocks:Block = []):
    loop1 = False
    loop2 = False
    leg = False
    for i in range(0, 16):
        loop1 = loop1 or blocks[i].getOccupancy()
    for i in range(43, 67):
        loop2 = loop2 or blocks[i].getOccupancy()
    for i in range(32, 38):
        leg = leg or blocks[i].getOccupancy()


    #Switch C10 - YARD(T77) , C10 - D11
    if((True) or blocks[76].getOccupancy()):
        blocks[9].setSwitch(False)
    if(not (True) or blocks[10].getOccupancy()):
        blocks[9].setSwitch(True)
    #Signal C10
    if(blocks[9].getOccupancy()):
        blocks[9].setSignal(False)
    else:
        blocks[9].setSignal(True)
    #Signal D11
    if(blocks[10].getOccupancy()):
        blocks[10].setSignal(False)
    else:
        blocks[10].setSignal(True)
    #Signal Yard
    if(not loop1 and blocks[76].getOccupancy()):
        blocks[76].setSignal(False)
    else:
        blocks[76].setSignal(True)


    #Switch  F16 - A1, F16 - E15
    if(blocks[0].getOccupancy() or blocks[15].getOccupancy()):
        blocks[15].setSwitch(False)
    if(blocks[14].getOccupancy()):
        blocks[15].setSwitch(True)
    #Signal A1
    if(blocks[0].getOccupancy()):
        blocks[0].setSignal(False)
    else:
        blocks[0].setSignal(True)
    #Signal E15
    if(blocks[14].getOccupancy()):
        blocks[14].setSignal(False)
    else:
        blocks[14].setSignal(True)
    #Signal F16
    if(blocks[15].getOccupancy()):
        blocks[15].setSignal(False)
    else:
        blocks[15].setSignal(True)


    #Switch H27 - H28 , H27 - T76
    if(blocks[25].getOccupancy() or blocks[27].getOccupancy()):
        blocks[26].setSwitch(False)
    elif(blocks[75].getOccupancy()):
        blocks[15].setSwitch(True)
    #Signal H27
    if(blocks[26].getOccupancy() and not(blocks[27].getOccupancy() or blocks[28].getOccupancy())):
        blocks[26].setSignal(False)
    else:
        blocks[26].setSignal(True)
    #Signal H28
    if(blocks[27].getOccupancy() and not(loop1 or blocks[76].getOccupancy())):
        blocks[27].setSignal(False)
    else:
        blocks[27].setSignal(True)
    #Signal T76
    if(blocks[75].getOccupancy() and not(loop1 or blocks[76].getOccupancy())):
        blocks[75].setSignal(False)
    else:
        blocks[75].setSignal(True)

    
    #Switch H33 - R72 , H33 - H32
    if(blocks[33].getOccupancy() or blocks[71].getOccupancy()):
        blocks[32].setSwitch(False)
    elif(blocks[31].getOccupancy()):
        blocks[32].setSwitch(True)
    #Signal H32
    if(blocks[31].getOccupancy() and not(leg or blocks[70].getOccupancy())):
        blocks[31].setSignal(False)
    else:
        blocks[31].setSignal(True)
    #Signal H33
    if(blocks[32].getOccupancy() and not(blocks[71].getOccupancy() or blocks[72].getOccupancy())):
        blocks[32].setSignal(False)
    else:
        blocks[32].setSignal(True)
    #Signal R72
    if(blocks[71].getOccupancy() and not(blocks[32].getOccupancy() or blocks[33].getOccupancy())):
        blocks[71].setSignal(False)
    else:
        blocks[71].setSignal(True)
    

    #Switch H38 - H39 , H38 - Q71
    if(blocks[36].getOccupancy() or blocks[38].getOccupancy()):
        blocks[37].setSwitch(False)
    elif(blocks[70].getOccupancy()):
        blocks[37].setSwitch(True)
    #Signal H38
    if(blocks[37].getOccupancy() and not(blocks[38].getOccupancy() or blocks[39].getOccupancy())):
        blocks[37].setSignal(False)
    else:
        blocks[37].setSignal(True)
    #Signal H39
    if(blocks[38].getOccupancy() and not(blocks[37].getOccupancy() or blocks[36].getOccupancy())):
        blocks[38].setSignal(False)
    else:
        blocks[38].setSignal(True)
    #Signal Q71
    if(blocks[70].getOccupancy() and not(leg)):
        blocks[70].setSignal(False)
    else:
        blocks[70].setSignal(True)


    #Switch H44 - O67 , H44 - H43
    if(blocks[44].getOccupancy() or blocks[66].getOccupancy()):
        blocks[43].setSwitch(False)
    elif(blocks[42].getOccupancy()):
        blocks[43].setSwitch(True)
    #Signal H43
    if(blocks[42].getOccupancy() and not(loop2)):
        blocks[42].setSignal(False)
    else:
        blocks[42].setSignal(True)
    #Signal H44
    if(blocks[43].getOccupancy() and not(blocks[66].getOccupancy() or blocks[67].getOccupancy())):
        blocks[43].setSignal(False)
    else:
        blocks[43].setSignal(True)
    #Signal O67
    if(blocks[66].getOccupancy() and not(loop2)):
        blocks[66].setSignal(False)
    else:
        blocks[66].setSignal(True)


    #Crossroad I47
    if(blocks[45].getOccupancy() or blocks[46].getOccupancy() or blocks[47].getOccupancy()):
        blocks[46].setCrossroad(True)
    else:
        blocks[46].setCrossroad(False)


    #Switch J52 - J53 , J52 - N66
    if(blocks[50].getOccupancy()):
        blocks[43].setSwitch(False)
    if(blocks[50].getOccupancy()):
        blocks[65].setSwitch(True)
    #Signal J52
    if(blocks[51].getOccupancy()):
        blocks[51].setSignal(False)
    else:
        blocks[51].setSignal(True)
    #Signal J53
    if(blocks[52].getOccupancy()):
        blocks[52].setSignal(False)
    else:
        blocks[52].setSignal(True)
    #Signal N66
    if(blocks[65].getOccupancy()):
        blocks[65].setSignal(False)
    else:
        blocks[65].setSignal(True)


def plcc(blocks:Block = []):
    return []
