from PyQt6 import QtCore, QtGui, QtWidgets
from UI_Breadboard_Class import Operations
from PyQt6.QtWidgets import QFileDialog
import subprocess

operate = Operations() #Class to perform operations on the breadboard

class Ui_MainWindow(object):

    Light1 = "green"
    Light2 = "red"
    Switch1 = "left"
    Switch2 = "left"
    Crossroad1 = "off"
    Crossroad2 = "off"
    BlockA = False
    BlockB = False
    BlockC = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(916, 350)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 40, 901, 251))
        self.tabWidget.setObjectName("tabWidget")



        #Automatic Tab
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listWidget_3 = QtWidgets.QListWidget(parent=self.tab_2)
        self.listWidget_3.setGeometry(QtCore.QRect(10, 20, 121, 61))
        self.listWidget_3.setObjectName("listWidget_3") #Wayside Selector
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)

        self.comboBox_5 = QtWidgets.QComboBox(parent=self.tab_2)
        self.comboBox_5.setGeometry(QtCore.QRect(170, 70, 101, 22))
        self.comboBox_5.setObjectName("comboBox_5") #Light Selector
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setDisabled(True)

        self.comboBox_6 = QtWidgets.QComboBox(parent=self.tab_2)
        self.comboBox_6.setGeometry(QtCore.QRect(330, 70, 121, 22))
        self.comboBox_6.setObjectName("comboBox_6") #Crossroad Selector
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setDisabled(True)

        self.comboBox_7 = QtWidgets.QComboBox(parent=self.tab_2)
        self.comboBox_7.setGeometry(QtCore.QRect(500, 70, 101, 22))
        self.comboBox_7.setObjectName("comboBox_7") #Switch Selector
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setDisabled(True)

        self.label = QtWidgets.QLabel(parent=self.tab_2)
        self.label.setGeometry(QtCore.QRect(170, 110, 101, 21))
        self.listWidget_7 = QtWidgets.QListWidget(parent=self.tab_2)
        self.listWidget_7.setGeometry(QtCore.QRect(650, 50, 81, 131))
        self.listWidget_7.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listWidget_7.setObjectName("listWidget_7") #Block Occupancy List

        self.label_12 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(650, 30, 91, 20))
        self.label_12.setObjectName("label_12") #Blocks occupied label (No need to edit)

        self.listWidget_8 = QtWidgets.QListWidget(parent=self.tab_2)
        self.listWidget_8.setGeometry(QtCore.QRect(780, 50, 81, 131))
        self.listWidget_8.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listWidget_8.setObjectName("listWidget_8") #Track Failures List

        self.label_13 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(780, 30, 81, 20))
        self.label_13.setObjectName("label_13") #Blocks failure label (No need to edit)
        self.tabWidget.addTab(self.tab_2, "")



        #Manual Tab
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.listWidget = QtWidgets.QListWidget(parent=self.tab)
        self.listWidget.setGeometry(QtCore.QRect(10, 30, 121, 61))
        self.listWidget.setObjectName("listWidget") #Wayside Selector
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)

        self.listWidget_2 = QtWidgets.QListWidget(parent=self.tab)
        self.listWidget_2.setGeometry(QtCore.QRect(160, 120, 91, 41))
        self.listWidget_2.setObjectName("listWidget_2") #Light Color selector
        item = QtWidgets.QListWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 12, 12))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.listWidget_2.addItem(item)
        self.listWidget_2.setDisabled(True)

        self.comboBox_2 = QtWidgets.QComboBox(parent=self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(160, 60, 101, 22))
        self.comboBox_2.setObjectName("comboBox_2") #Select Light
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setDisabled(True)

        self.pushButton = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton.setGeometry(QtCore.QRect(320, 120, 101, 51))
        self.pushButton.setObjectName("pushButton") #Toggle Crossroad
        self.pushButton.setDisabled(True)

        self.comboBox_3 = QtWidgets.QComboBox(parent=self.tab)
        self.comboBox_3.setGeometry(QtCore.QRect(310, 60, 121, 22))
        self.comboBox_3.setObjectName("comboBox_3") #Select Crossroad
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setDisabled(True)

        self.pushButton_2 = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 120, 101, 51))
        self.pushButton_2.setObjectName("pushButton_2") #Toggle Switch
        self.pushButton_2.setDisabled(True)

        self.comboBox_4 = QtWidgets.QComboBox(parent=self.tab)
        self.comboBox_4.setGeometry(QtCore.QRect(500, 60, 101, 22))
        self.comboBox_4.setObjectName("comboBox_4") #Select Switch
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setDisabled(True)

        self.listWidget_5 = QtWidgets.QListWidget(parent=self.tab)
        self.listWidget_5.setGeometry(QtCore.QRect(630, 50, 81, 131))
        self.listWidget_5.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listWidget_5.setObjectName("listWidget_5") #Blocks Occupied List

        self.label_10 = QtWidgets.QLabel(parent=self.tab)
        self.label_10.setGeometry(QtCore.QRect(630, 30, 91, 20))
        self.label_10.setObjectName("label_10") #Blocks occupied label (No need to edit)

        self.listWidget_6 = QtWidgets.QListWidget(parent=self.tab)
        self.listWidget_6.setGeometry(QtCore.QRect(770, 50, 81, 131))
        self.listWidget_6.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listWidget_6.setObjectName("listWidget_6") #Track Failures List

        self.label_11 = QtWidgets.QLabel(parent=self.tab)
        self.label_11.setGeometry(QtCore.QRect(770, 30, 81, 20))
        self.label_11.setObjectName("label_11") #Blocks failure label (No need to edit)
        self.tabWidget.addTab(self.tab, "")



        #Test Bench Tab
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.listWidget_9 = QtWidgets.QListWidget(parent=self.tab_3)
        self.listWidget_9.setGeometry(QtCore.QRect(10, 10, 121, 61))
        self.listWidget_9.setObjectName("listWidget_9") #Wayside Selector
        item = QtWidgets.QListWidgetItem()
        self.listWidget_9.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_9.addItem(item)

        self.comboBox_8 = QtWidgets.QComboBox(parent=self.tab_3)
        self.comboBox_8.setGeometry(QtCore.QRect(90, 110, 101, 22))
        self.comboBox_8.setObjectName("comboBox_8") #Track selections
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setDisabled(True)

        self.pushButton_4 = QtWidgets.QPushButton(parent=self.tab_3)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 160, 111, 51))
        self.pushButton_4.setObjectName("pushButton_4") #Toggle Occupancy
        self.pushButton_4.setDisabled(True)

        self.comboBox_9 = QtWidgets.QComboBox(parent=self.tab_3)
        self.comboBox_9.setGeometry(QtCore.QRect(170, 10, 101, 22))
        self.comboBox_9.setObjectName("comboBox_9") #Select Light
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.setDisabled(True)

        self.comboBox_10 = QtWidgets.QComboBox(parent=self.tab_3)
        self.comboBox_10.setGeometry(QtCore.QRect(310, 10, 121, 22))
        self.comboBox_10.setObjectName("comboBox_10") #Select Crossroad
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.setDisabled(True)

        self.comboBox_11 = QtWidgets.QComboBox(parent=self.tab_3)
        self.comboBox_11.setGeometry(QtCore.QRect(470, 10, 101, 22))
        self.comboBox_11.setObjectName("comboBox_11") #Select Switch
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.setDisabled(True)

        self.listWidget_4 = QtWidgets.QListWidget(parent=self.tab_3)
        self.listWidget_4.setGeometry(QtCore.QRect(170, 50, 91, 41))
        self.listWidget_4.setObjectName("listWidget_4") #Select Light Color
        item = QtWidgets.QListWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.listWidget_4.addItem(item)
        self.listWidget_4.setDisabled(True)

        self.listWidget_10 = QtWidgets.QListWidget(parent=self.tab_3)
        self.listWidget_10.setGeometry(QtCore.QRect(340, 50, 41, 41))
        self.listWidget_10.setObjectName("listWidget_10") #Select Status of Crossroad
        item = QtWidgets.QListWidgetItem()
        self.listWidget_10.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_10.addItem(item)
        self.listWidget_10.setDisabled(True)

        self.listWidget_11 = QtWidgets.QListWidget(parent=self.tab_3)
        self.listWidget_11.setGeometry(QtCore.QRect(470, 50, 91, 41))
        self.listWidget_11.setObjectName("listWidget_11") #Select Switch to change to
        item = QtWidgets.QListWidgetItem()
        self.listWidget_11.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_11.addItem(item)
        self.listWidget_11.setDisabled(True)

        self.pushButton_5 = QtWidgets.QPushButton(parent=self.tab_3)
        self.pushButton_5.setGeometry(QtCore.QRect(160, 160, 111, 51))
        self.pushButton_5.setObjectName("pushButton_5") #Toggle Track Failure
        self.pushButton_5.setDisabled(True)

        #Dont change any below
        self.label_3 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(670, 0, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3") #Inputs for CTC label (No need to edit)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.tab_3)
        self.tableWidget.setGeometry(QtCore.QRect(650, 50, 211, 91))
        self.tableWidget.setObjectName("tableWidget") #Displays Suggested speed and authority
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)


        #Whole UI Stuff
        self.tabWidget.addTab(self.tab_3, "")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 0, 201, 41))
        self.pushButton_3.setObjectName("pushButton_3") #Open PLC code button

        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget) #File location label
        self.label_4.setGeometry(QtCore.QRect(220, 10, 650, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar") #Don't edit 
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        #Automatic Mode UI
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HW Track Controller UI"))
        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        item = self.listWidget_3.item(0)
        item.setText(_translate("MainWindow", "Red Line Wayside"))
        item = self.listWidget_3.item(1)
        item.setText(_translate("MainWindow", "Green Line Wayside"))
        self.listWidget_3.setSortingEnabled(__sortingEnabled)
        self.listWidget_3.itemClicked.connect(self.checkListAutomatic)

        self.comboBox_5.setItemText(0, _translate("MainWindow", "Select Light"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "Light 1"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "Light 2"))
        self.comboBox_5.currentTextChanged.connect(self.defaultLight)


        self.comboBox_6.setItemText(0, _translate("MainWindow", "Select Crossroad"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "Crossroad 1"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "Crossroad 2"))
        self.comboBox_6.currentTextChanged.connect(self.defaultCrossroad)

        self.comboBox_7.setItemText(0, _translate("MainWindow", "Select Switch"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "Switch 1"))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "Switch 2"))
        self.comboBox_7.currentTextChanged.connect(self.defaultSwitch)

        self.label_12.setText(_translate("MainWindow", "Blocks Occupied"))

        self.label_13.setText(_translate("MainWindow", "Track Failures"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Main Page - Automatic"))



        #Manual Mode UI
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Red Line Wayside"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Green Line Wayside"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.listWidget.itemClicked.connect(self.checkListManual)

        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        red = self.listWidget_2.item(0)
        red.setText(_translate("MainWindow", "Red"))
        red = self.listWidget_2.item(1)
        red.setText(_translate("MainWindow", "Green"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.listWidget_2.itemClicked.connect(lambda item=red: self.saveLight(item.text()))

        self.comboBox_2.setItemText(0, _translate("MainWindow", "Select Light"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Light 1"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Light 2"))
        self.comboBox_2.currentIndexChanged.connect(self.lightChangeManual)
        self.comboBox_2.currentTextChanged.connect(self.defaultLight)

        self.pushButton.setText(_translate("MainWindow", "Toggle Crossroad"))
        self.pushButton.clicked.connect(self.crossroadUpdater)

        self.comboBox_3.setItemText(0, _translate("MainWindow", "Select Crossroad"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Crossroad 1"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Crossroad 2"))
        self.comboBox_3.currentIndexChanged.connect(self.crossChangeManual)
        self.comboBox_3.currentTextChanged.connect(self.defaultCrossroad)

        self.pushButton_2.setText(_translate("MainWindow", "Toggle Switch"))
        self.pushButton_2.clicked.connect(self.switchUpdater)

        #Toggles that block occupancy has been changed
        self.listWidget_5.model().rowsInserted.connect(self.plcCode)
        self.listWidget_5.model().rowsRemoved.connect(self.plcCode)

        self.comboBox_4.setItemText(0, _translate("MainWindow", "Select Switch"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Switch 1"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Switch 2"))
        self.comboBox_4.currentIndexChanged.connect(self.switchChangeManual)
        self.comboBox_4.currentTextChanged.connect(self.defaultSwitch)

        #No need to edit these 3 values
        self.label_10.setText(_translate("MainWindow", "Blocks Occupied"))
        self.label_11.setText(_translate("MainWindow", "Track Failures"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Main Page - Manual"))

        #Test Bench UI
        __sortingEnabled = self.listWidget_9.isSortingEnabled()
        self.listWidget_9.setSortingEnabled(False)
        item = self.listWidget_9.item(0)
        item.setText(_translate("MainWindow", "Red Line Wayside"))
        item = self.listWidget_9.item(1)
        item.setText(_translate("MainWindow", "Green Line Wayside"))
        self.listWidget_9.setSortingEnabled(__sortingEnabled)
        self.listWidget_9.itemClicked.connect(self.checkListTest)

        self.comboBox_8.setItemText(0, _translate("MainWindow", "Track Selection"))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "A"))
        self.comboBox_8.setItemText(2, _translate("MainWindow", "B"))
        self.comboBox_8.setItemText(3, _translate("MainWindow", "C"))
        self.comboBox_8.currentIndexChanged.connect(self.trackChangeTest)

        self.pushButton_4.setText(_translate("MainWindow", "Toggle Occupancy"))
        self.pushButton_4.clicked.connect(lambda: self.toggleOccu(self.comboBox_8.currentText()))

        self.comboBox_9.setItemText(0, _translate("MainWindow", "Select Light"))
        self.comboBox_9.setItemText(1, _translate("MainWindow", "Light 1"))
        self.comboBox_9.setItemText(2, _translate("MainWindow", "Light 2"))
        self.comboBox_9.currentIndexChanged.connect(self.lightChangeTest)

        self.comboBox_10.setItemText(0, _translate("MainWindow", "Select Crossroad"))
        self.comboBox_10.setItemText(1, _translate("MainWindow", "Crossroad 1"))
        self.comboBox_10.setItemText(2, _translate("MainWindow", "Crossroad 2"))
        self.comboBox_10.currentIndexChanged.connect(self.crossChangeTest)

        self.comboBox_11.setItemText(0, _translate("MainWindow", "Select Switch"))
        self.comboBox_11.setItemText(1, _translate("MainWindow", "Switch 1"))
        self.comboBox_11.setItemText(2, _translate("MainWindow", "Switch 2"))
        self.comboBox_11.currentIndexChanged.connect(self.switchChangeTest)
        self.comboBox_11.currentTextChanged.connect(self.switchSelection)

        __sortingEnabled = self.listWidget_4.isSortingEnabled()
        self.listWidget_4.setSortingEnabled(False)
        redTest = self.listWidget_4.item(0)
        redTest.setText(_translate("MainWindow", "Red"))
        redTest = self.listWidget_4.item(1)
        redTest.setText(_translate("MainWindow", "Green"))
        self.listWidget_4.setSortingEnabled(__sortingEnabled)
        self.listWidget_4.itemClicked.connect(lambda item=redTest: self.changeLight(item.text()))

        __sortingEnabled = self.listWidget_10.isSortingEnabled()
        self.listWidget_10.setSortingEnabled(False)
        cross = self.listWidget_10.item(0)
        cross.setText(_translate("MainWindow", "On"))
        cross = self.listWidget_10.item(1)
        cross.setText(_translate("MainWindow", "Off"))
        self.listWidget_10.setSortingEnabled(__sortingEnabled)
        self.listWidget_10.itemClicked.connect(lambda item=cross: self.changeCrossroad(item.text()))

        self.pushButton_5.setText(_translate("MainWindow", "Toggle Track Failure"))
        self.pushButton_5.clicked.connect(lambda: self.toggleFailure(self.comboBox_8.currentText()))

        #For Selection of Switch list
        __sortingEnabled = self.listWidget_11.isSortingEnabled()
        self.listWidget_11.setSortingEnabled(__sortingEnabled)
        switch = self.listWidget_11.item(0)
        switch = self.listWidget_11.item(1)
        self.listWidget_11.itemClicked.connect(lambda item=switch: self.changeSwitch(item.text()))

        #Below is for Displaying CTC Info given
        self.label_3.setText(_translate("MainWindow", "Inputs from CTC"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Suggested Speed"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Authority"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Values"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "50 km/h"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "60 m"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Test Bench"))

        #PLC Code opener button
        self.pushButton_3.setText(_translate("MainWindow", "Open PLC Code"))
        self.label_4.setText("PLC Path Location")

        self.pushButton_3.clicked.connect(self.openArduinoFile)
    
    #Functions to be used in all
    def defaultCrossroad(self, text):
        if text == "Crossroad 1":
            if self.Crossroad1 == "on":
                operate.crossroadOn()
            else:
                operate.crossroadOff()
        elif text == "Crossroad 2":
            if self.Crossroad2 == "on":
                operate.crossroadOn()
            else:
                operate.crossroadOff()
    def defaultSwitch(self, text):
        if text == "Switch 1":
            if self.Switch1 == "right":
                operate.switchRight()
            else:
                operate.switchLeft()
        elif text == "Switch 2":
            if self.Switch2 == "right":
                operate.switchRight()
            else:
                operate.switchLeft()
    def defaultLight(self, text):
        if text == "Light 1":
            operate.changeLight(self.Light1)
        elif text == "Light 2":
            operate.changeLight(self.Light2)
    def openArduinoFile(self):
        dialog = QFileDialog()
        dialog.setNameFilter("Arduino File (*.ino)")
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        dialogSuccessful = dialog.exec()
        if dialogSuccessful:
            fileLocation = dialog.selectedFiles()[0]
            self.label_4.setText(fileLocation)
            arduino = "C:\Program Files (x86)\Arduino\\arduino.exe"
            command = f'"{arduino}" "{fileLocation}"'
            subprocess.run(command, shell=True)        
    def plcCode(self):
        self.BlockA = False
        self.BlockB = False
        self.BlockC = False
        items = [str(self.listWidget_5.item(i).text()) for i in range(self.listWidget_5.count())]
        for element in items:
            if element == "A":
                self.BlockA = True
            elif element == "B":
                self.BlockB = True
            elif element == "C":
                self.BlockC = True
        
        
        



    #Functions all to ensure Manual mode is Good
    def crossChangeManual(self): #Checks if still selecting crossroad to grey out button
        if self.comboBox_3.currentText() == "Select Crossroad":
            self.pushButton.setDisabled(True)
        else:
            self.pushButton.setDisabled(False)
    def switchChangeManual(self): #Checks if still selecting switch to grey out button
        if self.comboBox_4.currentText() == "Select Switch":
            self.pushButton_2.setDisabled(True)
        else:
            self.pushButton_2.setDisabled(False)
    def lightChangeManual(self): #Checks if still selecting light to grey out list
        if self.comboBox_2.currentText() == "Select Light":
            self.listWidget_2.setDisabled(True)
        else:
            self.listWidget_2.setDisabled(False)
    def checkListManual(self): #Checks if a wayside is selected or not to grey out combo boxes or not
        if self.listWidget.currentItem() is not None:
            self.enableCombosManual()
    def enableCombosManual(self): #enables all the combo boxes and lists in manual mode
        for combo_box in [self.comboBox_2, self.comboBox_3, self.comboBox_4, self.listWidget_5, self.listWidget_6]:
            combo_box.setEnabled(True)
    def crossroadUpdater(self):
        if self.comboBox_3.currentText() == "Crossroad 1":
            if self.Crossroad1 == "off":
                self.Crossroad1 = "on"
                operate.crossroadOn()
            elif self.Crossroad1 == "on":
                self.Crossroad1 = "off"
                operate.crossroadOff()
        elif self.comboBox_3.currentText() == "Crossroad 2":
            if self.Crossroad2 == "off":
                self.Crossroad2 = "on"
                operate.crossroadOn()
            elif self.Crossroad2 == "on":
                self.Crossroad2 = "off"
                operate.crossroadOff()
    def switchUpdater(self):
        if self.comboBox_4.currentText() == "Switch 1":
            if self.Switch1 == "right":
                self.Switch1 = "left"
                operate.switchLeft()
            elif self.Switch1 == "left":
                self.Switch1 = "right"
                operate.switchRight()
        elif self.comboBox_4.currentText() == "Switch 2":
            if self.Switch2 == "right":
                self.Switch2 = "left"
                operate.switchLeft()
            elif self.Switch2 == "left":
                self.Switch2 = "right"
                operate.switchRight()
    def saveLight(self, item):
        if self.comboBox_2.currentText() == "Light 1":
            self.Light1 = item
            operate.changeLight(self.Light1)
        elif self.comboBox_2.currentText() == "Light 2":
            self.Light2 = item
            operate.changeLight(self.Light2)


    #Functions for Automatic Mode
    def checkListAutomatic(self): #Checks if a wayside is selected or not to grey out combo boxes or not
        if self.listWidget_3.currentItem() is not None:
            self.enableCombosAutomatic()
    def enableCombosAutomatic(self): #Enables all combo boxes in Automatic tab
        for combo_box in [self.comboBox_5, self.comboBox_6, self.comboBox_7, self.listWidget_7, self.listWidget_8]:
            combo_box.setEnabled(True)

    #Functions for Test Bench
    def checkListTest(self): #Checks if a wayside is selected or not to grey out combo boxes or not
        if self.listWidget_9.currentItem() is not None:
            self.enableCombosTest()
    def enableCombosTest(self): #enables all the combo boxes and lists in manual mode
        for combo_box in [self.comboBox_9, self.comboBox_10, self.comboBox_11, self.comboBox_8]:
            combo_box.setEnabled(True)
    def crossChangeTest(self): #Checks if still selecting crossroad to grey out list
        if self.comboBox_10.currentText() == "Select Crossroad":
            self.listWidget_10.setDisabled(True)
        else:
            self.listWidget_10.setDisabled(False)
    def switchChangeTest(self): #Checks if still selecting switch to grey out list
        if self.comboBox_11.currentText() == "Select Switch":
            self.listWidget_11.setDisabled(True)
        else:
            self.listWidget_11.setDisabled(False)
    def lightChangeTest(self): #Checks if still selecting light to grey out list
        if self.comboBox_9.currentText() == "Select Light":
            self.listWidget_4.setDisabled(True)
        else:
            self.listWidget_4.setDisabled(False)
    def trackChangeTest(self):
        if self.comboBox_8.currentText() == "Track Selection":
            self.pushButton_4.setDisabled(True)
            self.pushButton_5.setDisabled(True)
        else:
            self.pushButton_4.setDisabled(False)
            self.pushButton_5.setDisabled(False)
    def changeLight(self, item):
        if self.comboBox_9.currentText() == "Light 1":
            self.Light1 = item
        elif self.comboBox_9.currentText() == "Light 2":
            self.Light2 = item
    def changeCrossroad(self, item):
        if self.comboBox_10.currentText() == "Crossroad 1":
            self.Crossroad1 = str(item).lower()
        elif self.comboBox_10.currentText() == "Crossroad 2":
            self.Crossroad2 = str(item).lower()
    def switchSelection(self, item):
        if item == "Switch 1":
            temp = self.listWidget_11.item(0)
            temp.setText("A->B")
            temp = self.listWidget_11.item(1)
            temp.setText("A<->C")
        elif item == "Switch 2":
            temp = self.listWidget_11.item(0)
            temp.setText("B->D")
            temp = self.listWidget_11.item(1)
            temp.setText("B->E")
        else:
            temp = self.listWidget_11.item(0)
            temp.setText("")
            temp = self.listWidget_11.item(1)
            temp.setText("")
    def changeSwitch(self, item):
        if self.comboBox_11.currentText() == "Switch 1":
            if item == "A->B":
                self.Switch1 = "right"
            else:
                self.Switch1 = "left"
        elif self.comboBox_11.currentText() == "Switch 2":
            if item == "B->D":
                self.Switch2 = "left"
            else:
                self.Switch2 = "right"
    def toggleOccu(self, value):
        item = self.listWidget_5.findItems(value, QtCore.Qt.MatchFlag.MatchExactly)
        if item:
            # If the item is found, remove it
            row = self.listWidget_5.row(item[0])
            self.listWidget_5.takeItem(row)
            self.listWidget_7.takeItem(row)
        else:
            # If the item is not found, add it
            new_item = QtWidgets.QListWidgetItem(value)
            self.listWidget_5.addItem(new_item)
            new_item2 = QtWidgets.QListWidgetItem(value)
            self.listWidget_7.addItem(new_item2)
    def toggleFailure(self, value):
        item = self.listWidget_6.findItems(value, QtCore.Qt.MatchFlag.MatchExactly)
        if item:
            # If the item is found, remove it
            row = self.listWidget_6.row(item[0])
            self.listWidget_6.takeItem(row)
            self.listWidget_8.takeItem(row)
        else:
            # If the item is not found, add it
            new_item = QtWidgets.QListWidgetItem(value)
            self.listWidget_6.addItem(new_item)
            new_item2 = QtWidgets.QListWidgetItem(value)
            self.listWidget_8.addItem(new_item2)




"""if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec()) """
