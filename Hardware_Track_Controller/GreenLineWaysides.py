from Hardware_Track_Controller.WaysideClass import Wayside
#from AuthorityClass import AuthorityClass

class GreenLine():

    Waysides = [Wayside(), Wayside(), Wayside(), Wayside()] #All The waysides going in order of 1,2,3,4 for Green Line

    def setTracks(self, tracks): #Creates the track on start up of program from Track Model
        switch = []
        crossroad = []
        light =[]
        trackName = []
        left = []
        right = []
        for i in range(len(tracks[0])):
            switch.append(tracks[0][i])
        for i in range(len(tracks[1])):
            crossroad.append(tracks[1][i])
        for i in range(len(tracks[2])):
            light.append(tracks[2][i])
        for i in range(len(tracks[3])):
            trackName.append(tracks[3][i])
        for i in range(len(tracks[4])):
            left.append(tracks[4][i])
        for i in range(len(tracks[5])):
            right.append(tracks[5][i])

        for i in range(len(tracks[0])):
            if(i <= 31): #Creates A1-G32
                self.Waysides[0].createTrack(switch[i], crossroad[i], light[i], trackName[i], left[i], right[i])
            if(31 < i <= 72): #Creates H33-L73
                self.Waysides[1].createTrack(switch[i], crossroad[i], light[i], trackName[i], left[i], right[i])
            if(72 < i <= 100): #Creates M74-R101
                self.Waysides[2].createTrack(switch[i], crossroad[i], light[i], trackName[i], left[i], right[i])
            if(100 < i <= 148): #Creates S102-Y149
                self.Waysides[3].createTrack(switch[i], crossroad[i], light[i], trackName[i], left[i], right[i])
        self.Waysides[0].createTrack(switch[149], crossroad[149], light[149], trackName[149], left[149], right[149])
        self.Waysides[1].createTrack(switch[150], crossroad[150], light[150], trackName[150], left[150], right[150])


    
    
    # def arrayOfTracks(self): #Creates a array of tracks for authority logic
    #     for i in range(32): #A1-G32
    #         self.trackList.append(self.Waysides[0].getTrack(i))
    #     #All for Wayside 2
    #     for i in range(41): #H33-L73
    #         self.trackList.append(self.Waysides[1].getTrack(i))
    #     #All for Wayside 3
    #     for i in range(28): #M74-R101
    #         self.trackList.append(self.Waysides[2].getTrack(i))
    #     #All for Wayside 4
    #     for i in range(48): #S102-Y149
    #         self.trackList.append(self.Waysides[3].getTrack(i))
    #     self.trackList.append(self.Waysides[0].getTrack(32)) #Z150
    #     self.trackList.append(self.Waysides[1].getTrack(41)) #Z151/YARD
    
    
    #Configuration of all tracks in Green Line Waysides - THIS IS FOR TESTING PERSONALLY ONLY
    #switch:bool, crossroad:bool, light:bool, trackName:str, left = "", right = ""
    #Wayside 1
    # Waysides[0].createTrack(False, False, True, "A1") #A1 [0]
    # Waysides[0].createTrack(False, False, False, "A2") #A2 [1]
    # Waysides[0].createTrack(False, False, False, "A3") #A3 [2]
    # Waysides[0].createTrack(False, False, False, "B4") #B4 [3]
    # Waysides[0].createTrack(False, False, False, "B5") #B5 [4]
    # Waysides[0].createTrack(False, False, False, "B6") #B6 [5]
    # Waysides[0].createTrack(False, False, False, "C7") #C7 [6]
    # Waysides[0].createTrack(False, False, False, "C8") #C8 [7]
    # Waysides[0].createTrack(False, False, False, "C9") #C9 [8]
    # Waysides[0].createTrack(False, False, False, "C10") #C10 [9]
    # Waysides[0].createTrack(False, False, False, "C11") #C11 [10]
    # Waysides[0].createTrack(False, False, False, "C12") #C12 [11]
    # Waysides[0].createTrack(True, False, True, "D13", "C12", "A1") #D13 [12]
    # Waysides[0].createTrack(False, False, False, "D14") #D14 [13]
    # Waysides[0].createTrack(False, False, False, "D15") #D15 [14]
    # Waysides[0].createTrack(False, False, False, "D16") #D16 [15]
    # Waysides[0].createTrack(False, False, False, "E17") #E17 [16]
    # Waysides[0].createTrack(False, False, False, "E18") #E18 [17]
    # Waysides[0].createTrack(False, True, False, "E19") #E19 [18]
    # Waysides[0].createTrack(False, False, False, "E20") #E20 [19]
    # Waysides[0].createTrack(False, False, False, "F21") #F21 [20]
    # Waysides[0].createTrack(False, False, False, "F22") #F22 [21]
    # Waysides[0].createTrack(False, False, False, "F23") #F23 [22]
    # Waysides[0].createTrack(False, False, False, "F24") #F24 [23]
    # Waysides[0].createTrack(False, False, False, "F25") #F25 [24]
    # Waysides[0].createTrack(False, False, False, "F26") #F26 [25]
    # Waysides[0].createTrack(False, False, False, "F27") #F27 [26]
    # Waysides[0].createTrack(False, False, False, "F28") #F28 [27]
    # Waysides[0].createTrack(True, False, True, "G29", "G30", "Z150") #G29 [28]
    # Waysides[0].createTrack(False, False, False, "G30") #G30 [29]
    # Waysides[0].createTrack(False, False, False, "G31") #G31 [30]
    # Waysides[0].createTrack(False, False, False, "G32") #G32 [31]
    # Waysides[0].createTrack(False, False, True, "Z150") #Z150 [32]
    # #Wayside 2
    # Waysides[1].createTrack(False, False, False, "H33") #H33 [0]
    # Waysides[1].createTrack(False, False, False, "H34") #H34 [1]
    # Waysides[1].createTrack(False, False, False, "H35") #H35 [2]
    # Waysides[1].createTrack(False, False, False, "I36") #I36 [3]
    # Waysides[1].createTrack(False, False, False, "I37") #I37 [4]
    # Waysides[1].createTrack(False, False, False, "I38") #I38 [5]
    # Waysides[1].createTrack(False, False, False, "I39") #I39 [6]
    # Waysides[1].createTrack(False, False, False, "I40") #I40 [7]
    # Waysides[1].createTrack(False, False, False, "I41") #I41 [8]
    # Waysides[1].createTrack(False, False, False, "I42") #I42 [9]
    # Waysides[1].createTrack(False, False, False, "I43") #I43 [10]
    # Waysides[1].createTrack(False, False, False, "I44") #I44 [11]
    # Waysides[1].createTrack(False, False, False, "I45") #I45 [12]
    # Waysides[1].createTrack(False, False, False, "I46") #I46 [13]
    # Waysides[1].createTrack(False, False, False, "I47") #I47 [14]
    # Waysides[1].createTrack(False, False, False, "I48") #I48 [15]
    # Waysides[1].createTrack(False, False, False, "I49") #I49 [16]
    # Waysides[1].createTrack(False, False, False, "I50") #I50 [17]
    # Waysides[1].createTrack(False, False, False, "I51") #I51 [18]
    # Waysides[1].createTrack(False, False, False, "I52") #I52 [19]
    # Waysides[1].createTrack(False, False, False, "I53") #I53 [20]
    # Waysides[1].createTrack(False, False, False, "I54") #I54 [21]
    # Waysides[1].createTrack(False, False, False, "I55") #I55 [22]
    # Waysides[1].createTrack(False, False, False, "I56") #I56 [23]
    # Waysides[1].createTrack(False, False, False, "I57") #I57 [24]
    # Waysides[1].createTrack(True, False, True, "J58","Z151", "J59") #J58 [25]
    # Waysides[1].createTrack(False, False, False, "J59") #J59 [26]
    # Waysides[1].createTrack(False, False, False, "J60") #J60 [27]
    # Waysides[1].createTrack(False, False, True, "J61") #J61 [28]
    # Waysides[1].createTrack(True, False, False, "J62","J61", "Z151") #J62 [29]
    # Waysides[1].createTrack(False, False, False, "K63") #K63 [30]
    # Waysides[1].createTrack(False, False, False, "K64") #K64 [31]
    # Waysides[1].createTrack(False, False, False, "K65") #K65 [32]
    # Waysides[1].createTrack(False, False, False, "K66") #K66 [33]
    # Waysides[1].createTrack(False, False, False, "K67") #K67 [34]
    # Waysides[1].createTrack(False, False, False, "K68") #K68 [35]
    # Waysides[1].createTrack(False, False, False, "L69") #L69 [36]
    # Waysides[1].createTrack(False, False, False, "L70") #L70 [37]
    # Waysides[1].createTrack(False, False, False, "L71") #L71 [38]
    # Waysides[1].createTrack(False, False, False, "L72") #L72 [39]
    # Waysides[1].createTrack(False, False, False, "L73") #L73 [40]
    # Waysides[1].createTrack(False, False, True, "Z151") #Z151/YARD [41]
    # #Wayside 3
    # Waysides[2].createTrack(False, False, False, "M74") #M74 [0]
    # Waysides[2].createTrack(False, False, False, "M75") #M75 [1]
    # Waysides[2].createTrack(False, False, True, "M76") #M76 [2]
    # Waysides[2].createTrack(True, False, True, "N77", "R101", "M76") #N77 [3]
    # Waysides[2].createTrack(False, False, False, "N78") #N78 [4]
    # Waysides[2].createTrack(False, False, False, "N79") #N79 [5]
    # Waysides[2].createTrack(False, False, False, "N80") #N80 [6]
    # Waysides[2].createTrack(False, False, False, "N81") #N81 [7]
    # Waysides[2].createTrack(False, False, False, "N82") #N82 [8]
    # Waysides[2].createTrack(False, False, False, "N83") #N83 [9]
    # Waysides[2].createTrack(False, False, False, "N84") #N84 [10]
    # Waysides[2].createTrack(True, False, True, "N85", "O86", "Q100") #N85 [11]
    # Waysides[2].createTrack(False, False, False, "O86") #O86 [12]
    # Waysides[2].createTrack(False, False, False, "O87") #O87 [13]
    # Waysides[2].createTrack(False, False, False, "O88") #O88 [14]
    # Waysides[2].createTrack(False, False, False, "P89") #P89 [15]
    # Waysides[2].createTrack(False, False, False, "P90") #P90 [16]
    # Waysides[2].createTrack(False, False, False, "P91") #P91 [17]
    # Waysides[2].createTrack(False, False, False, "P92") #P92 [18]
    # Waysides[2].createTrack(False, False, False, "P93") #P93 [19]
    # Waysides[2].createTrack(False, False, False, "P94") #P94 [20]
    # Waysides[2].createTrack(False, False, False, "P95") #P95 [21]
    # Waysides[2].createTrack(False, False, False, "P96") #P96 [22]
    # Waysides[2].createTrack(False, False, False, "P97") #P97 [23]
    # Waysides[2].createTrack(False, False, False, "Q98") #Q98 [24]
    # Waysides[2].createTrack(False, False, False, "Q99") #Q99 [25]
    # Waysides[2].createTrack(False, False, True, "Q100") #Q100 [26]
    # Waysides[2].createTrack(False, False, False, "R101") #R101 [27]
    # #Wayside 4
    # Waysides[3].createTrack(False, False, False, "S102") #S102 [0]
    # Waysides[3].createTrack(False, False, False, "S103") #S103 [1]
    # Waysides[3].createTrack(False, False, False, "S104") #S104 [2]
    # Waysides[3].createTrack(False, False, False, "T105") #T105 [3]
    # Waysides[3].createTrack(False, False, False, "T106") #T106 [4]
    # Waysides[3].createTrack(False, False, False, "T107") #T107 [5]
    # Waysides[3].createTrack(False, False, False, "T108") #T108 [6]
    # Waysides[3].createTrack(False, False, False, "T109") #T109 [7]
    # Waysides[3].createTrack(False, False, False, "U110") #U110 [8]
    # Waysides[3].createTrack(False, False, False, "U111") #U111 [9]
    # Waysides[3].createTrack(False, False, False, "U112") #U112 [10]
    # Waysides[3].createTrack(False, False, False, "U113") #U113 [11]
    # Waysides[3].createTrack(False, False, False, "U114") #U114 [12]
    # Waysides[3].createTrack(False, False, False, "U115") #U115 [13]
    # Waysides[3].createTrack(False, False, False, "U116") #U116 [14]
    # Waysides[3].createTrack(False, False, False, "V117") #V117 [15]
    # Waysides[3].createTrack(False, False, False, "V118") #V118 [16]
    # Waysides[3].createTrack(False, False, False, "V119") #V119 [17]
    # Waysides[3].createTrack(False, False, False, "V120") #V120 [18]
    # Waysides[3].createTrack(False, False, False, "V121") #V121 [19]
    # Waysides[3].createTrack(False, False, False, "W122") #W122 [20]
    # Waysides[3].createTrack(False, False, False, "W123") #W123 [21]
    # Waysides[3].createTrack(False, False, False, "W124") #W124 [22]
    # Waysides[3].createTrack(False, False, False, "W125") #W125 [23]
    # Waysides[3].createTrack(False, False, False, "W126") #W126 [24]
    # Waysides[3].createTrack(False, False, False, "W127") #W127 [25]
    # Waysides[3].createTrack(False, False, False, "W128") #W128 [26]
    # Waysides[3].createTrack(False, False, False, "W129") #W129 [27]
    # Waysides[3].createTrack(False, False, False, "W130") #W130 [28]
    # Waysides[3].createTrack(False, False, False, "W131") #W131 [29]
    # Waysides[3].createTrack(False, False, False, "W132") #W132 [30]
    # Waysides[3].createTrack(False, False, False, "W133") #W133 [31]
    # Waysides[3].createTrack(False, False, False, "W134") #W134 [32]
    # Waysides[3].createTrack(False, False, False, "W135") #W135 [33]
    # Waysides[3].createTrack(False, False, False, "W136") #W136 [34]
    # Waysides[3].createTrack(False, False, False, "W137") #W137 [35]
    # Waysides[3].createTrack(False, False, False, "W138") #W138 [36]
    # Waysides[3].createTrack(False, False, False, "W139") #W139 [37]
    # Waysides[3].createTrack(False, False, False, "W140") #W140 [38]
    # Waysides[3].createTrack(False, False, False, "W141") #W141 [39]
    # Waysides[3].createTrack(False, False, False, "W142") #W142 [40]
    # Waysides[3].createTrack(False, False, False, "W143") #W143 [41]
    # Waysides[3].createTrack(False, False, False, "X144") #X144 [42]
    # Waysides[3].createTrack(False, False, False, "X145") #X145 [43]
    # Waysides[3].createTrack(False, False, False, "X146") #X146 [44]
    # Waysides[3].createTrack(False, False, False, "Y147") #Y147 [45]
    # Waysides[3].createTrack(False, False, False, "Y148") #Y148 [46]
    # Waysides[3].createTrack(False, False, False, "Y149") #Y149 [47]