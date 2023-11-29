from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog
import subprocess

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(916, 346)
        self.tabWidget = QtWidgets.QTabWidget(parent=Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 50, 901, 251))
        self.tabWidget.setObjectName("tabWidget")


        #Automatic Tab
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listWidget_3 = QtWidgets.QListWidget(parent=self.tab_2)
        self.listWidget_3.setGeometry(QtCore.QRect(10, 20, 121, 61))
        self.listWidget_3.setObjectName("listWidget_3") #Line Selector
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)

        self.comboBox_5 = QtWidgets.QComboBox(parent=self.tab_2)
        self.comboBox_5.setGeometry(QtCore.QRect(170, 70, 101, 22))
        self.comboBox_5.setObjectName("comboBox_5") #Light Selector
        self.comboBox_5.addItem("")
        self.comboBox_5.setDisabled(True)

        self.comboBox_6 = QtWidgets.QComboBox(parent=self.tab_2)
        self.comboBox_6.setGeometry(QtCore.QRect(330, 70, 121, 22))
        self.comboBox_6.setObjectName("comboBox_6") #Crossroad Selector
        self.comboBox_6.addItem("")
        self.comboBox_6.setDisabled(True)

        self.comboBox_7 = QtWidgets.QComboBox(parent=self.tab_2)
        self.comboBox_7.setGeometry(QtCore.QRect(500, 70, 101, 22))
        self.comboBox_7.setObjectName("comboBox_7") #Switch Selector
        self.comboBox_7.addItem("")
        self.comboBox_7.setDisabled(True)

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

        self.comboBox = QtWidgets.QComboBox(parent=self.tab_2)
        self.comboBox.setGeometry(QtCore.QRect(10, 110, 121, 22))
        self.comboBox.setObjectName("comboBox") #Wayside Selector
        self.comboBox.addItem("")
        self.comboBox.setDisabled(True)



        #Manual Tab
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.listWidget = QtWidgets.QListWidget(parent=self.tab)
        self.listWidget.setGeometry(QtCore.QRect(10, 30, 121, 61))
        self.listWidget.setObjectName("listWidget") #Line Selector
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
        self.comboBox_2.setDisabled(True)

        self.pushButton = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton.setGeometry(QtCore.QRect(320, 120, 101, 51))
        self.pushButton.setObjectName("pushButton") #Toggle Crossroad
        self.pushButton.setDisabled(True)

        self.comboBox_3 = QtWidgets.QComboBox(parent=self.tab)
        self.comboBox_3.setGeometry(QtCore.QRect(310, 60, 121, 22))
        self.comboBox_3.setObjectName("comboBox_3")#Select Crossroad
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
        self.comboBox_4.setDisabled(True)

        self.listWidget_5 = QtWidgets.QListWidget(parent=self.tab)
        self.listWidget_5.setGeometry(QtCore.QRect(630, 50, 81, 131))
        self.listWidget_5.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listWidget_5.setObjectName("listWidget_5")#Blocks Occupied List

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

        self.comboBox_12 = QtWidgets.QComboBox(parent=self.tab)
        self.comboBox_12.setGeometry(QtCore.QRect(10, 120, 121, 22))
        self.comboBox_12.setObjectName("comboBox_12") #Wayside Selector
        self.comboBox_12.addItem("")
        self.comboBox_12.setDisabled(True)



        #Test Bench
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.listWidget_9 = QtWidgets.QListWidget(parent=self.tab_3)
        self.listWidget_9.setGeometry(QtCore.QRect(10, 10, 121, 61))
        self.listWidget_9.setObjectName("listWidget_9")#Line Selector
        item = QtWidgets.QListWidgetItem()
        self.listWidget_9.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_9.addItem(item)

        self.comboBox_8 = QtWidgets.QComboBox(parent=self.tab_3)
        self.comboBox_8.setGeometry(QtCore.QRect(310, 110, 101, 22))
        self.comboBox_8.setObjectName("comboBox_8") #Track selections
        self.comboBox_8.addItem("")
        self.comboBox_8.setDisabled(True)

        self.pushButton_4 = QtWidgets.QPushButton(parent=self.tab_3)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 160, 111, 51))
        self.pushButton_4.setObjectName("pushButton_4") #Toggle Occupancy
        self.pushButton_4.setDisabled(True)

        self.comboBox_9 = QtWidgets.QComboBox(parent=self.tab_3)
        self.comboBox_9.setGeometry(QtCore.QRect(170, 10, 101, 22))
        self.comboBox_9.setObjectName("comboBox_9") #Select Light
        self.comboBox_9.addItem("")
        self.comboBox_9.setDisabled(True)

        self.comboBox_10 = QtWidgets.QComboBox(parent=self.tab_3)
        self.comboBox_10.setGeometry(QtCore.QRect(310, 10, 121, 22))
        self.comboBox_10.setObjectName("comboBox_10") #Select Crossroad
        self.comboBox_10.addItem("")
        self.comboBox_10.setDisabled(True)

        self.comboBox_11 = QtWidgets.QComboBox(parent=self.tab_3)
        self.comboBox_11.setGeometry(QtCore.QRect(470, 10, 101, 22))
        self.comboBox_11.setObjectName("comboBox_11") #Select Switch
        self.comboBox_11.addItem("")
        self.comboBox_11.setDisabled(True)

        self.listWidget_4 = QtWidgets.QListWidget(parent=self.tab_3)
        self.listWidget_4.setGeometry(QtCore.QRect(170, 50, 91, 41))
        self.listWidget_4.setObjectName("listWidget_4")#Select Light Color
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
        self.listWidget_10.setDisabled(True)

        self.listWidget_11 = QtWidgets.QListWidget(parent=self.tab_3)
        self.listWidget_11.setGeometry(QtCore.QRect(470, 50, 91, 41))
        self.listWidget_11.setObjectName("listWidget_11") #Select Switch to change to
        self.listWidget_11.setDisabled(True)

        self.pushButton_5 = QtWidgets.QPushButton(parent=self.tab_3)
        self.pushButton_5.setGeometry(QtCore.QRect(400, 160, 111, 51))
        self.pushButton_5.setObjectName("pushButton_5")#Toggle Track Failure
        self.pushButton_5.setDisabled(True)

        self.comboBox_13 = QtWidgets.QComboBox(parent=self.tab_3)
        self.comboBox_13.setGeometry(QtCore.QRect(10, 110, 121, 22))
        self.comboBox_13.setObjectName("comboBox_13") #Wayside Selector
        self.comboBox_13.addItem("")
        self.comboBox_13.setDisabled(True)


        #Dont Change below
        self.label_3 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(670, 0, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")#Inputs for CTC label (No need to edit)
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


        #Whole UI stuff
        self.tabWidget.addTab(self.tab_3, "")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 10, 201, 41))
        self.pushButton_3.setObjectName("pushButton_3") #Open PLC code button

        self.label_4 = QtWidgets.QLabel(parent=Form) #File location label
        self.label_4.setGeometry(QtCore.QRect(220, 10, 650, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")


        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)



    def retranslateUi(self, Form):
        #Automatic Mode UI
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        item = self.listWidget_3.item(0)
        item.setText(_translate("Form", "Red Line"))
        item = self.listWidget_3.item(1)
        item.setText(_translate("Form", "Green Line"))
        self.listWidget_3.setSortingEnabled(__sortingEnabled)

        self.comboBox_5.setItemText(0, _translate("Form", "Select Light"))
        self.comboBox_6.setItemText(0, _translate("Form", "Select Crossroad"))
        self.comboBox_7.setItemText(0, _translate("Form", "Select Switch"))
        self.label_12.setText(_translate("Form", "Blocks Occupied"))
        self.label_13.setText(_translate("Form", "Track Failures"))
        self.comboBox.setItemText(0, _translate("Form", "Select Wayside"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Main Page - Automatic"))


        #Manual Mode UI
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "Red Line"))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "Green Line"))
        self.listWidget.setSortingEnabled(__sortingEnabled)

        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("Form", "Red"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("Form", "Green"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.comboBox_2.setItemText(0, _translate("Form", "Select Light"))
        self.pushButton.setText(_translate("Form", "Toggle Crossroad"))
        self.comboBox_3.setItemText(0, _translate("Form", "Select Crossroad"))
        self.pushButton_2.setText(_translate("Form", "Toggle Switch"))
        self.comboBox_4.setItemText(0, _translate("Form", "Select Switch"))
        self.label_10.setText(_translate("Form", "Blocks Occupied"))
        self.label_11.setText(_translate("Form", "Track Failures"))
        self.comboBox_12.setItemText(0, _translate("Form", "Select Wayside"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Main Page - Manual"))


        #Test Bench
        __sortingEnabled = self.listWidget_9.isSortingEnabled()
        self.listWidget_9.setSortingEnabled(False)
        item = self.listWidget_9.item(0)
        item.setText(_translate("Form", "Red Line"))
        item = self.listWidget_9.item(1)
        item.setText(_translate("Form", "Green Line"))
        self.listWidget_9.setSortingEnabled(__sortingEnabled)

        self.comboBox_8.setItemText(0, _translate("Form", "Track Selection"))
        self.pushButton_4.setText(_translate("Form", "Toggle Occupancy"))
        self.comboBox_9.setItemText(0, _translate("Form", "Select Light"))
        self.comboBox_10.setItemText(0, _translate("Form", "Select Crossroad"))
        self.comboBox_11.setItemText(0, _translate("Form", "Select Switch"))
        self.comboBox_13.setItemText(0, _translate("Form", "Select Wayside"))

        __sortingEnabled = self.listWidget_4.isSortingEnabled()
        self.listWidget_4.setSortingEnabled(False)
        item = self.listWidget_4.item(0)
        item.setText(_translate("Form", "Red"))
        item = self.listWidget_4.item(1)
        item.setText(_translate("Form", "Green"))
        self.listWidget_4.setSortingEnabled(__sortingEnabled)

        __sortingEnabled = self.listWidget_10.isSortingEnabled()
        self.listWidget_10.setSortingEnabled(False)
        item = self.listWidget_10.item(0)
        item.setText(_translate("Form", "On"))
        item = self.listWidget_10.item(1)
        item.setText(_translate("Form", "Off"))
        self.listWidget_10.setSortingEnabled(__sortingEnabled)

        self.pushButton_5.setText(_translate("Form", "Toggle Track Failure"))

        __sortingEnabled = self.listWidget_11.isSortingEnabled()
        self.listWidget_11.setSortingEnabled(__sortingEnabled)
        switch = self.listWidget_11.item(0)
        switch = self.listWidget_11.item(1)

        #Below for displaying CTC stuff
        self.label_3.setText(_translate("Form", "Inputs from CTC"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "Suggested Speed"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "Authority"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Values"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "50 km/h"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Form", "60 m"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)


        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Test Bench"))

        #PLC Code opener
        self.pushButton_3.setText(_translate("Form", "Open PLC Code"))
        self.label_4.setText("PLC Path Location")
