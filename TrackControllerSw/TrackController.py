# Form implementation generated from reading ui file 'TrackController.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


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
        self.sectionData = QtWidgets.QTableWidget(parent=self.mainPage)
        self.sectionData.setGeometry(QtCore.QRect(30, 50, 331, 261))
        self.sectionData.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sectionData.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.sectionData.setLineWidth(2)
        self.sectionData.setMidLineWidth(2)
        self.sectionData.setObjectName("sectionData")
        self.sectionData.setColumnCount(2)
        self.sectionData.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.sectionData.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sectionData.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.sectionData.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.sectionData.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sectionData.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.sectionData.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sectionData.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.sectionData.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sectionData.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.sectionData.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sectionData.setItem(2, 1, item)
        self.sectionData.horizontalHeader().setDefaultSectionSize(130)
        self.sectionData.horizontalHeader().setMinimumSectionSize(39)
        self.section = QtWidgets.QComboBox(parent=self.mainPage)
        self.section.setGeometry(QtCore.QRect(30, 10, 101, 22))
        self.section.setObjectName("section")
        self.section.addItem("")
        self.section.addItem("")
        self.switchFrame = QtWidgets.QFrame(parent=self.mainPage)
        self.switchFrame.setGeometry(QtCore.QRect(430, 40, 351, 271))
        self.switchFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.switchFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.switchFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.switchFrame.setObjectName("switchFrame")
        self.switchDirection = QtWidgets.QLabel(parent=self.switchFrame)
        self.switchDirection.setGeometry(QtCore.QRect(120, 110, 131, 91))
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
        self.switchSelect.addItem("")
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
        self.signalSelect.addItem("")
        self.modeButton = QtWidgets.QRadioButton(parent=self.mainPage)
        self.modeButton.setGeometry(QtCore.QRect(660, 10, 121, 20))
        self.modeButton.setObjectName("modeButton")
        self.nextStation = QtWidgets.QLabel(parent=self.mainPage)
        self.nextStation.setGeometry(QtCore.QRect(390, 10, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nextStation.setFont(font)
        self.nextStation.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.nextStation.setLineWidth(1)
        self.nextStation.setMidLineWidth(0)
        self.nextStation.setObjectName("nextStation")
        self.statText = QtWidgets.QLabel(parent=self.mainPage)
        self.statText.setGeometry(QtCore.QRect(300, 0, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.statText.setFont(font)
        self.statText.setLineWidth(1)
        self.statText.setMidLineWidth(0)
        self.statText.setObjectName("statText")
        self.switchFrame.raise_()
        self.sectionData.raise_()
        self.section.raise_()
        self.crossroadFrame.raise_()
        self.signalFrame.raise_()
        self.modeButton.raise_()
        self.nextStation.raise_()
        self.statText.raise_()
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
        self.dataTB.setColumnCount(2)
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
        self.dataTB.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTB.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTB.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTB.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTB.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTB.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTB.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTB.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTB.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTB.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTB.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTB.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTB.setItem(5, 1, item)
        self.dataTB.horizontalHeader().setDefaultSectionSize(130)
        self.dataTB.horizontalHeader().setMinimumSectionSize(39)
        self.sectionTB = QtWidgets.QComboBox(parent=self.testBench)
        self.sectionTB.setGeometry(QtCore.QRect(30, 10, 101, 22))
        self.sectionTB.setObjectName("sectionTB")
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
        self.switchSelectTB.addItem("")
        self.switchData = QtWidgets.QTableWidget(parent=self.switchTB)
        self.switchData.setGeometry(QtCore.QRect(0, 20, 351, 51))
        self.switchData.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.switchData.setObjectName("switchData")
        self.switchData.setColumnCount(2)
        self.switchData.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.switchData.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.switchData.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.switchData.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.switchData.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.switchData.setItem(0, 1, item)
        self.switchData.horizontalHeader().setDefaultSectionSize(150)
        self.crossroadTB = QtWidgets.QFrame(parent=self.testBench)
        self.crossroadTB.setGeometry(QtCore.QRect(20, 340, 351, 71))
        self.crossroadTB.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.crossroadTB.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.crossroadTB.setObjectName("crossroadTB")
        self.crossroadSelectTB = QtWidgets.QComboBox(parent=self.crossroadTB)
        self.crossroadSelectTB.setGeometry(QtCore.QRect(0, 0, 101, 22))
        self.crossroadSelectTB.setObjectName("crossroadSelectTB")
        self.crossroadSelectTB.addItem("")
        self.crossroadSelectTB.addItem("")
        self.crossroadData = QtWidgets.QTableWidget(parent=self.crossroadTB)
        self.crossroadData.setGeometry(QtCore.QRect(0, 20, 351, 51))
        self.crossroadData.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.crossroadData.setObjectName("crossroadData")
        self.crossroadData.setColumnCount(2)
        self.crossroadData.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.crossroadData.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.crossroadData.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.crossroadData.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.crossroadData.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.crossroadData.setItem(0, 1, item)
        self.crossroadData.horizontalHeader().setDefaultSectionSize(150)
        self.signalTB = QtWidgets.QFrame(parent=self.testBench)
        self.signalTB.setGeometry(QtCore.QRect(430, 340, 351, 71))
        self.signalTB.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.signalTB.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.signalTB.setObjectName("signalTB")
        self.signalSelectTB = QtWidgets.QComboBox(parent=self.signalTB)
        self.signalSelectTB.setGeometry(QtCore.QRect(0, 0, 101, 22))
        self.signalSelectTB.setObjectName("signalSelectTB")
        self.signalSelectTB.addItem("")
        self.signalSelectTB.addItem("")
        self.signalData = QtWidgets.QTableWidget(parent=self.signalTB)
        self.signalData.setGeometry(QtCore.QRect(0, 20, 351, 51))
        self.signalData.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.signalData.setObjectName("signalData")
        self.signalData.setColumnCount(2)
        self.signalData.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.signalData.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.signalData.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.signalData.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.signalData.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.signalData.setItem(0, 1, item)
        self.signalData.horizontalHeader().setDefaultSectionSize(150)
        self.pageSelection.addTab(self.testBench, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 898, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.pageSelection.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name.setText(_translate("MainWindow", "Track Controller"))
        __sortingEnabled = self.sectionData.isSortingEnabled()
        self.sectionData.setSortingEnabled(False)
        item = self.sectionData.item(0, 0)
        item.setText(_translate("MainWindow", "Track Section :"))
        item = self.sectionData.item(0, 1)
        item.setText(_translate("MainWindow", "A"))
        item = self.sectionData.item(1, 0)
        item.setText(_translate("MainWindow", "Section Occupation :"))
        item = self.sectionData.item(1, 1)
        item.setText(_translate("MainWindow", "Not Occupied"))
        item = self.sectionData.item(2, 0)
        item.setText(_translate("MainWindow", "Section Failure :"))
        item = self.sectionData.item(2, 1)
        item.setText(_translate("MainWindow", "No Failure"))
        self.sectionData.setSortingEnabled(__sortingEnabled)
        self.section.setItemText(0, _translate("MainWindow", "Section A"))
        self.section.setItemText(1, _translate("MainWindow", "Section B"))
        self.switchDirection.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/left/left.jpg\"/></p></body></html>"))
        self.toggleDirection.setText(_translate("MainWindow", "Toggle Direction"))
        self.switchSelect.setItemText(0, _translate("MainWindow", "Switch 1"))
        self.switchSelect.setItemText(1, _translate("MainWindow", "Switch 2"))
        self.crossroadStatus.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/crossc/crossc.jpg\"/></p></body></html>"))
        self.toggleCrossroad.setText(_translate("MainWindow", "Toggle Crossroad"))
        self.crossroadSelect.setItemText(0, _translate("MainWindow", "Crossroad 1"))
        self.crossroadSelect.setItemText(1, _translate("MainWindow", "Crossroad 2"))
        self.greenButton.setText(_translate("MainWindow", "Green"))
        self.redButton.setText(_translate("MainWindow", "Red"))
        self.signalState.setText(_translate("MainWindow", "Current Signal"))
        self.signalSelect.setItemText(0, _translate("MainWindow", "Signal 1"))
        self.signalSelect.setItemText(1, _translate("MainWindow", "Signal 2"))
        self.modeButton.setText(_translate("MainWindow", "Automatic Mode"))
        self.nextStation.setText(_translate("MainWindow", "Station ..."))
        self.statText.setText(_translate("MainWindow", "Next Station:"))
        self.pageSelection.setTabText(self.pageSelection.indexOf(self.mainPage), _translate("MainWindow", "Main Page"))
        __sortingEnabled = self.dataTB.isSortingEnabled()
        self.dataTB.setSortingEnabled(False)
        item = self.dataTB.item(0, 0)
        item.setText(_translate("MainWindow", "Track Section :"))
        item = self.dataTB.item(0, 1)
        item.setText(_translate("MainWindow", "A"))
        item = self.dataTB.item(1, 0)
        item.setText(_translate("MainWindow", "Section Occupation :"))
        item = self.dataTB.item(1, 1)
        item.setText(_translate("MainWindow", "Not Occupied"))
        item = self.dataTB.item(2, 0)
        item.setText(_translate("MainWindow", "Section Failure :"))
        item = self.dataTB.item(2, 1)
        item.setText(_translate("MainWindow", "No Failure"))
        item = self.dataTB.item(3, 0)
        item.setText(_translate("MainWindow", "Suggested Speed :"))
        item = self.dataTB.item(3, 1)
        item.setText(_translate("MainWindow", "30m/s"))
        item = self.dataTB.item(4, 0)
        item.setText(_translate("MainWindow", "Authority :"))
        item = self.dataTB.item(4, 1)
        item.setText(_translate("MainWindow", "10"))
        item = self.dataTB.item(5, 0)
        item.setText(_translate("MainWindow", "Route :"))
        item = self.dataTB.item(5, 1)
        item.setText(_translate("MainWindow", "1"))
        self.dataTB.setSortingEnabled(__sortingEnabled)
        self.sectionTB.setItemText(0, _translate("MainWindow", "Section A"))
        self.sectionTB.setItemText(1, _translate("MainWindow", "Section B"))
        self.switchSelectTB.setItemText(0, _translate("MainWindow", "Switch 1"))
        self.switchSelectTB.setItemText(1, _translate("MainWindow", "Switch 2"))
        __sortingEnabled = self.switchData.isSortingEnabled()
        self.switchData.setSortingEnabled(False)
        item = self.switchData.item(0, 0)
        item.setText(_translate("MainWindow", "Switch Status :"))
        item = self.switchData.item(0, 1)
        item.setText(_translate("MainWindow", "Left"))
        self.switchData.setSortingEnabled(__sortingEnabled)
        self.crossroadSelectTB.setItemText(0, _translate("MainWindow", "Crossroad 1"))
        self.crossroadSelectTB.setItemText(1, _translate("MainWindow", "Crossroad 2"))
        __sortingEnabled = self.crossroadData.isSortingEnabled()
        self.crossroadData.setSortingEnabled(False)
        item = self.crossroadData.item(0, 0)
        item.setText(_translate("MainWindow", "Crossroad Status :"))
        item = self.crossroadData.item(0, 1)
        item.setText(_translate("MainWindow", "Open"))
        self.crossroadData.setSortingEnabled(__sortingEnabled)
        self.signalSelectTB.setItemText(0, _translate("MainWindow", "Signal 1"))
        self.signalSelectTB.setItemText(1, _translate("MainWindow", "Signal 2"))
        __sortingEnabled = self.signalData.isSortingEnabled()
        self.signalData.setSortingEnabled(False)
        item = self.signalData.item(0, 0)
        item.setText(_translate("MainWindow", "Signal Status :"))
        item = self.signalData.item(0, 1)
        item.setText(_translate("MainWindow", "Green"))
        self.signalData.setSortingEnabled(__sortingEnabled)
        self.pageSelection.setTabText(self.pageSelection.indexOf(self.testBench), _translate("MainWindow", "Test Bench"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
