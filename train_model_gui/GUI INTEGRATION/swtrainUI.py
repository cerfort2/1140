# Form implementation generated from reading ui file '.\SoftwareTrainController1.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1004, 584)
        self.tabWidget = QtWidgets.QTabWidget(parent=Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 1001, 571))
        self.tabWidget.setIconSize(QtCore.QSize(32, 32))
        self.tabWidget.setObjectName("tabWidget")
        self.manual = QtWidgets.QWidget()
        self.manual.setObjectName("manual")
        self.rightdoor = QtWidgets.QCheckBox(parent=self.manual)
        self.rightdoor.setGeometry(QtCore.QRect(340, 270, 111, 21))
        self.rightdoor.setObjectName("rightdoor")
        self.internallight = QtWidgets.QCheckBox(parent=self.manual)
        self.internallight.setGeometry(QtCore.QRect(340, 470, 121, 21))
        self.internallight.setObjectName("internallight")
        self.externallight = QtWidgets.QCheckBox(parent=self.manual)
        self.externallight.setGeometry(QtCore.QRect(340, 490, 121, 21))
        self.externallight.setObjectName("externallight")
        self.textEdit = QtWidgets.QTextEdit(parent=self.manual)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(320, 430, 161, 41))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_3 = QtWidgets.QTextEdit(parent=self.manual)
        self.textEdit_3.setEnabled(False)
        self.textEdit_3.setGeometry(QtCore.QRect(320, 230, 161, 41))
        self.textEdit_3.setObjectName("textEdit_3")
        self.ebrake = QtWidgets.QPushButton(parent=self.manual)
        self.ebrake.setGeometry(QtCore.QRect(750, 10, 231, 101))
        self.ebrake.setObjectName("ebrake")
        self.textEdit_2 = QtWidgets.QTextEdit(parent=self.manual)
        self.textEdit_2.setEnabled(False)
        self.textEdit_2.setGeometry(QtCore.QRect(320, 140, 171, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.announcement = QtWidgets.QComboBox(parent=self.manual)
        self.announcement.setEnabled(True)
        self.announcement.setGeometry(QtCore.QRect(320, 180, 171, 31))
        self.announcement.setEditable(True)
        self.announcement.setDuplicatesEnabled(False)
        self.announcement.setObjectName("announcement")
        self.manualtrainfailures = QtWidgets.QTextEdit(parent=self.manual)
        self.manualtrainfailures.setEnabled(False)
        self.manualtrainfailures.setGeometry(QtCore.QRect(320, 320, 161, 41))
        self.manualtrainfailures.setObjectName("manualtrainfailures")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(parent=self.manual)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 10, 291, 521))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.temp = QtWidgets.QSpinBox(parent=self.gridLayoutWidget_2)
        self.temp.setWrapping(False)
        self.temp.setFrame(True)
        self.temp.setObjectName("temp")
        self.gridLayout_2.addWidget(self.temp, 12, 2, 1, 1)
        self.textEdit_10 = QtWidgets.QTextEdit(parent=self.gridLayoutWidget_2)
        self.textEdit_10.setEnabled(False)
        self.textEdit_10.setObjectName("textEdit_10")
        self.gridLayout_2.addWidget(self.textEdit_10, 0, 0, 1, 1)
        self.textEdit_4 = QtWidgets.QTextEdit(parent=self.gridLayoutWidget_2)
        self.textEdit_4.setEnabled(False)
        self.textEdit_4.setObjectName("textEdit_4")
        self.gridLayout_2.addWidget(self.textEdit_4, 2, 0, 1, 1)
        self.speedlimit = QtWidgets.QLCDNumber(parent=self.gridLayoutWidget_2)
        self.speedlimit.setObjectName("speedlimit")
        self.gridLayout_2.addWidget(self.speedlimit, 2, 2, 1, 1)
        self.textEdit_15 = QtWidgets.QTextEdit(parent=self.gridLayoutWidget_2)
        self.textEdit_15.setEnabled(False)
        self.textEdit_15.setObjectName("textEdit_15")
        self.gridLayout_2.addWidget(self.textEdit_15, 6, 0, 1, 1)
        self.authority = QtWidgets.QLCDNumber(parent=self.gridLayoutWidget_2)
        self.authority.setObjectName("authority")
        self.gridLayout_2.addWidget(self.authority, 6, 2, 1, 1)
        self.time = QtWidgets.QDateTimeEdit(parent=self.gridLayoutWidget_2)
        self.time.setEnabled(False)
        self.time.setObjectName("time")
        self.gridLayout_2.addWidget(self.time, 0, 2, 1, 1)
        self.textEdit_8 = QtWidgets.QTextEdit(parent=self.gridLayoutWidget_2)
        self.textEdit_8.setEnabled(False)
        self.textEdit_8.setObjectName("textEdit_8")
        self.gridLayout_2.addWidget(self.textEdit_8, 12, 0, 1, 1)
        self.nextstop = QtWidgets.QTextEdit(parent=self.gridLayoutWidget_2)
        self.nextstop.setEnabled(False)
        self.nextstop.setObjectName("nextstop")
        self.gridLayout_2.addWidget(self.nextstop, 1, 2, 1, 1)
        self.amanualnextstop = QtWidgets.QTextEdit(parent=self.gridLayoutWidget_2)
        self.amanualnextstop.setEnabled(False)
        self.amanualnextstop.setObjectName("amanualnextstop")
        self.gridLayout_2.addWidget(self.amanualnextstop, 1, 0, 1, 1)
        self.brakefailure = QtWidgets.QCheckBox(parent=self.manual)
        self.brakefailure.setEnabled(False)
        self.brakefailure.setGeometry(QtCore.QRect(340, 360, 91, 20))
        self.brakefailure.setObjectName("brakefailure")
        self.enginefailure = QtWidgets.QCheckBox(parent=self.manual)
        self.enginefailure.setEnabled(False)
        self.enginefailure.setGeometry(QtCore.QRect(340, 380, 101, 20))
        self.enginefailure.setObjectName("enginefailure")
        self.signalfailure = QtWidgets.QCheckBox(parent=self.manual)
        self.signalfailure.setEnabled(False)
        self.signalfailure.setGeometry(QtCore.QRect(340, 400, 91, 20))
        self.signalfailure.setObjectName("signalfailure")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(parent=self.manual)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(800, 140, 191, 331))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.amanualki = QtWidgets.QTextEdit(parent=self.gridLayoutWidget_5)
        self.amanualki.setEnabled(False)
        self.amanualki.setObjectName("amanualki")
        self.gridLayout_5.addWidget(self.amanualki, 1, 0, 1, 1)
        self.kp = QtWidgets.QSpinBox(parent=self.gridLayoutWidget_5)
        self.kp.setObjectName("kp")
        self.gridLayout_5.addWidget(self.kp, 2, 1, 1, 1)
        self.ki = QtWidgets.QSpinBox(parent=self.gridLayoutWidget_5)
        self.ki.setObjectName("ki")
        self.gridLayout_5.addWidget(self.ki, 1, 1, 1, 1)
        self.amanualkp = QtWidgets.QTextEdit(parent=self.gridLayoutWidget_5)
        self.amanualkp.setEnabled(False)
        self.amanualkp.setObjectName("amanualkp")
        self.gridLayout_5.addWidget(self.amanualkp, 2, 0, 1, 1)
        self.apowertext = QtWidgets.QTextEdit(parent=self.gridLayoutWidget_5)
        self.apowertext.setEnabled(False)
        self.apowertext.setObjectName("apowertext")
        self.gridLayout_5.addWidget(self.apowertext, 0, 0, 1, 1)
        self.power = QtWidgets.QLCDNumber(parent=self.gridLayoutWidget_5)
        self.power.setObjectName("power")
        self.gridLayout_5.addWidget(self.power, 0, 1, 1, 1)
        self.textEdit_17 = QtWidgets.QTextEdit(parent=self.manual)
        self.textEdit_17.setEnabled(False)
        self.textEdit_17.setGeometry(QtCore.QRect(320, 10, 171, 61))
        self.textEdit_17.setAutoFillBackground(False)
        self.textEdit_17.setObjectName("textEdit_17")
        self.mode = QtWidgets.QComboBox(parent=self.manual)
        self.mode.setGeometry(QtCore.QRect(320, 70, 171, 51))
        self.mode.setObjectName("mode")
        self.mode.addItem("")
        self.mode.addItem("")
        self.textEdit_9 = QtWidgets.QTextEdit(parent=self.manual)
        self.textEdit_9.setEnabled(False)
        self.textEdit_9.setGeometry(QtCore.QRect(520, 150, 181, 51))
        self.textEdit_9.setObjectName("textEdit_9")
        self.gridLayoutWidget_7 = QtWidgets.QWidget(parent=self.manual)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(500, 260, 281, 231))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.textEdit_11 = QtWidgets.QTextEdit(parent=self.gridLayoutWidget_7)
        self.textEdit_11.setEnabled(False)
        self.textEdit_11.setObjectName("textEdit_11")
        self.gridLayout_7.addWidget(self.textEdit_11, 1, 0, 1, 1)
        self.amanualspeedtext = QtWidgets.QTextEdit(parent=self.gridLayoutWidget_7)
        self.amanualspeedtext.setEnabled(False)
        self.amanualspeedtext.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.amanualspeedtext.setObjectName("amanualspeedtext")
        self.gridLayout_7.addWidget(self.amanualspeedtext, 2, 0, 1, 1)
        self.currentspeed = QtWidgets.QLCDNumber(parent=self.gridLayoutWidget_7)
        self.currentspeed.setObjectName("currentspeed")
        self.gridLayout_7.addWidget(self.currentspeed, 1, 1, 1, 1)
        self.autocommandedspeed = QtWidgets.QLCDNumber(parent=self.gridLayoutWidget_7)
        self.autocommandedspeed.setObjectName("autocommandedspeed")
        self.gridLayout_7.addWidget(self.autocommandedspeed, 2, 1, 1, 1)
        self.leftdoor = QtWidgets.QCheckBox(parent=self.manual)
        self.leftdoor.setGeometry(QtCore.QRect(340, 290, 111, 21))
        self.leftdoor.setObjectName("leftdoor")
        self.manualcommandedspeed = QtWidgets.QSpinBox(parent=self.manual)
        self.manualcommandedspeed.setGeometry(QtCore.QRect(520, 200, 121, 41))
        self.manualcommandedspeed.setObjectName("manualcommandedspeed")
        self.textEdit_5 = QtWidgets.QTextEdit(parent=self.manual)
        self.textEdit_5.setGeometry(QtCore.QRect(640, 200, 61, 41))
        self.textEdit_5.setObjectName("textEdit_5")
        self.serviceBrake = QtWidgets.QPushButton(parent=self.manual)
        self.serviceBrake.setGeometry(QtCore.QRect(530, 10, 201, 101))
        self.serviceBrake.setObjectName("serviceBrake")
        self.tabWidget.addTab(self.manual, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.rightdoor.setText(_translate("Form", "Right Door Open"))
        self.internallight.setText(_translate("Form", "Internal Lights On"))
        self.externallight.setText(_translate("Form", "External Lights On"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Light Statuses</span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Door Statuses</span></p></body></html>"))
        self.ebrake.setToolTip(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.ebrake.setText(_translate("Form", "Emergency Brake"))
        self.textEdit_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Announcement:</span></p></body></html>"))
        self.manualtrainfailures.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Train Failures</span></p></body></html>"))
        self.textEdit_10.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Time:</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Speed Limit (miles/hr)</span></p></body></html>"))
        self.textEdit_15.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Authority (feet)</span></p></body></html>"))
        self.textEdit_8.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">Temperature (F)</span></p></body></html>"))
        self.nextstop.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.amanualnextstop.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Next stop:</span></p></body></html>"))
        self.brakefailure.setText(_translate("Form", "Brake Failure"))
        self.enginefailure.setText(_translate("Form", "Engine Failure"))
        self.signalfailure.setText(_translate("Form", "Signal Failure"))
        self.amanualki.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Integral Gain (Ki):</span></p></body></html>"))
        self.amanualkp.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Proportional Gain (Kp):</span></p></body></html>"))
        self.apowertext.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700; font-style:italic; text-decoration: underline;\">Power (W)</span></p></body></html>"))
        self.textEdit_17.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700; font-style:italic; text-decoration: underline;\">Mode:</span></p></body></html>"))
        self.mode.setItemText(0, _translate("Form", "Automatic"))
        self.mode.setItemText(1, _translate("Form", "Manual"))
        self.textEdit_9.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Manual Velocity</span></p></body></html>"))
        self.textEdit_11.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700; font-style:italic; text-decoration: underline;\">Current Speed (miles/hr)</span></p></body></html>"))
        self.amanualspeedtext.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700; font-style:italic; text-decoration: underline;\">Commanded Speed (miles/hr)</span></p></body></html>"))
        self.leftdoor.setText(_translate("Form", "Left Door Open"))
        self.textEdit_5.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">miles/hr</p></body></html>"))
        self.serviceBrake.setText(_translate("Form", "Service Brake"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.manual), _translate("Form", "Main Page"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())