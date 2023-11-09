# Form implementation generated from reading ui file 'TrackControllerTB.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(912, 729)
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
        self.tab = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tab.setGeometry(QtCore.QRect(10, 40, 891, 661))
        self.tab.setObjectName("tab")
        self.main = QtWidgets.QWidget()
        self.main.setObjectName("main")
        self.frame = QtWidgets.QFrame(parent=self.main)
        self.frame.setGeometry(QtCore.QRect(0, 0, 881, 631))
        self.frame.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.signalFrame = QtWidgets.QFrame(parent=self.frame)
        self.signalFrame.setGeometry(QtCore.QRect(420, 350, 351, 271))
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
        self.signalState.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.signalState.setAutoDefault(False)
        self.signalState.setObjectName("signalState")
        self.switchFrame = QtWidgets.QFrame(parent=self.frame)
        self.switchFrame.setGeometry(QtCore.QRect(420, 50, 351, 271))
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
        self.leftBlock = QtWidgets.QLabel(parent=self.switchFrame)
        self.leftBlock.setGeometry(QtCore.QRect(10, 140, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.leftBlock.setFont(font)
        self.leftBlock.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.leftBlock.setLineWidth(1)
        self.leftBlock.setMidLineWidth(0)
        self.leftBlock.setObjectName("leftBlock")
        self.rightBlock = QtWidgets.QLabel(parent=self.switchFrame)
        self.rightBlock.setGeometry(QtCore.QRect(240, 140, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rightBlock.setFont(font)
        self.rightBlock.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.rightBlock.setLineWidth(1)
        self.rightBlock.setMidLineWidth(0)
        self.rightBlock.setObjectName("rightBlock")
        self.modeButton = QtWidgets.QRadioButton(parent=self.frame)
        self.modeButton.setGeometry(QtCore.QRect(650, 20, 121, 20))
        self.modeButton.setObjectName("modeButton")
        self.dataFrame = QtWidgets.QFrame(parent=self.frame)
        self.dataFrame.setGeometry(QtCore.QRect(10, 50, 351, 271))
        self.dataFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dataFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.dataFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.dataFrame.setObjectName("dataFrame")
        self.waysideData = QtWidgets.QLabel(parent=self.dataFrame)
        self.waysideData.setGeometry(QtCore.QRect(100, 10, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.waysideData.setFont(font)
        self.waysideData.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.waysideData.setLineWidth(1)
        self.waysideData.setMidLineWidth(0)
        self.waysideData.setObjectName("waysideData")
        self.waysideLabel = QtWidgets.QLabel(parent=self.dataFrame)
        self.waysideLabel.setGeometry(QtCore.QRect(0, 0, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.waysideLabel.setFont(font)
        self.waysideLabel.setLineWidth(1)
        self.waysideLabel.setMidLineWidth(0)
        self.waysideLabel.setObjectName("waysideLabel")
        self.blockData = QtWidgets.QLabel(parent=self.dataFrame)
        self.blockData.setGeometry(QtCore.QRect(100, 40, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.blockData.setFont(font)
        self.blockData.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.blockData.setLineWidth(1)
        self.blockData.setMidLineWidth(0)
        self.blockData.setObjectName("blockData")
        self.blockLabel = QtWidgets.QLabel(parent=self.dataFrame)
        self.blockLabel.setGeometry(QtCore.QRect(0, 30, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.blockLabel.setFont(font)
        self.blockLabel.setLineWidth(1)
        self.blockLabel.setMidLineWidth(0)
        self.blockLabel.setObjectName("blockLabel")
        self.failureLabel = QtWidgets.QLabel(parent=self.dataFrame)
        self.failureLabel.setGeometry(QtCore.QRect(0, 60, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.failureLabel.setFont(font)
        self.failureLabel.setLineWidth(1)
        self.failureLabel.setMidLineWidth(0)
        self.failureLabel.setObjectName("failureLabel")
        self.failureData = QtWidgets.QLabel(parent=self.dataFrame)
        self.failureData.setGeometry(QtCore.QRect(100, 70, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.failureData.setFont(font)
        self.failureData.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.failureData.setLineWidth(1)
        self.failureData.setMidLineWidth(0)
        self.failureData.setObjectName("failureData")
        self.wayside = QtWidgets.QComboBox(parent=self.frame)
        self.wayside.setGeometry(QtCore.QRect(20, 20, 101, 22))
        self.wayside.setObjectName("wayside")
        self.crossroadFrame = QtWidgets.QFrame(parent=self.frame)
        self.crossroadFrame.setGeometry(QtCore.QRect(10, 350, 351, 271))
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
        self.block = QtWidgets.QComboBox(parent=self.frame)
        self.block.setGeometry(QtCore.QRect(140, 20, 101, 22))
        self.block.setObjectName("block")
        self.occupationData = QtWidgets.QListWidget(parent=self.frame)
        self.occupationData.setEnabled(False)
        self.occupationData.setGeometry(QtCore.QRect(780, 100, 91, 521))
        self.occupationData.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.occupationData.setObjectName("occupationData")
        self.occupationLabel = QtWidgets.QLabel(parent=self.frame)
        self.occupationLabel.setGeometry(QtCore.QRect(780, 70, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.occupationLabel.setFont(font)
        self.occupationLabel.setLineWidth(1)
        self.occupationLabel.setMidLineWidth(0)
        self.occupationLabel.setObjectName("occupationLabel")
        self.tab.addTab(self.main, "")
        self.TB = QtWidgets.QWidget()
        self.TB.setObjectName("TB")
        self.frameTB = QtWidgets.QFrame(parent=self.TB)
        self.frameTB.setGeometry(QtCore.QRect(0, 0, 781, 631))
        self.frameTB.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.frameTB.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameTB.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameTB.setObjectName("frameTB")
        self.waysideTB = QtWidgets.QComboBox(parent=self.frameTB)
        self.waysideTB.setGeometry(QtCore.QRect(20, 20, 101, 22))
        self.waysideTB.setObjectName("waysideTB")
        self.blockTB = QtWidgets.QComboBox(parent=self.frameTB)
        self.blockTB.setGeometry(QtCore.QRect(140, 20, 101, 22))
        self.blockTB.setObjectName("blockTB")
        self.occupationTB = QtWidgets.QCheckBox(parent=self.frameTB)
        self.occupationTB.setGeometry(QtCore.QRect(30, 60, 91, 20))
        self.occupationTB.setObjectName("occupationTB")
        self.authorityLabelTB = QtWidgets.QLabel(parent=self.frameTB)
        self.authorityLabelTB.setGeometry(QtCore.QRect(30, 80, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.authorityLabelTB.setFont(font)
        self.authorityLabelTB.setLineWidth(1)
        self.authorityLabelTB.setMidLineWidth(0)
        self.authorityLabelTB.setObjectName("authorityLabelTB")
        self.authorityDataTB = QtWidgets.QLineEdit(parent=self.frameTB)
        self.authorityDataTB.setGeometry(QtCore.QRect(90, 80, 113, 22))
        self.authorityDataTB.setObjectName("authorityDataTB")
        self.tab.addTab(self.TB, "")
        self.tab.raise_()
        self.name.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 912, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name.setText(_translate("MainWindow", "Track Controller"))
        self.greenButton.setText(_translate("MainWindow", "Green"))
        self.redButton.setText(_translate("MainWindow", "Red"))
        self.signalState.setText(_translate("MainWindow", "Current Signal"))
        self.switchDirection.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/left/left.jpg\"/></p></body></html>"))
        self.toggleDirection.setText(_translate("MainWindow", "Toggle Direction"))
        self.leftBlock.setText(_translate("MainWindow", "Left"))
        self.rightBlock.setText(_translate("MainWindow", "Right"))
        self.modeButton.setText(_translate("MainWindow", "Automatic Mode"))
        self.waysideData.setText(_translate("MainWindow", "..."))
        self.waysideLabel.setText(_translate("MainWindow", "Wayside:"))
        self.blockData.setText(_translate("MainWindow", "..."))
        self.blockLabel.setText(_translate("MainWindow", "Block:"))
        self.failureLabel.setText(_translate("MainWindow", "Failures:"))
        self.failureData.setText(_translate("MainWindow", "..."))
        self.crossroadStatus.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/crossc/crossc.jpg\"/></p></body></html>"))
        self.toggleCrossroad.setText(_translate("MainWindow", "Toggle Crossroad"))
        self.occupationLabel.setText(_translate("MainWindow", "Occupied Blocks"))
        self.tab.setTabText(self.tab.indexOf(self.main), _translate("MainWindow", "Main"))
        self.occupationTB.setText(_translate("MainWindow", "Occupation"))
        self.authorityLabelTB.setText(_translate("MainWindow", "Authority:"))
        self.tab.setTabText(self.tab.indexOf(self.TB), _translate("MainWindow", "TB"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
