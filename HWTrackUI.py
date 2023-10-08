from PyQt6 import QtCore, QtGui, QtWidgets
from UI_Breadboard_Class import Operations

operate = Operations() #Class to perform operations on the breadboard

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(933, 229)
        MainWindow.setStyleSheet("QCheckBox\n"
"{\n"
"    border: 3px solid #5A5A5A;\n"
"}\n"
"QMainWindow\n"
"{\n"
"    \n"
"    color: rgb(193, 69, 255);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QtCore.QRect(750, 0, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.checkBox.setFont(font)
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")

        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 0, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 70, 71, 91))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)

        self.comboBox_2 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 60, 101, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setDisabled(True)

        self.comboBox_3 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(320, 60, 121, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setDisabled(True)

        self.comboBox_4 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(530, 60, 101, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setDisabled(True)

        self.listWidget_2 = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(150, 100, 91, 61))
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_2.setDisabled(True)

        item = QtWidgets.QListWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 225, 75))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.listWidget_2.addItem(item)

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 110, 101, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setDisabled(True)

        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 110, 101, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setDisabled(True)

        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(710, 70, 211, 81))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.setDisabled(True)

        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(300, 0, 264, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.NoTextInteraction)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_2.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.NoTextInteraction)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 933, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HW Track Controller UI"))


        self.checkBox.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.checkBox.setText(_translate("MainWindow", "Manual Mode"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Main Page"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Test Bench"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)



        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Wayside 1"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Wayside 2"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Wayside 3"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.listWidget.itemClicked.connect(self.checkList)



        self.comboBox_2.setItemText(0, _translate("MainWindow", "Select Light"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Light 1"))
        self.comboBox_2.currentIndexChanged.connect(self.lightChange)

        self.comboBox_3.setItemText(0, _translate("MainWindow", "Select Crossroad"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Crossroad 1"))
        self.comboBox_3.currentIndexChanged.connect(self.crossChange)

        self.comboBox_4.setItemText(0, _translate("MainWindow", "Select Switch"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Switch 1"))
        self.comboBox_4.currentIndexChanged.connect(self.switchChange)

        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)


        red = self.listWidget_2.item(0)
        red.setText(_translate("MainWindow", "Red"))
        red = self.listWidget_2.item(1)
        red.setText(_translate("MainWindow", "Yellow"))
        red = self.listWidget_2.item(2)
        red.setText(_translate("MainWindow", "Green"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.listWidget_2.itemClicked.connect(lambda item=red: operate.changeLight(item.text()))


        self.pushButton.setText(_translate("MainWindow", "Toggle Crossroad"))
        self.pushButton.clicked.connect(lambda: operate.changeCrossroad())

        self.pushButton_2.setText(_translate("MainWindow", "Toggle Switch"))
        self.pushButton_2.clicked.connect(lambda: operate.changeSwitch())


        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Block Occupancy"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Track Failure"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Status"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:16pt; text-decoration: underline;\">Next Station:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">Station Name</span></p></body></html>"))


    def crossChange(self): #Checks if still selecting crossroad to grey out button
        if self.comboBox_3.currentText() == "Select Crossroad":
            self.pushButton.setDisabled(True)
        else:
            self.pushButton.setDisabled(False)

    def switchChange(self): #Checks if still selecting switch to grey out button
        if self.comboBox_4.currentText() == "Select Switch":
            self.pushButton_2.setDisabled(True)
        else:
            self.pushButton_2.setDisabled(False)

    def lightChange(self): #Checks if still selecting light to grey out list
        if self.comboBox_2.currentText() == "Select Light":
            self.listWidget_2.setDisabled(True)
        else:
            self.listWidget_2.setDisabled(False)
    
    def checkList(self): #Checks if a wayside is selected or not to grey out combo boxes or not
        if self.listWidget.currentItem() is not None:
            self.enableCombos()

    def enableCombos(self): #enables all the combo boxes
        for combo_box in [self.comboBox_2, self.comboBox_3, self.comboBox_4, self.tableWidget]:
            combo_box.setEnabled(True)
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
