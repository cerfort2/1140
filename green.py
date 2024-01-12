import Software_Track_Controller.Block
from Software_Track_Controller.Block import *
def plc(blocks:Block = []):
    loop1 = False
    loop2 = False
    for i in range(12, 29):
        loop1 = loop1 or blocks[i].getOccupancy()
    for i in range(76, 85):
        loop2 = loop2 or blocks[i].getOccupancy()

    for i in range(0,3): #Triple Redundancy
        #Switch D13 - C12 , D13 - A1
        if(blocks[13].getOccupancy()): 
            blocks[12].setSwitch(False)
        elif(blocks[0].getOccupancy() and not (loop1)):
            blocks[12].setSwitch(True)
        #Signal A1
        if(blocks[0].getOccupancy() or blocks[1].getOccupancy() or blocks[2].getOccupancy() or loop1):
            if((blocks[0].getOccupancy() or blocks[1].getOccupancy()) and not (loop1)):
                blocks[0].setSignal(False)
            else:
                blocks[0].setSignal(True)
        #Signal D13
        if (blocks[11].getOccupancy() or blocks[12].getOccupancy() or blocks[13].getOccupancy() or blocks[14].getOccupancy() or blocks[15].getOccupancy()):
            if((blocks[12].getOccupancy() or blocks[13].getOccupancy()) and not (blocks[10].getOccupancy() or blocks[11].getOccupancy())):
                blocks[12].setSignal(False)
            else:
                blocks[12].setSignal(True)

        #Crossroad E19
        if(blocks[16].getOccupancy() or blocks[17].getOccupancy() or blocks[18].getOccupancy() or blocks[19].getOccupancy() or blocks[20].getOccupancy()):
            if(blocks[17].getOccupancy() or blocks[18].getOccupancy() or blocks[19].getOccupancy()):
                blocks[18].setCrossroad(True)
            else:
                blocks[18].setCrossroad(False)

        #Switch G29 - G30 , G29 - Z150
        if(blocks[27].getOccupancy() or loop1):
            blocks[28].setSwitch(False)
        elif(blocks[149].getOccupancy()):
            blocks[28].setSwitch(True)
        #Signal G29
        if(blocks[26].getOccupancy() or blocks[27].getOccupancy() or blocks[28].getOccupancy() or blocks[29].getOccupancy() or blocks[30].getOccupancy()):
            if((blocks[27].getOccupancy() or blocks[28].getOccupancy()) and not (blocks[29].getOccupancy() or blocks[30].getOccupancy())):
                blocks[28].setSignal(False)
            else:
                blocks[28].setSignal(True)
        #Signal Z150
        if(blocks[27].getOccupancy() or blocks[28].getOccupancy() or blocks[147].getOccupancy() or blocks[148].getOccupancy() or blocks[149].getOccupancy()):
            if((blocks[148].getOccupancy() or blocks[149].getOccupancy()) and not loop1):
                blocks[149].setSignal(False)
            else:
                blocks[149].setSignal(True)
        

        #Switch J58 - Yard , J58 - J59
        if(True):
            blocks[57].setSwitch(False)
        else:
            blocks[57].setSwitch(True)
        #Signal J58
        if(blocks[55].getOccupancy() or blocks[56].getOccupancy() or blocks[57].getOccupancy() or blocks[58].getOccupancy() or blocks[59].getOccupancy()):
            if((blocks[56].getOccupancy() or blocks[57].getOccupancy()) and not (blocks[58].getOccupancy() or blocks[59].getOccupancy())):
                blocks[57].setSignal(False)
            else:
                blocks[57].setSignal(True)

        #Switch J62 - J61 , J62 - Yard
        if(blocks[150].getOccupancy()):
            blocks[61].setSwitch(True)
        elif(blocks[60].getOccupancy()):
            blocks[61].setSwitch(False)
        #Signal yard
        if(blocks[150].getOccupancy() or blocks[61].getOccupancy() or blocks[62].getOccupancy()):
            if((blocks[150].getOccupancy()) and not(blocks[61].getOccupancy() or blocks[62].getOccupancy())):
                blocks[150].setSignal(False)
            else:
                blocks[150].setSignal(True)
        #Signal J61
        if(blocks[58].getOccupancy() or blocks[59].getOccupancy() or blocks[60].getOccupancy() or blocks[61].getOccupancy() or blocks[62].getOccupancy() or blocks[150].getOccupancy()):
            if((blocks[59].getOccupancy() or blocks[60].getOccupancy()) and not(blocks[61].getOccupancy() or blocks[62].getOccupancy() or blocks[150].getOccupancy())):
                blocks[60].setSignal(False)
            else:
                blocks[60].setSignal(True)

            
        #Switch N77 - R101 , N77 - M76
        if(blocks[77].getOccupancy() or loop1):
            blocks[76].setSwitch(False)
        elif(blocks[75].getOccupancy()):
            blocks[76].setSwitch(True)
        #Signal M76
        if(blocks[73].getOccupancy() or blocks[74].getOccupancy() or blocks[75].getOccupancy() or loop2):
            if((blocks[74].getOccupancy() or blocks[75].getOccupancy()) and not loop2):
                blocks[75].setSignal(False)
            else:
                blocks[75].setSignal(True)
        #Signal N77
        if(blocks[76].getOccupancy() or blocks[77].getOccupancy() or blocks[78].getOccupancy() or blocks[100].getOccupancy() or blocks[101].getOccupancy()):
            if((blocks[77].getOccupancy() or blocks[76].getOccupancy()) and not (blocks[100].getOccupancy() or blocks[101].getOccupancy())):
                blocks[76].setSignal(False)
            else:
                blocks[76].setSignal(True)

        #Switch N85 - O86 , N85 - Q100
        if(blocks[83].getOccupancy()):
            blocks[84].setSwitch(False)
        if(blocks[99].getOccupancy() and not (loop2)):
            blocks[84].setSwitch(True)
        #Signal N85
        if(blocks[82].getOccupancy() or blocks[83].getOccupancy() or blocks[84].getOccupancy() or blocks[85].getOccupancy() or blocks[86].getOccupancy()):
            if((blocks[83].getOccupancy() or blocks[84].getOccupancy()) and not (blocks[85].getOccupancy() or blocks[86].getOccupancy())):
                blocks[84].setSignal(False)
            else:
                blocks[84].setSignal(True)
        #Signal Q100
        if(blocks[97].getOccupancy() or blocks[98].getOccupancy() or blocks[99].getOccupancy() or blocks[84].getOccupancy() or blocks[83].getOccupancy() or blocks[82].getOccupancy()):
            if(blocks[98].getOccupancy or blocks[99].getOccupancy() and not (loop2)):
                blocks[99].setSignal(True)
            else:
                blocks[99].setSignal(False)

