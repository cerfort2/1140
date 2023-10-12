# Form implementation generated from reading ui file 'TrackController.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QTableWidgetItem

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(898, 779)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QLabel(parent=self.centralwidget)
        self.name.setGeometry(QtCore.QRect(10, 0, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.name.setFont(font)
        self.name.setLineWidth(1)
        self.name.setMidLineWidth(0)
        self.name.setObjectName("name")
        self.pageSelection = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.pageSelection.setGeometry(QtCore.QRect(10, 50, 881, 691))
        self.pageSelection.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.pageSelection.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.pageSelection.setTabShape(QtWidgets.QTabWidget.TabShape.Triangular)
        self.pageSelection.setProperty("Sections", 2)
        self.pageSelection.setObjectName("pageSelection")
        self.mainPage = QtWidgets.QWidget()
        self.mainPage.setObjectName("mainPage")
        self.section = QtWidgets.QComboBox(parent=self.mainPage)
        self.section.setGeometry(QtCore.QRect(30, 10, 101, 22))
        self.section.setObjectName("section")
        self.section.addItem("")
        self.section.addItem("")
        self.section.addItem("")
        self.switchFrame = QtWidgets.QFrame(parent=self.mainPage)
        self.switchFrame.setGeometry(QtCore.QRect(430, 40, 351, 271))
        self.switchFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.switchFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.switchFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.switchFrame.setObjectName("switchFrame")
        self.switchDirection = QtWidgets.QLabel(parent=self.switchFrame)
        self.switchDirection.setGeometry(QtCore.QRect(120, 90, 131, 131))
        self.switchDirection.setObjectName("switchDirection")
        self.toggleDirection = QtWidgets.QPushButton(parent=self.switchFrame)
        self.toggleDirection.setGeometry(QtCore.QRect(130, 30, 101, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.toggleDirection.setFont(font)
        self.toggleDirection.setObjectName("toggleDirection")
        self.switchSelect = QtWidgets.QComboBox(parent=self.switchFrame)
        self.switchSelect.setGeometry(QtCore.QRect(0, 0, 101, 22))
        self.switchSelect.setObjectName("switchSelect")
        self.switchSelect.addItem("")
        self.leftSection = QtWidgets.QLabel(parent=self.switchFrame)
        self.leftSection.setGeometry(QtCore.QRect(10, 140, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.leftSection.setFont(font)
        self.leftSection.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.leftSection.setLineWidth(1)
        self.leftSection.setMidLineWidth(0)
        self.leftSection.setObjectName("leftSection")
        self.rightSection = QtWidgets.QLabel(parent=self.switchFrame)
        self.rightSection.setGeometry(QtCore.QRect(250, 140, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rightSection.setFont(font)
        self.rightSection.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.rightSection.setLineWidth(1)
        self.rightSection.setMidLineWidth(0)
        self.rightSection.setObjectName("rightSection")
        self.crossroadFrame = QtWidgets.QFrame(parent=self.mainPage)
        self.crossroadFrame.setGeometry(QtCore.QRect(20, 340, 351, 271))
        self.crossroadFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.crossroadFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.crossroadFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.crossroadFrame.setObjectName("crossroadFrame")
        self.crossroadStatus = QtWidgets.QLabel(parent=self.crossroadFrame)
        self.crossroadStatus.setGeometry(QtCore.QRect(90, 70, 161, 161))
        self.crossroadStatus.setObjectName("crossroadStatus")
        self.toggleCrossroad = QtWidgets.QPushButton(parent=self.crossroadFrame)
        self.toggleCrossroad.setGeometry(QtCore.QRect(130, 20, 101, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.toggleCrossroad.setFont(font)
        self.toggleCrossroad.setObjectName("toggleCrossroad")
        self.crossroadSelect = QtWidgets.QComboBox(parent=self.crossroadFrame)
        self.crossroadSelect.setGeometry(QtCore.QRect(0, 0, 101, 22))
        self.crossroadSelect.setObjectName("crossroadSelect")
        self.crossroadSelect.addItem("")
        self.signalFrame = QtWidgets.QFrame(parent=self.mainPage)
        self.signalFrame.setGeometry(QtCore.QRect(430, 340, 351, 271))
        self.signalFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.signalFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.signalFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.signalFrame.setObjectName("signalFrame")
        self.greenButton = QtWidgets.QPushButton(parent=self.signalFrame)
        self.greenButton.setGeometry(QtCore.QRect(50, 50, 75, 24))
        self.greenButton.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.greenButton.setObjectName("greenButton")
        self.redButton = QtWidgets.QPushButton(parent=self.signalFrame)
        self.redButton.setGeometry(QtCore.QRect(50, 160, 75, 24))
        self.redButton.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.redButton.setObjectName("redButton")
        self.signalState = QtWidgets.QPushButton(parent=self.signalFrame)
        self.signalState.setGeometry(QtCore.QRect(210, 50, 91, 131))
        font = QtGui.QFont()
        font.setBold(True)
        self.signalState.setFont(font)
        self.signalState.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.signalState.setAutoDefault(False)
        self.signalState.setObjectName("signalState")
        self.signalSelect = QtWidgets.QComboBox(parent=self.signalFrame)
        self.signalSelect.setGeometry(QtCore.QRect(0, 0, 101, 22))
        self.signalSelect.setObjectName("signalSelect")
        self.signalSelect.addItem("")
        self.modeButton = QtWidgets.QRadioButton(parent=self.mainPage)
        self.modeButton.setGeometry(QtCore.QRect(660, 10, 121, 20))
        self.modeButton.setObjectName("modeButton")
        self.dataFrame = QtWidgets.QFrame(parent=self.mainPage)
        self.dataFrame.setGeometry(QtCore.QRect(20, 40, 351, 271))
        self.dataFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dataFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.dataFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.dataFrame.setObjectName("dataFrame")
        self.sectionData = QtWidgets.QLabel(parent=self.dataFrame)
        self.sectionData.setGeometry(QtCore.QRect(100, 10, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sectionData.setFont(font)
        self.sectionData.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.sectionData.setLineWidth(1)
        self.sectionData.setMidLineWidth(0)
        self.sectionData.setObjectName("sectionData")
        self.secLab = QtWidgets.QLabel(parent=self.dataFrame)
        self.secLab.setGeometry(QtCore.QRect(0, 0, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.secLab.setFont(font)
        self.secLab.setLineWidth(1)
        self.secLab.setMidLineWidth(0)
        self.secLab.setObjectName("secLab")
        self.occupationData = QtWidgets.QLabel(parent=self.dataFrame)
        self.occupationData.setGeometry(QtCore.QRect(100, 40, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.occupationData.setFont(font)
        self.occupationData.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.occupationData.setLineWidth(1)
        self.occupationData.setMidLineWidth(0)
        self.occupationData.setObjectName("occupationData")
        self.occLab = QtWidgets.QLabel(parent=self.dataFrame)
        self.occLab.setGeometry(QtCore.QRect(0, 30, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.occLab.setFont(font)
        self.occLab.setLineWidth(1)
        self.occLab.setMidLineWidth(0)
        self.occLab.setObjectName("occLab")
        self.failData = QtWidgets.QLabel(parent=self.dataFrame)
        self.failData.setGeometry(QtCore.QRect(100, 70, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.failData.setFont(font)
        self.failData.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.failData.setLineWidth(1)
        self.failData.setMidLineWidth(0)
        self.failData.setObjectName("failData")
        self.faiLab = QtWidgets.QLabel(parent=self.dataFrame)
        self.faiLab.setGeometry(QtCore.QRect(0, 60, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.faiLab.setFont(font)
        self.faiLab.setLineWidth(1)
        self.faiLab.setMidLineWidth(0)
        self.faiLab.setObjectName("faiLab")
        self.nextStation = QtWidgets.QLabel(parent=self.mainPage)
        self.nextStation.setGeometry(QtCore.QRect(410, 10, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nextStation.setFont(font)
        self.nextStation.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.nextStation.setLineWidth(1)
        self.nextStation.setMidLineWidth(0)
        self.nextStation.setObjectName("nextStation")
        self.stattext = QtWidgets.QLabel(parent=self.mainPage)
        self.stattext.setGeometry(QtCore.QRect(310, 0, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stattext.setFont(font)
        self.stattext.setLineWidth(1)
        self.stattext.setMidLineWidth(0)
        self.stattext.setObjectName("stattext")
        self.switchFrame.raise_()
        self.section.raise_()
        self.crossroadFrame.raise_()
        self.signalFrame.raise_()
        self.modeButton.raise_()
        self.dataFrame.raise_()
        self.nextStation.raise_()
        self.stattext.raise_()
        self.pageSelection.addTab(self.mainPage, "")
        self.testBench = QtWidgets.QWidget()
        self.testBench.setObjectName("testBench")
        self.dataTB = QtWidgets.QTableWidget(parent=self.testBench)
        self.dataTB.setGeometry(QtCore.QRect(30, 50, 331, 211))
        self.dataTB.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dataTB.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.dataTB.setLineWidth(2)
        self.dataTB.setMidLineWidth(2)
        self.dataTB.setObjectName("dataTB")
        self.dataTB.setColumnCount(1)
        self.dataTB.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.dataTB.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTB.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTB.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTB.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTB.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTB.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTB.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTB.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTB.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTB.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTB.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTB.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTB.setItem(5, 0, item)
        self.dataTB.horizontalHeader().setCascadingSectionResizes(False)
        self.dataTB.horizontalHeader().setDefaultSectionSize(210)
        self.dataTB.horizontalHeader().setMinimumSectionSize(39)
        self.sectionTB = QtWidgets.QComboBox(parent=self.testBench)
        self.sectionTB.setGeometry(QtCore.QRect(30, 10, 101, 22))
        self.sectionTB.setObjectName("sectionTB")
        self.sectionTB.addItem("")
        self.sectionTB.addItem("")
        self.sectionTB.addItem("")
        self.switchTB = QtWidgets.QFrame(parent=self.testBench)
        self.switchTB.setGeometry(QtCore.QRect(430, 40, 351, 71))
        self.switchTB.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.switchTB.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.switchTB.setObjectName("switchTB")
        self.switchSelectTB = QtWidgets.QComboBox(parent=self.switchTB)
        self.switchSelectTB.setGeometry(QtCore.QRect(0, 0, 101, 22))
        self.switchSelectTB.setObjectName("switchSelectTB")
        self.switchSelectTB.addItem("")
        self.stattext_4 = QtWidgets.QLabel(parent=self.switchTB)
        self.stattext_4.setGeometry(QtCore.QRect(40, 30, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stattext_4.setFont(font)
        self.stattext_4.setLineWidth(1)
        self.stattext_4.setMidLineWidth(0)
        self.stattext_4.setObjectName("stattext_4")
        self.switchStatusTB = QtWidgets.QComboBox(parent=self.switchTB)
        self.switchStatusTB.setGeometry(QtCore.QRect(140, 40, 101, 22))
        self.switchStatusTB.setObjectName("switchStatusTB")
        self.switchStatusTB.addItem("")
        self.switchStatusTB.addItem("")
        self.crossroadTB = QtWidgets.QFrame(parent=self.testBench)
        self.crossroadTB.setGeometry(QtCore.QRect(20, 340, 351, 71))
        self.crossroadTB.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.crossroadTB.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.crossroadTB.setObjectName("crossroadTB")
        self.crossroadSelectTB = QtWidgets.QComboBox(parent=self.crossroadTB)
        self.crossroadSelectTB.setGeometry(QtCore.QRect(0, 0, 101, 22))
        self.crossroadSelectTB.setObjectName("crossroadSelectTB")
        self.crossroadSelectTB.addItem("")
        self.stattext_3 = QtWidgets.QLabel(parent=self.crossroadTB)
        self.stattext_3.setGeometry(QtCore.QRect(30, 30, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stattext_3.setFont(font)
        self.stattext_3.setLineWidth(1)
        self.stattext_3.setMidLineWidth(0)
        self.stattext_3.setObjectName("stattext_3")
        self.crossroadStatusTB = QtWidgets.QComboBox(parent=self.crossroadTB)
        self.crossroadStatusTB.setGeometry(QtCore.QRect(160, 40, 101, 22))
        self.crossroadStatusTB.setObjectName("crossroadStatusTB")
        self.crossroadStatusTB.addItem("")
        self.crossroadStatusTB.addItem("")
        self.signalTB = QtWidgets.QFrame(parent=self.testBench)
        self.signalTB.setGeometry(QtCore.QRect(430, 340, 351, 71))
        self.signalTB.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.signalTB.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.signalTB.setObjectName("signalTB")
        self.signalSelectTB = QtWidgets.QComboBox(parent=self.signalTB)
        self.signalSelectTB.setGeometry(QtCore.QRect(0, 0, 101, 22))
        self.signalSelectTB.setObjectName("signalSelectTB")
        self.signalSelectTB.addItem("")
        self.stattext_5 = QtWidgets.QLabel(parent=self.signalTB)
        self.stattext_5.setGeometry(QtCore.QRect(40, 30, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stattext_5.setFont(font)
        self.stattext_5.setLineWidth(1)
        self.stattext_5.setMidLineWidth(0)
        self.stattext_5.setObjectName("stattext_5")
        self.signalStatusTB = QtWidgets.QComboBox(parent=self.signalTB)
        self.signalStatusTB.setGeometry(QtCore.QRect(140, 40, 101, 22))
        self.signalStatusTB.setObjectName("signalStatusTB")
        self.signalStatusTB.addItem("")
        self.signalStatusTB.addItem("")
        self.applyTB = QtWidgets.QPushButton(parent=self.testBench)
        self.applyTB.setGeometry(QtCore.QRect(330, 450, 131, 71))
        self.applyTB.setObjectName("applyTB")
        self.stattext_2 = QtWidgets.QLabel(parent=self.testBench)
        self.stattext_2.setGeometry(QtCore.QRect(310, 0, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stattext_2.setFont(font)
        self.stattext_2.setLineWidth(1)
        self.stattext_2.setMidLineWidth(0)
        self.stattext_2.setObjectName("stattext_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.testBench)
        self.lineEdit.setGeometry(QtCore.QRect(410, 10, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.pageSelection.addTab(self.testBench, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 898, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.pageSelection.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ######################################################################################## 

        #Set up images and texts
        pixmap = QPixmap("1140\TrackControllerSw\left.jpg")
        self.switchDirection.setPixmap(pixmap)
        pixmap = QPixmap("1140\TrackControllerSw\crosso.jpg")
        self.crossroadStatus.setPixmap(pixmap)
        self.leftSection.setText("Section 6-10")
        self.rightSection.setText("Section 11-15")
        self.section.setItemText(0, "Section 1-5")
        self.section.setItemText(1, "Section 6-10")
        self.section.setItemText(2, "Section 11-15")
        self.sectionTB.setItemText(0, "Section 1-5")
        self.sectionTB.setItemText(1, "Section 6-10")
        self.sectionTB.setItemText(2, "Section 11-15")
        self.sectionData.setText(self.section.currentText())
        self.occupationData.setText("...")
        self.failData.setText("...")

        #Switch Toggle Signal
        self.toggleDirection.clicked.connect(self.toggle_direction_handler)
        #Crossroad Toggle Signal
        self.toggleCrossroad.clicked.connect(self.toggle_crossroad_handler)
        #Green button
        self.greenButton.clicked.connect(self.green_handler)
        #Red button
        self.redButton.clicked.connect(self.red_handler)
        #Apply Button
        self.applyTB.clicked.connect(self.apply_handler)
        #Change section
        self.section.currentIndexChanged.connect(self.newSection)
        #Change TB section
        self.sectionTB.currentIndexChanged.connect(self.newSectionTB)
        #Change page
        self.pageSelection.currentChanged.connect(self.pageChange)
        #Mode
        self.modeButton.toggled.connect(self.mode_handler)

        #variables
        self.direc = False
        self.cross = [False, False, False]
        self.sig = [False, False, False]
        self.station = ""
        self.occupation = ["...","...","..."]
        self.failures = ["...","...","..."]


    def toggle_direction_handler(self):
        self.direc = not self.direc
        section_index = self.section.currentIndex()
        switch_index = self.switchSelect.currentIndex()
        if(self.direc):
            pixmap = QPixmap("1140\TrackControllerSw\light.jpg")
        else:
            pixmap = QPixmap("1140\TrackControllerSw\left.jpg")
        self.switchDirection.setPixmap(pixmap)

    def toggle_crossroad_handler(self):
        
        section_index = self.section.currentIndex()
        crossroad_index = self.crossroadSelect.currentIndex()
        self.cross[section_index] = not self.cross[section_index]
        if(self.cross[section_index]):
            pixmap = QPixmap("1140\TrackControllerSw\crossc.jpg")
        else:
            pixmap = QPixmap("1140\TrackControllerSw\crosso.jpg")
        self.crossroadStatus.setPixmap(pixmap)

    def green_handler(self):
        section_index = self.section.currentIndex()
        signal_index = self.signalSelect.currentIndex()
        self.signalState.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.sig[section_index] = False

    def red_handler(self):
        section_index = self.section.currentIndex()
        signal_index = self.signalSelect.currentIndex()
        self.signalState.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.sig[section_index] = True
        

    def apply_handler(self):
        sectionTB_index = self.sectionTB.currentIndex()
        switchTB_index = self.switchSelectTB.currentIndex()
        crossroadTB_index = self.crossroadSelectTB.currentIndex()
        signalTB_index = self.signalSelectTB.currentIndex()
        if(self.switchStatusTB.currentIndex() == 0):
            self.direc = False
        else:
            self.direc = True
        if(self.crossroadStatusTB.currentIndex() == 0):
            self.cross[sectionTB_index] = False
        else:
            self.cross[sectionTB_index] = True
        if(self.signalStatusTB.currentIndex() == 0):
            self.sig[sectionTB_index] = False
        else:
            self.sig[sectionTB_index] = True
        self.station = self.lineEdit.text()
        text = (self.dataTB.item(1,0)).text()
        self.occupation[sectionTB_index] = text
        text = (self.dataTB.item(2,0)).text()
        self.failures[sectionTB_index] = text
    
    def newSection(self):
        section_index = self.section.currentIndex()
        self.sectionData.setText(self.section.currentText())
        self.occupationData.setText(self.occupation[section_index])
        self.failData.setText(self.failures[section_index])
        if(self.cross[section_index]):
            pixmap = QPixmap("1140\TrackControllerSw\crossc.jpg")
        else:
            pixmap = QPixmap("1140\TrackControllerSw\crosso.jpg")
        self.crossroadStatus.setPixmap(pixmap)
        if(self.sig[section_index]):
            self.signalState.setStyleSheet("background-color: rgb(255, 0, 0);")
        else:
            self.signalState.setStyleSheet("background-color: rgb(0, 255, 0);")
        if(section_index == 0):
            if(self.direc):
                pixmap = QPixmap("1140\TrackControllerSw\light.jpg")
            else:
                pixmap = QPixmap("1140\TrackControllerSw\left.jpg")
            self.switchDirection.setPixmap(pixmap)
            self.leftSection.show()
            self.rightSection.show()
            self.toggleDirection.show()
        else:
            if(section_index == 1):
                pixmap = QPixmap("")
                self.switchDirection.setPixmap(pixmap)
                self.leftSection.hide()
                self.rightSection.hide()
                self.toggleDirection.hide()
            else:
                pixmap = QPixmap("")
                self.switchDirection.setPixmap(pixmap)
                self.leftSection.hide()
                self.rightSection.hide()
                self.toggleDirection.hide()

    def newSectionTB(self):
        text = QTableWidgetItem(self.sectionTB.currentText())
        self.dataTB.setItem(0,0,text)
        section_index = self.sectionTB.currentIndex()
        text = QTableWidgetItem(self.occupation[section_index])
        self.dataTB.setItem(1,0,text)
        text = QTableWidgetItem(self.failures[section_index])
        self.dataTB.setItem(2,0,text)
        if(self.cross[section_index]):
            self.crossroadStatusTB.setCurrentIndex(1)
        else:
            self.crossroadStatusTB.setCurrentIndex(0)
        if(self.sig[section_index]):
            self.signalStatusTB.setCurrentIndex(1)
        else:
            self.signalStatusTB.setCurrentIndex(0)
        if(section_index == 0):
            if(self.direc):
                self.switchStatusTB.setCurrentIndex(1)
            else:
                self.switchStatusTB.setCurrentIndex(0)
            self.switchStatusTB.show()
        else:
            if(section_index == 1):
                self.switchStatusTB.hide()
            else:
                self.switchStatusTB.hide()

    def pageChange(self):
        if(self.pageSelection.currentIndex() == 0):
            section_index = self.section.currentIndex()
            self.sectionData.setText(self.section.currentText())
            self.nextStation.setText(self.station)
            self.occupationData.setText(self.occupation[section_index])
            self.failData.setText(self.failures[section_index])
            if(self.cross[section_index]):
                pixmap = QPixmap("1140\TrackControllerSw\crossc.jpg")
            else:
                pixmap = QPixmap("1140\TrackControllerSw\crosso.jpg")
            self.crossroadStatus.setPixmap(pixmap)
            if(self.sig[section_index]):
                self.signalState.setStyleSheet("background-color: rgb(255, 0, 0);")
            else:
                self.signalState.setStyleSheet("background-color: rgb(0, 255, 0);")
            if(section_index == 0):
                if(self.direc):
                    pixmap = QPixmap("1140\TrackControllerSw\light.jpg")
                else:
                    pixmap = QPixmap("1140\TrackControllerSw\left.jpg")
                self.switchDirection.setPixmap(pixmap)
                self.leftSection.show()
                self.rightSection.show()
                self.toggleDirection.show()
            else:
                if(section_index == 1):
                    pixmap = QPixmap("")
                    self.switchDirection.setPixmap(pixmap)
                    self.leftSection.hide()
                    self.rightSection.hide()
                    self.toggleDirection.hide()
                else:
                    pixmap = QPixmap("")
                    self.switchDirection.setPixmap(pixmap)
                    self.leftSection.hide()
                    self.rightSection.hide()
                    self.toggleDirection.hide()
        else:
            text = QTableWidgetItem(self.sectionTB.currentText())
            self.dataTB.setItem(0,0,text)
            section_index = self.sectionTB.currentIndex()
            text = QTableWidgetItem(self.occupation[section_index])
            self.dataTB.setItem(1,0,text)
            text = QTableWidgetItem(self.failures[section_index])
            self.dataTB.setItem(2,0,text)
            if(self.cross[section_index]):
                self.crossroadStatusTB.setCurrentIndex(1)
            else:
                self.crossroadStatusTB.setCurrentIndex(0)
            if(self.sig[section_index]):
                self.signalStatusTB.setCurrentIndex(1)
            else:
                self.signalStatusTB.setCurrentIndex(0)
            if(section_index == 0):
                if(self.direc):
                    self.switchStatusTB.setCurrentIndex(1)
                else:
                    self.switchStatusTB.setCurrentIndex(0)
                self.switchStatusTB.show()
            else:
                if(section_index == 1):
                    self.switchStatusTB.hide()
                else:
                    self.switchStatusTB.hide()
        self.mode_handler()

    def mode_handler(self):
        if(self.modeButton.isChecked()):
            self.toggleDirection.hide()
            self.toggleCrossroad.hide()
            self.greenButton.hide()
            self.redButton.hide()
            if(self.nextStation.text() == "Station B"):
                self.direc = False
                if(self.section.currentIndex() == 0):
                    pixmap = QPixmap("1140\TrackControllerSw\left.jpg")
                    self.switchDirection.setPixmap(pixmap)
            if(self.nextStation.text() == "Station C"):
                self.direc = True
                if(self.section.currentIndex() == 0):
                    pixmap = QPixmap("1140\TrackControllerSw\light.jpg")
                    self.switchDirection.setPixmap(pixmap)
            if(self.occupationData.text() == "Occupied"):
                self.cross[self.section.currentIndex()] = True
                pixmap = QPixmap("1140\TrackControllerSw\crossc.jpg")
                self.crossroadStatus.setPixmap(pixmap)
            if(self.occupationData.text() == "Unoccupied"):
                self.cross[self.section.currentIndex()] = False
                pixmap = QPixmap("1140\TrackControllerSw\crosso.jpg")
                self.crossroadStatus.setPixmap(pixmap)
            if(self.failData.text() == "Failure"):
                self.sig[self.section.currentIndex()] = True
                self.signalState.setStyleSheet("background-color: rgb(255, 0, 0);")
            else:
                self.sig[self.section.currentIndex()] = False
                self.signalState.setStyleSheet("background-color: rgb(0, 255, 0);")
                

        else:
            if(self.section.currentIndex() == 0):
                self.toggleDirection.show()
            self.toggleCrossroad.show()
            self.greenButton.show()
            self.redButton.show()



    ########################################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name.setText(_translate("MainWindow", "Track Controller"))
        self.section.setItemText(0, _translate("MainWindow", "Section A"))
        self.section.setItemText(1, _translate("MainWindow", "Section B"))
        self.section.setItemText(2, _translate("MainWindow", "Section C"))
        self.switchDirection.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/left/left.jpg\"/></p></body></html>"))
        self.toggleDirection.setText(_translate("MainWindow", "Toggle Direction"))
        self.switchSelect.setItemText(0, _translate("MainWindow", "Switch 1"))
        self.leftSection.setText(_translate("MainWindow", "Left"))
        self.rightSection.setText(_translate("MainWindow", "Right"))
        self.crossroadStatus.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/crossc/crossc.jpg\"/></p></body></html>"))
        self.toggleCrossroad.setText(_translate("MainWindow", "Toggle Crossroad"))
        self.crossroadSelect.setItemText(0, _translate("MainWindow", "Crossroad 1"))
        self.greenButton.setText(_translate("MainWindow", "Green"))
        self.redButton.setText(_translate("MainWindow", "Red"))
        self.signalState.setText(_translate("MainWindow", "Current Signal"))
        self.signalSelect.setItemText(0, _translate("MainWindow", "Signal 1"))
        self.modeButton.setText(_translate("MainWindow", "Automatic Mode"))
        self.sectionData.setText(_translate("MainWindow", "A"))
        self.secLab.setText(_translate("MainWindow", "Section:"))
        self.occupationData.setText(_translate("MainWindow", "Unoccupied"))
        self.occLab.setText(_translate("MainWindow", "Occupation:"))
        self.failData.setText(_translate("MainWindow", "No Failures"))
        self.faiLab.setText(_translate("MainWindow", "Failures:"))
        self.nextStation.setText(_translate("MainWindow", "..."))
        self.stattext.setText(_translate("MainWindow", "Next Station:"))
        self.pageSelection.setTabText(self.pageSelection.indexOf(self.mainPage), _translate("MainWindow", "Main Page"))
        item = self.dataTB.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Track Section:"))
        item = self.dataTB.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Section Occupation:"))
        item = self.dataTB.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Section Failure:"))
        item = self.dataTB.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Suggested Speed:"))
        item = self.dataTB.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Authority:"))
        item = self.dataTB.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Route:"))
        __sortingEnabled = self.dataTB.isSortingEnabled()
        self.dataTB.setSortingEnabled(False)
        item = self.dataTB.item(0, 0)
        item.setText(_translate("MainWindow", "A"))
        item = self.dataTB.item(1, 0)
        item.setText(_translate("MainWindow", "Not Occupied"))
        item = self.dataTB.item(2, 0)
        item.setText(_translate("MainWindow", "No Failure"))
        item = self.dataTB.item(3, 0)
        item.setText(_translate("MainWindow", "30m/s"))
        item = self.dataTB.item(4, 0)
        item.setText(_translate("MainWindow", "10"))
        item = self.dataTB.item(5, 0)
        item.setText(_translate("MainWindow", "1"))
        self.dataTB.setSortingEnabled(__sortingEnabled)
        self.sectionTB.setItemText(0, _translate("MainWindow", "Section A"))
        self.sectionTB.setItemText(1, _translate("MainWindow", "Section B"))
        self.sectionTB.setItemText(2, _translate("MainWindow", "Section C"))
        self.switchSelectTB.setItemText(0, _translate("MainWindow", "Switch 1"))
        self.stattext_4.setText(_translate("MainWindow", "Switch Status:"))
        self.switchStatusTB.setItemText(0, _translate("MainWindow", "Left"))
        self.switchStatusTB.setItemText(1, _translate("MainWindow", "Right"))
        self.crossroadSelectTB.setItemText(0, _translate("MainWindow", "Crossroad 1"))
        self.stattext_3.setText(_translate("MainWindow", "Crossroad Status:"))
        self.crossroadStatusTB.setItemText(0, _translate("MainWindow", "Open"))
        self.crossroadStatusTB.setItemText(1, _translate("MainWindow", "Closed"))
        self.signalSelectTB.setItemText(0, _translate("MainWindow", "Signal 1"))
        self.stattext_5.setText(_translate("MainWindow", "Signal Status:"))
        self.signalStatusTB.setItemText(0, _translate("MainWindow", "Green"))
        self.signalStatusTB.setItemText(1, _translate("MainWindow", "Red"))
        self.applyTB.setText(_translate("MainWindow", "Apply Changes"))
        self.stattext_2.setText(_translate("MainWindow", "Next Station:"))
        self.lineEdit.setText(_translate("MainWindow", "..."))
        self.pageSelection.setTabText(self.pageSelection.indexOf(self.testBench), _translate("MainWindow", "Test Bench"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
