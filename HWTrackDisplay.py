from PyQt6 import QtCore, QtGui, QtWidgets
from UI_Breadboard_Class import Operations

operate = Operations() #Class to perform operations on the breadboard

class Ui_MainWindow(object):

    Light1 = "green"
    Light2 = "red"
    Switch1 = "right"
    Switch2 = "left"
    Crossroad1 = "on"
    Crossroad2 = "off"

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
        self.comboBox_5.setDisabled(True)

        self.comboBox_6 = QtWidgets.QComboBox(parent=self.tab_2)
        self.comboBox_6.setGeometry(QtCore.QRect(330, 70, 121, 22))
        self.comboBox_6.setObjectName("comboBox_6") #Crossroad Selector
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setDisabled(True)

        self.comboBox_7 = QtWidgets.QComboBox(parent=self.tab_2)
        self.comboBox_7.setGeometry(QtCore.QRect(500, 70, 101, 22))
        self.comboBox_7.setObjectName("comboBox_7") #Switch Selector
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setDisabled(True)

        self.label = QtWidgets.QLabel(parent=self.tab_2)
        self.label.setGeometry(QtCore.QRect(170, 110, 101, 21))
        self.listWidget_7 = QtWidgets.QListWidget(parent=self.tab_2)
        self.listWidget_7.setGeometry(QtCore.QRect(650, 50, 81, 131))
        self.listWidget_7.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listWidget_7.setObjectName("listWidget_7") #Block Occupancy List
        self.listWidget_7.setDisabled(True)

        self.label_12 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(650, 30, 91, 20))
        self.label_12.setObjectName("label_12") #Blocks occupied label (No need to edit)

        self.listWidget_8 = QtWidgets.QListWidget(parent=self.tab_2)
        self.listWidget_8.setGeometry(QtCore.QRect(780, 50, 81, 131))
        self.listWidget_8.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listWidget_8.setObjectName("listWidget_8") #Track Failures List
        self.listWidget_8.setDisabled(True)

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
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
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
        self.listWidget_5.setDisabled(True)

        self.label_10 = QtWidgets.QLabel(parent=self.tab)
        self.label_10.setGeometry(QtCore.QRect(630, 30, 91, 20))
        self.label_10.setObjectName("label_10") #Blocks occupied label (No need to edit)

        self.listWidget_6 = QtWidgets.QListWidget(parent=self.tab)
        self.listWidget_6.setGeometry(QtCore.QRect(770, 50, 81, 131))
        self.listWidget_6.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listWidget_6.setObjectName("listWidget_6") #Track Failures List
        self.listWidget_6.setDisabled(True)

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
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.tab_3)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 160, 111, 51))
        self.pushButton_4.setObjectName("pushButton_4") #Toggle Occupancy
        self.comboBox_9 = QtWidgets.QComboBox(parent=self.tab_3)
        self.comboBox_9.setGeometry(QtCore.QRect(170, 10, 101, 22))
        self.comboBox_9.setObjectName("comboBox_9") #Select Light
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_10 = QtWidgets.QComboBox(parent=self.tab_3)
        self.comboBox_10.setGeometry(QtCore.QRect(310, 10, 121, 22))
        self.comboBox_10.setObjectName("comboBox_10") #Select Crossroad
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_11 = QtWidgets.QComboBox(parent=self.tab_3)
        self.comboBox_11.setGeometry(QtCore.QRect(470, 10, 101, 22))
        self.comboBox_11.setObjectName("comboBox_11") #Select Switch
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
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
        self.listWidget_10 = QtWidgets.QListWidget(parent=self.tab_3)
        self.listWidget_10.setGeometry(QtCore.QRect(340, 50, 41, 41))
        self.listWidget_10.setObjectName("listWidget_10") #Select Status of Crossroad
        item = QtWidgets.QListWidgetItem()
        self.listWidget_10.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_10.addItem(item)
        self.listWidget_11 = QtWidgets.QListWidget(parent=self.tab_3)
        self.listWidget_11.setGeometry(QtCore.QRect(470, 50, 91, 41))
        self.listWidget_11.setObjectName("listWidget_11") #Select Switch to change to
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.tab_3)
        self.pushButton_5.setGeometry(QtCore.QRect(160, 160, 111, 51))
        self.pushButton_5.setObjectName("pushButton_5") #Toggle Track Failure
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
        self.tabWidget.addTab(self.tab_3, "")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 0, 201, 41))
        self.pushButton_3.setObjectName("pushButton_3") #Open PLC code button
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
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Select Light"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "Light 1"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Select Crossroad"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "Crossroad 1"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "Select Switch"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "Switch 1"))
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
        self.comboBox_8.setItemText(0, _translate("MainWindow", "Track Selection"))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "A"))
        self.comboBox_8.setItemText(2, _translate("MainWindow", "B"))
        self.comboBox_8.setItemText(3, _translate("MainWindow", "C"))
        self.pushButton_4.setText(_translate("MainWindow", "Toggle Occupancy"))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "Select Light"))
        self.comboBox_9.setItemText(1, _translate("MainWindow", "Light 1"))
        self.comboBox_10.setItemText(0, _translate("MainWindow", "Select Crossroad"))
        self.comboBox_10.setItemText(1, _translate("MainWindow", "Crossroad 1"))
        self.comboBox_11.setItemText(0, _translate("MainWindow", "Select Switch"))
        self.comboBox_11.setItemText(1, _translate("MainWindow", "Switch 1"))
        __sortingEnabled = self.listWidget_4.isSortingEnabled()
        self.listWidget_4.setSortingEnabled(False)
        item = self.listWidget_4.item(0)
        item.setText(_translate("MainWindow", "Red"))
        item = self.listWidget_4.item(1)
        item.setText(_translate("MainWindow", "Green"))
        self.listWidget_4.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_10.isSortingEnabled()
        self.listWidget_10.setSortingEnabled(False)
        item = self.listWidget_10.item(0)
        item.setText(_translate("MainWindow", "On"))
        item = self.listWidget_10.item(1)
        item.setText(_translate("MainWindow", "Off"))
        self.listWidget_10.setSortingEnabled(__sortingEnabled)
        self.pushButton_5.setText(_translate("MainWindow", "Toggle Track Failure"))
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
    def defaultLight(self, text):
        if text == "Light 1":
            operate.changeLight(self.Light1)
        elif text == "Light 2":
            operate.changeLight(self.Light2)
    def saveLight(self, item):
        if self.comboBox_2.currentText() == "Light 1":
            self.Light1 = item
            operate.changeLight(self.Light1)
        elif self.comboBox_2.currentText() == "Light 2":
            self.Light2 = item
            operate.changeLight(self.Light2)


    #Functions for Automatic Mode

    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