def plcc(blocks:Block = []):
    stoppage = []
    loop1 = False
    loop2 = False
    for i in range(12, 29):
        loop1 = loop1 or blocks[i].getOccupancy()
    for i in range(76, 85):
        loop2 = loop2 or blocks[i].getOccupancy()
    #Line
    for i in range(3, 15):
        if(blocks[i].getOccupancy()):
            if(blocks[i-1].getOccupancy() or blocks[i-2].getOccupancy()):
                stoppage.append(blocks[i].getName())
    for i in range(14, 148):
        if(blocks[i].getOccupancy()):
            if(blocks[i+1].getOccupancy() or blocks[i+2].getOccupancy() or blocks[i+3].getOccupancy()):
                stoppage.append(blocks[i].getName())
    #Signal A1
    if(blocks[0].getOccupancy() and loop1):
        stoppage.append(blocks[0].getName())
    if(blocks[1].getOccupancy() and loop1):
        stoppage.append(blocks[1].getName())
    if(blocks[2].getOccupancy() and loop1):
        stoppage.append(blocks[2].getName())

    #Signal Z150
    if(blocks[146].getOccupancy() and loop1):
        stoppage.append(blocks[146].getName())
    if(blocks[147].getOccupancy() and loop1):
        stoppage.append(blocks[147].getName())
    if(blocks[148].getOccupancy() and loop1):
        stoppage.append(blocks[148].getName())

    #Signal G29
    if(blocks[28].getOccupancy() and (blocks[29].getOccupancy() or blocks[30].getOccupancy())):
        stoppage.append(blocks[28].getName())
    if(blocks[27].getOccupancy() and (blocks[29].getOccupancy() or blocks[30].getOccupancy())):
        stoppage.append(blocks[27].getName())
    #Signal J58
    if(blocks[57].getOccupancy() and (blocks[58].getOccupancy() or blocks[59].getOccupancy())):
        stoppage.append(blocks[57].getName())
    if(blocks[56].getOccupancy() and (blocks[58].getOccupancy() or blocks[59].getOccupancy())):
        stoppage.append(blocks[56].getName())
    #Signal yard
    if(blocks[150].getOccupancy() and (blocks[61].getOccupancy() or blocks[62].getOccupancy())):
        stoppage.append(blocks[150].getName())
    #signal J61
    if(blocks[60].getOccupancy() and (blocks[61].getOccupancy() or blocks[62].getOccupancy() or blocks[150].getOccupancy())):
        stoppage.append(blocks[60].getName())
    if(blocks[59].getOccupancy() and (blocks[61].getOccupancy() or blocks[62].getOccupancy() or blocks[150].getOccupancy())):
        stoppage.append(blocks[59].getName())
    #Signal M76
    if(blocks[73].getOccupancy() and loop2):
        stoppage.append(blocks[73].getName())
    if(blocks[74].getOccupancy() and loop2):
        stoppage.append(blocks[74].getName())
    if(blocks[75].getOccupancy() and loop2):
        stoppage.append(blocks[75].getName())
    #N77
    if(blocks[76].getOccupancy() and (blocks[100].getOccupancy() or blocks[101].getOccupancy())):
        stoppage.append(blocks[76].getName())
    if(blocks[77].getOccupancy() and (blocks[100].getOccupancy() or blocks[101].getOccupancy())):
        stoppage.append(blocks[77].getName())
    #Signal Q100
    if(blocks[97].getOccupancy() and loop2):
        stoppage.append(blocks[97].getName())
    if(blocks[98].getOccupancy() and loop2):
        stoppage.append(blocks[98].getName())
    if(blocks[99].getOccupancy() and loop2):
        stoppage.append(blocks[99].getName())
    
    return stoppage