# Form implementation generated from reading ui file './ui_files/Home.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(392, 441)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(69, 89, 281, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ctc = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.ctc.setObjectName("ctc")
        self.verticalLayout.addWidget(self.ctc)
        self.track_model = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.track_model.setObjectName("track_model")
        self.verticalLayout.addWidget(self.track_model)
        self.track_controller = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.track_controller.setObjectName("track_controller")
        self.verticalLayout.addWidget(self.track_controller)
        self.train_model = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.train_model.setObjectName("train_model")
        self.verticalLayout.addWidget(self.train_model)
        self.train_controller = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.train_controller.setObjectName("train_controller")
        self.verticalLayout.addWidget(self.train_controller)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(170, 70, 81, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ctc.setText(_translate("Form", "CTC"))
        self.track_model.setText(_translate("Form", "Track Model"))
        self.track_controller.setText(_translate("Form", "Track Controller (Software)"))
        self.train_model.setText(_translate("Form", "Train Model"))
        self.train_controller.setText(_translate("Form", "Train Controller (Software)"))
        self.label.setText(_translate("Form", "Select Module"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
