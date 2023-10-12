from PyQt6.QtWidgets import QApplication, QComboBox, QMainWindow, QFileDialog
from PyQt6 import QtCore, QtGui, QtWidgets
import pandas as pd
from customUI import Ui_MainWindow

## TO CONVERT UI TO PY
# open terminal at folder with ui
# pyuic6 -x -o test.py mainwindow.ui
#profit
#################

#comboBox_4 = Block box
# comboBox_3 = Line Box

class line():
    def __init__(self,name):
        self.name = name
        self.blocks = []
    def addBlock(self,blk):
        self.blocks.append(blk)

class block():
    def __init__(self,name):
        self.name = name
        self.occupied = False
        # self.line = attributes[0] #string
        # self.name = attributes[1] #string
        # self.occupied = attributes[2] #bool
        # self.length = attributes[3] #double
        # self.grade = attributes[4]  #double
        # self.elevation = attributes[5] #double
        # self.limit = attributes[6] #double
        # self.station = attributes[7] #bool
        # self.switch = attributes[8] #bool
        # self.underground = attributes[9] #bool
        # self.crossroad = attributes[10] #bool
        # self.heater = attributes[11] #bool
        # self.failure = attributes[12] #bool
    def setOccupied(self):
        self.occupied = True
    def clearOccupied(self):
        self.occupied = False
    def setLength(self,length):
        self.length = length
    def setGrade(self,grade):
        self.grade = grade
    def setLimit(self,limit):
        self.limit = limit
    def setElevation(self, elevation):
        self.elevation = elevation

#debug array


metersToFeet = 3.28084
kmhrTomihr = 0.621371



class functionalUI(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.lines = []
        self.occupied_debug = []


    def update(self):
        self.comboBox_3.activated.connect(self.lineChange)
        self.comboBox_4.currentIndexChanged.connect(self.blockChange)
        self.pushButton_2.clicked.connect(self.buttonPress)
        self.lineEdit.returnPressed.connect(self.tbChange)
        self.updateOccupancy()


        # #tb
        # self.comboBox_5.activated.connect(self.lineChange)
        # self.comboBox_6.currentIndexChanged.connect(self.blockChange)

    def tbChange(self):
        tbInfo = self.lineEdit.displayText().split(',')
    
        for l in self.lines:
            if(l.name == tbInfo[0]):
                break

        tbInfo.pop(0)

        self.occupied_debug += tbInfo
        self.updateOccupancy()

    def lineChange(self):
        #Clear the Blocks
        self.comboBox_4.clear()
        self.listWidget_2.clear()

        # #tb
        # self.comboBox_6.clear()


        # Add the blocks associated with that line
        currentLineName = self.comboBox_3.currentText()

        for l in self.lines:
            if(l.name == currentLineName):
                for blk in l.blocks:
                    self.comboBox_4.addItem(blk.name)
                    if(blk.occupied):
                        self.listWidget_2.addItem(blk.name)
                    # #tb
                    # self.comboBox_6.addItem(blk.name)


                


    def blockChange(self):
        currentBlockName = self.comboBox_4.currentText()
        currentLineName = self.comboBox_3.currentText()
        # tbLineName = self.comboBox_5.currentText()
        # tbBlockName = self.comboBox_6.currentText()

        for l in self.lines:
            if(l.name == currentLineName):
                break

        for b in l.blocks:
            if (b.name == currentBlockName):
                break

        # for tbl in self.lines:
        #     if tbl.name == tbLineName:
        #         break
        
        # for tbb in tbl.blocks:
        #     if tbb.name == tbBlockName:
        #         break

        #name
        self.tableWidget_3.item(0,0).setText(currentBlockName)
        #occupancy
        if(b.occupied):
            self.tableWidget_3.item(1,0).setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.tableWidget_3.item(1,0).setCheckState(QtCore.Qt.CheckState.Unchecked)
        #length
        self.tableWidget_3.item(2,0).setText(str(round(b.length * metersToFeet,3)) +" feet")
        #grade
        self.tableWidget_3.item(3,0).setText(str(b.grade) + "%")
        #elevation
        self.tableWidget_3.item(4,0).setText(str(round(b.elevation*metersToFeet,3)) + " feet")
        #limit
        self.tableWidget_3.item(5,0).setText(str(round(b.limit*kmhrTomihr,3)) + " mi/hr")


        # #tb
        # #name
        # self.tableWidget_4.item(0,0).setText(tbBlockName)
        # #occupancy
        # if(self.tableWidget_4.item(1,0).checkState() == QtCore.Qt.CheckState.Checked):
        #     l.occupied += tbb.name
        # #length
        # self.tableWidget_4.item(2,0).setText(str(round(tbb.length * metersToFeet,3)) +" feet")
        # #grade
        # self.tableWidget_4.item(3,0).setText(str(tbb.grade) + "%")
        # #elevation
        # self.tableWidget_4.item(4,0).setText(str(round(tbb.elevation*metersToFeet,3)) + " feet")
        # #limit
        # self.tableWidget_4.item(5,0).setText(str(round(tbb.limit*kmhrTomihr,3)) + " mi/hr")
    

    def buttonPress(self):
        fd = QFileDialog()
        path, _ = fd.getOpenFileName(None, 'Select a file:')
        db = pd.read_csv(path)
        numOfRows = len(db.index)

        #instantiate line:
        newLine = line(db.at[0,"Line"] + " Line")

        #Instantiate Blocks
        for i in range(numOfRows):
            if(not (db.isna().at[i,"Section"])):
                name = db.at[i,"Section"]+str(int(db.at[i, "Block Number"]))
                length = db.at[i,"Block Length (m)"]
                grade = db.at[i,"Block Grade (%)"]
                limit = db.at[i,"Speed Limit (Km/Hr)"]
                elevation = db.at[i,"ELEVATION (M)"]


                blk = block(name)
                blk.setElevation(elevation)
                blk.setLimit(limit)
                blk.setLength(length)
                blk.setGrade(grade)
                newLine.addBlock(blk)
        

        self.comboBox_3.addItem(newLine.name)

        # #tb
        # self.comboBox_5.addItem(newLine.name)

        self.lines.append(newLine)

        self.updateOccupancy()

    def updateOccupancy(self):
        for line in self.lines:
            for blk in line.blocks:
                if (blk.name in self.occupied_debug):
                    blk.setOccupied()
                else:
                    blk.clearOccupied()




app = QApplication([])
MainWindow = QMainWindow()
ui = functionalUI()
ui.setupUi(MainWindow)
ui.update()
MainWindow.show()
# # Start the event loop.
app.exec()