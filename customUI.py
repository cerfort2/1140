# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1029, 755)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1011, 731))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.comboBox_3 = QtWidgets.QComboBox(parent=self.tab)
        self.comboBox_3.setGeometry(QtCore.QRect(730, 40, 271, 32))
        self.comboBox_3.setObjectName("comboBox_3")
        self.tableWidget_6 = QtWidgets.QTableWidget(parent=self.tab)
        self.tableWidget_6.setGeometry(QtCore.QRect(140, 580, 231, 81))
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(1)
        self.tableWidget_6.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEditable|QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.tableWidget_6.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEditable|QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.tableWidget_6.setItem(1, 0, item)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 181, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget_7 = QtWidgets.QTableWidget(parent=self.tab)
        self.tableWidget_7.setGeometry(QtCore.QRect(390, 580, 351, 111))
        self.tableWidget_7.setObjectName("tableWidget_7")
        self.tableWidget_7.setColumnCount(1)
        self.tableWidget_7.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEditable|QtCore.Qt.ItemFlag.ItemIsDragEnabled|QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.tableWidget_7.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEditable|QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.tableWidget_7.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEditable|QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.tableWidget_7.setItem(2, 0, item)
        self.label_2 = QtWidgets.QLabel(parent=self.tab)
        self.label_2.setGeometry(QtCore.QRect(550, 80, 181, 31))
        self.label_2.setObjectName("label_2")
        self.tableWidget_3 = QtWidgets.QTableWidget(parent=self.tab)
        self.tableWidget_3.setGeometry(QtCore.QRect(750, 110, 241, 441))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(1)
        self.tableWidget_3.setRowCount(14)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        icon = QtGui.QIcon.fromTheme("accessories-calculator")
        item.setIcon(icon)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEditable|QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.tableWidget_3.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.tableWidget_3.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.tableWidget_3.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.tableWidget_3.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.tableWidget_3.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.tableWidget_3.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.tableWidget_3.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.tableWidget_3.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.tableWidget_3.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.tableWidget_3.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.tableWidget_3.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.tableWidget_3.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.tableWidget_3.setItem(12, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.tableWidget_3.setItem(13, 0, item)
        self.listWidget_2 = QtWidgets.QListWidget(parent=self.tab)
        self.listWidget_2.setGeometry(QtCore.QRect(545, 110, 191, 441))
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
        self.listWidget_2.addItem(item)
        self.tableWidget_8 = QtWidgets.QTableWidget(parent=self.tab)
        self.tableWidget_8.setGeometry(QtCore.QRect(760, 580, 231, 111))
        self.tableWidget_8.setObjectName("tableWidget_8")
        self.tableWidget_8.setColumnCount(1)
        self.tableWidget_8.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEditable|QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.tableWidget_8.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEditable|QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.tableWidget_8.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEditable|QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.tableWidget_8.setItem(2, 0, item)
        self.comboBox_4 = QtWidgets.QComboBox(parent=self.tab)
        self.comboBox_4.setGeometry(QtCore.QRect(730, 70, 271, 32))
        self.comboBox_4.setObjectName("comboBox_4")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(450, 100, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(parent=self.tab_2)
        self.label.setGeometry(QtCore.QRect(300, 30, 461, 20))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(440, 70, 141, 16))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget_6.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Crossroad Selected:"))
        item = self.tableWidget_6.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Open?"))
        __sortingEnabled = self.tableWidget_6.isSortingEnabled()
        self.tableWidget_6.setSortingEnabled(False)
        self.tableWidget_6.setSortingEnabled(__sortingEnabled)
        self.pushButton_2.setText(_translate("MainWindow", "Upload Track Layout .csv"))
        item = self.tableWidget_7.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Station Selected:"))
        item = self.tableWidget_7.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Number of Tickets Sold:"))
        item = self.tableWidget_7.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Station Side"))
        __sortingEnabled = self.tableWidget_7.isSortingEnabled()
        self.tableWidget_7.setSortingEnabled(False)
        self.tableWidget_7.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("MainWindow", "Occupied Blocks on this Line"))
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Current Block Selected"))
        item = self.tableWidget_3.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Occupied?"))
        item = self.tableWidget_3.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Block Length"))
        item = self.tableWidget_3.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Block Grade"))
        item = self.tableWidget_3.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Elevation"))
        item = self.tableWidget_3.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Speed Limit"))
        item = self.tableWidget_3.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "Station?"))
        item = self.tableWidget_3.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "Switch?"))
        item = self.tableWidget_3.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "Underground?"))
        item = self.tableWidget_3.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "Crossroad?"))
        item = self.tableWidget_3.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "Track Heater?"))
        item = self.tableWidget_3.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "Broken Rail?"))
        item = self.tableWidget_3.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "Track Circuit Failure?"))
        item = self.tableWidget_3.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "Power Failure?"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Status"))
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget_8.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Switch Selected:"))
        item = self.tableWidget_8.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Block Pointing To:"))
        item = self.tableWidget_8.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Block Pointing Away:"))
        __sortingEnabled = self.tableWidget_8.isSortingEnabled()
        self.tableWidget_8.setSortingEnabled(False)
        self.tableWidget_8.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Main Page"))
        self.label.setText(_translate("MainWindow", "Enter the Line, and blocks to be occupied, using commas and no spaces:"))
        self.label_3.setText(_translate("MainWindow", "Ex: Red Line,A2,A3,A4"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Testbench"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
