from PyQt6.QtWidgets import QApplication, QComboBox, QMainWindow, QFileDialog
from PyQt6 import QtCore, QtGui, QtWidgets
import pandas as pd
from customUI import Ui_MainWindow


# Only needed for access to command line arguments


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.

## TO CONVERT UI TO PY
# open terminal at folder with ui
# pyuic6 -x -o test.py mainwindow.ui
#profit
#################

#comboBox = Block box
# comboBox_2 = Line Box

class line():
    def __init__(self,name):
        self.name = name
        self.blocks = []
        self.occupied = []
    def addBlock(self,blk):
        self.blocks.append(blk)
    def addOccupied(self, blk_name):
        self.occupied.append(blk_name)
    def addOccupiedList(self,blkname_list):
        self.occupied += blkname_list

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
    def toggleOccupied(self):
        self.occupied = not self.occupied
    def setLength(self,length):
        self.length = length
    def setGrade(self,grade):
        self.grade = grade
    def setLimit(self,limit):
        self.limit = limit
    def setElevation(self, elevation):
        self.elevation = elevation

occupied_debug = ["A2","E13","H33","H25", "R72"] #debug array


metersToFeet = 3.28084
kmhrTomihr = 0.621371



class functionalUI(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.lines = []

    def update(self):

        self.comboBox_2.activated.connect(self.lineChange)
        self.comboBox.currentIndexChanged.connect(self.blockChange)
        self.pushButton.clicked.connect(self.buttonPress)



    def lineChange(self):
        #Clear the Blocks
        self.comboBox.clear()

        # Add the blocks associated with that line
        currentLineName = self.comboBox_2.currentText()

        for l in self.lines:
            if(l.name == currentLineName):
                for blk in l.blocks:
                    self.comboBox.addItem(blk.name)

                self.listWidget.clear()
                self.listWidget.addItems(l.occupied)


                


    def blockChange(self):
        currentBlockName = self.comboBox.currentText()
        currentLineName = self.comboBox_2.currentText()

        for l in self.lines:
            if(l.name == currentLineName):
                break

        for b in l.blocks:
            if (b.name == currentBlockName):
                break

        #name
        self.tableWidget.item(0,0).setText(currentBlockName)
        #occupancy
        if(b.occupied):
            self.tableWidget.item(1,0).setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.tableWidget.item(1,0).setCheckState(QtCore.Qt.CheckState.Unchecked)
        #length
        self.tableWidget.item(2,0).setText(str(round(b.length * metersToFeet,3)) +" feet")
        #grade
        self.tableWidget.item(3,0).setText(str(b.grade) + "%")
        #elevation
        self.tableWidget.item(4,0).setText(str(round(b.elevation*metersToFeet,3)) + " feet")
        #limit
        self.tableWidget.item(5,0).setText(str(round(b.limit*kmhrTomihr,3)) + " mi/hr")
    

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
    
        #Set self.occupied values
        for x in newLine.blocks:
            if(x.name in occupied_debug):
                newLine.addOccupied(x.name)
                x.toggleOccupied()
        

        self.comboBox_2.addItem(newLine.name)
        self.lines.append(newLine)


        
        
        


        

    


# app = QApplication([])

# # Create a Qt widget, which will be our window.

# class MainScreen(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Track Model")

#     def initDropdown(self):
#         dropdown = QComboBox()
#         # dropdown.addItems([List of Block names])
#         dropdown.addItem("Option 1")
#         dropdown.addItem("Option 2")
#         dropdown.activated.connect(self.update)
#         self.setCentralWidget(dropdown)

#     def update(self):
#         pass
        


# window = MainScreen()
# window.initDropdown()

# window.show()  # IMPORTANT!!!!! Windows are hidden by default.

app = QApplication([])
MainWindow = QMainWindow()
ui = functionalUI()
ui.setupUi(MainWindow)
ui.update()
MainWindow.show()
# # Start the event loop.
app.exec()