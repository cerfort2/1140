# Form implementation generated from reading ui file 'train_model_ui_file_widget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form_train_model(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1146, 594)
        self.tabWidget = QtWidgets.QTabWidget(parent=Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1141, 591))
        self.tabWidget.setObjectName("tabWidget")
        self.page_tab = QtWidgets.QWidget()
        self.page_tab.setObjectName("page_tab")
        self.time_label = QtWidgets.QLabel(parent=self.page_tab)
        self.time_label.setGeometry(QtCore.QRect(10, 10, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.time_label.setFont(font)
        self.time_label.setObjectName("time_label")
        self.curr_time = QtWidgets.QLabel(parent=self.page_tab)
        self.curr_time.setGeometry(QtCore.QRect(140, 10, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.curr_time.setFont(font)
        self.curr_time.setObjectName("curr_time")
        self.announcement_label = QtWidgets.QLabel(parent=self.page_tab)
        self.announcement_label.setGeometry(QtCore.QRect(370, 20, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.announcement_label.setFont(font)
        self.announcement_label.setObjectName("announcement_label")
        self.announcement = QtWidgets.QTextBrowser(parent=self.page_tab)
        self.announcement.setGeometry(QtCore.QRect(520, 10, 231, 81))
        self.announcement.setObjectName("announcement")
        self.authority = QtWidgets.QLabel(parent=self.page_tab)
        self.authority.setGeometry(QtCore.QRect(880, 170, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.authority.setFont(font)
        self.authority.setObjectName("authority")
        self.current_velocity_label = QtWidgets.QLabel(parent=self.page_tab)
        self.current_velocity_label.setGeometry(QtCore.QRect(770, 130, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.current_velocity_label.setFont(font)
        self.current_velocity_label.setObjectName("current_velocity_label")
        self.train_vars_title = QtWidgets.QLabel(parent=self.page_tab)
        self.train_vars_title.setGeometry(QtCore.QRect(770, 0, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setUnderline(True)
        self.train_vars_title.setFont(font)
        self.train_vars_title.setObjectName("train_vars_title")
        self.passenger_count = QtWidgets.QLabel(parent=self.page_tab)
        self.passenger_count.setGeometry(QtCore.QRect(950, 290, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.passenger_count.setFont(font)
        self.passenger_count.setObjectName("passenger_count")
        self.current_velocity = QtWidgets.QLabel(parent=self.page_tab)
        self.current_velocity.setGeometry(QtCore.QRect(940, 130, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.current_velocity.setFont(font)
        self.current_velocity.setObjectName("current_velocity")
        self.power = QtWidgets.QLabel(parent=self.page_tab)
        self.power.setGeometry(QtCore.QRect(850, 90, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.power.setFont(font)
        self.power.setObjectName("power")
        self.power_label = QtWidgets.QLabel(parent=self.page_tab)
        self.power_label.setGeometry(QtCore.QRect(770, 90, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.power_label.setFont(font)
        self.power_label.setObjectName("power_label")
        self.authority_label = QtWidgets.QLabel(parent=self.page_tab)
        self.authority_label.setGeometry(QtCore.QRect(770, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.authority_label.setFont(font)
        self.authority_label.setObjectName("authority_label")
        self.passenger_count_label = QtWidgets.QLabel(parent=self.page_tab)
        self.passenger_count_label.setGeometry(QtCore.QRect(770, 290, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.passenger_count_label.setFont(font)
        self.passenger_count_label.setObjectName("passenger_count_label")
        self.environment = QtWidgets.QLabel(parent=self.page_tab)
        self.environment.setGeometry(QtCore.QRect(590, 230, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.environment.setFont(font)
        self.environment.setObjectName("environment")
        self.curr_environment_label = QtWidgets.QLabel(parent=self.page_tab)
        self.curr_environment_label.setGeometry(QtCore.QRect(380, 230, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.curr_environment_label.setFont(font)
        self.curr_environment_label.setObjectName("curr_environment_label")
        self.slope_label = QtWidgets.QLabel(parent=self.page_tab)
        self.slope_label.setGeometry(QtCore.QRect(380, 150, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.slope_label.setFont(font)
        self.slope_label.setObjectName("slope_label")
        self.enviromental_vars_title = QtWidgets.QLabel(parent=self.page_tab)
        self.enviromental_vars_title.setGeometry(QtCore.QRect(370, 100, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setUnderline(True)
        self.ad = QtWidgets.QLabel(parent=self.page_tab)
        self.ad.setGeometry(QtCore.QRect(20, 20, 300, 500))
        self.ad.setObjectName("advertisment")
        self.ad1 = QtGui.QPixmap("chipotle_ad.jpg")
        self.ad2 = QtGui.QPixmap("valorant_ad.jpg")
        self.ad3 = QtGui.QPixmap("zoo_ad.jpg")
        self.ad.setPixmap(self.ad1)
        self.enviromental_vars_title.setFont(font)
        self.enviromental_vars_title.setObjectName("enviromental_vars_title")
        self.slope = QtWidgets.QLabel(parent=self.page_tab)
        self.slope.setGeometry(QtCore.QRect(450, 150, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.slope.setFont(font)
        self.slope.setObjectName("slope")
        self.elevation = QtWidgets.QLabel(parent=self.page_tab)
        self.elevation.setGeometry(QtCore.QRect(490, 190, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.elevation.setFont(font)
        self.elevation.setObjectName("elevation")
        self.elevation_label = QtWidgets.QLabel(parent=self.page_tab)
        self.elevation_label.setGeometry(QtCore.QRect(380, 190, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.elevation_label.setFont(font)
        self.elevation_label.setObjectName("elevation_label")
        self.acceleration = QtWidgets.QLabel(parent=self.page_tab)
        self.acceleration.setGeometry(QtCore.QRect(910, 250, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.acceleration.setFont(font)
        self.acceleration.setObjectName("acceleration")
        self.air_conditioning = QtWidgets.QLabel(parent=self.page_tab)
        self.air_conditioning.setGeometry(QtCore.QRect(940, 210, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.air_conditioning.setFont(font)
        self.air_conditioning.setObjectName("air_conditioning")
        self.air_conditioning_label = QtWidgets.QLabel(parent=self.page_tab)
        self.air_conditioning_label.setGeometry(QtCore.QRect(770, 210, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.air_conditioning_label.setFont(font)
        self.air_conditioning_label.setObjectName("air_conditioning_label")
        self.acceleration_label = QtWidgets.QLabel(parent=self.page_tab)
        self.acceleration_label.setGeometry(QtCore.QRect(770, 250, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.acceleration_label.setFont(font)
        self.acceleration_label.setObjectName("acceleration_label")
        self.closed_door_text = QtWidgets.QLabel(parent=self.page_tab)
        self.closed_door_text.setGeometry(QtCore.QRect(660, 300, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.closed_door_text.setFont(font)
        self.closed_door_text.setObjectName("closed_door_text")
        self.left_door_label = QtWidgets.QLabel(parent=self.page_tab)
        self.left_door_label.setGeometry(QtCore.QRect(560, 315, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.left_door_label.setFont(font)
        self.left_door_label.setObjectName("left_door_label")
        self.inside_lights = QtWidgets.QCheckBox(parent=self.page_tab)
        self.inside_lights.setEnabled(False)
        self.inside_lights.setGeometry(QtCore.QRect(510, 325, 16, 16))
        self.inside_lights.setText("")
        self.inside_lights.setObjectName("inside_lights")
        self.enviromental_vars_title_2 = QtWidgets.QLabel(parent=self.page_tab)
        self.enviromental_vars_title_2.setGeometry(QtCore.QRect(380, 275, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setUnderline(True)
        self.enviromental_vars_title_2.setFont(font)
        self.enviromental_vars_title_2.setObjectName("enviromental_vars_title_2")
        self.left_door = QtWidgets.QCheckBox(parent=self.page_tab)
        self.left_door.setEnabled(False)
        self.left_door.setGeometry(QtCore.QRect(680, 325, 16, 16))
        self.left_door.setText("")
        self.left_door.setObjectName("left_door")
        self.right_door_label = QtWidgets.QLabel(parent=self.page_tab)
        self.right_door_label.setGeometry(QtCore.QRect(560, 365, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.right_door_label.setFont(font)
        self.right_door_label.setObjectName("right_door_label")
        self.outside_light_label = QtWidgets.QLabel(parent=self.page_tab)
        self.outside_light_label.setGeometry(QtCore.QRect(380, 365, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.outside_light_label.setFont(font)
        self.outside_light_label.setObjectName("outside_light_label")
        self.inside_light_label = QtWidgets.QLabel(parent=self.page_tab)
        self.inside_light_label.setGeometry(QtCore.QRect(380, 315, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.inside_light_label.setFont(font)
        self.inside_light_label.setObjectName("inside_light_label")
        self.outside_lights = QtWidgets.QCheckBox(parent=self.page_tab)
        self.outside_lights.setEnabled(False)
        self.outside_lights.setGeometry(QtCore.QRect(530, 375, 16, 16))
        self.outside_lights.setText("")
        self.outside_lights.setObjectName("outside_lights")
        self.right_door = QtWidgets.QCheckBox(parent=self.page_tab)
        self.right_door.setEnabled(False)
        self.right_door.setGeometry(QtCore.QRect(680, 375, 16, 16))
        self.right_door.setText("")
        self.right_door.setObjectName("right_door")
        self.brake_failure_label = QtWidgets.QLabel(parent=self.page_tab)
        self.brake_failure_label.setGeometry(QtCore.QRect(770, 480, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.brake_failure_label.setFont(font)
        self.brake_failure_label.setObjectName("brake_failure_label")
        self.signal_pickup_failure_title = QtWidgets.QLabel(parent=self.page_tab)
        self.signal_pickup_failure_title.setGeometry(QtCore.QRect(770, 520, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.signal_pickup_failure_title.setFont(font)
        self.signal_pickup_failure_title.setObjectName("signal_pickup_failure_title")
        self.train_failures_title = QtWidgets.QLabel(parent=self.page_tab)
        self.train_failures_title.setGeometry(QtCore.QRect(770, 400, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setUnderline(True)
        self.train_failures_title.setFont(font)
        self.train_failures_title.setObjectName("train_failures_title")
        self.engine_failure_label = QtWidgets.QLabel(parent=self.page_tab)
        self.engine_failure_label.setGeometry(QtCore.QRect(770, 440, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.engine_failure_label.setFont(font)
        self.engine_failure_label.setObjectName("engine_failure_label")
        self.emergency_brake = QtWidgets.QPushButton(parent=self.page_tab)
        self.emergency_brake.setGeometry(QtCore.QRect(0, 440, 491, 121))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.emergency_brake.setFont(font)
        self.emergency_brake.setAutoFillBackground(False)
        self.emergency_brake.setObjectName("emergency_brake")
        self.emergency_brake.setStyleSheet('QPushButton {background-color: #FF0000; color: black;}')
        self.train_number = QtWidgets.QLabel(parent=self.page_tab)
        self.train_number.setGeometry(QtCore.QRect(10, 40, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.train_number.setFont(font)
        self.train_number.setObjectName("train_number")
        self.train_number_value = QtWidgets.QLabel(parent=self.page_tab)
        self.train_number_value.setGeometry(QtCore.QRect(150, 40, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.train_number_value.setFont(font)
        self.train_number_value.setObjectName("train_number_value")
        self.crew_count_label = QtWidgets.QLabel(parent=self.page_tab)
        self.crew_count_label.setGeometry(QtCore.QRect(770, 330, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.crew_count_label.setFont(font)
        self.crew_count_label.setObjectName("crew_count_label")
        self.crew_count = QtWidgets.QLabel(parent=self.page_tab)
        self.crew_count.setGeometry(QtCore.QRect(900, 330, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.crew_count.setFont(font)
        self.crew_count.setObjectName("crew_count")
        self.engine_failure = QtWidgets.QCheckBox(parent=self.page_tab)
        self.engine_failure.setGeometry(QtCore.QRect(920, 450, 16, 17))
        self.engine_failure.setText("")
        self.engine_failure.setObjectName("engine_failure")
        self.brake_failure = QtWidgets.QCheckBox(parent=self.page_tab)
        self.brake_failure.setGeometry(QtCore.QRect(910, 490, 16, 17))
        self.brake_failure.setText("")
        self.brake_failure.setObjectName("brake_failure")
        self.signal_failure = QtWidgets.QCheckBox(parent=self.page_tab)
        self.signal_failure.setGeometry(QtCore.QRect(980, 530, 16, 17))
        self.signal_failure.setText("")
        self.signal_failure.setObjectName("signal_failure")
        self.enviromental_vars_title_3 = QtWidgets.QLabel(parent=self.page_tab)
        self.enviromental_vars_title_3.setGeometry(QtCore.QRect(500, 410, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setUnderline(True)
        self.enviromental_vars_title_3.setFont(font)
        self.enviromental_vars_title_3.setObjectName("enviromental_vars_title_3")
        self.outside_light_label_2 = QtWidgets.QLabel(parent=self.page_tab)
        self.outside_light_label_2.setGeometry(QtCore.QRect(500, 450, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.outside_light_label_2.setFont(font)
        self.outside_light_label_2.setObjectName("outside_light_label_2")
        self.outside_light_label_3 = QtWidgets.QLabel(parent=self.page_tab)
        self.outside_light_label_3.setGeometry(QtCore.QRect(500, 490, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.outside_light_label_3.setFont(font)
        self.outside_light_label_3.setObjectName("outside_light_label_3")
        self.outside_light_label_4 = QtWidgets.QLabel(parent=self.page_tab)
        self.outside_light_label_4.setGeometry(QtCore.QRect(500, 530, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.outside_light_label_4.setFont(font)
        self.outside_light_label_4.setObjectName("outside_light_label_4")
        self.power_label_2 = QtWidgets.QLabel(parent=self.page_tab)
        self.power_label_2.setGeometry(QtCore.QRect(770, 50, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.power_label_2.setFont(font)
        self.power_label_2.setObjectName("power_label_2")
        self.mass = QtWidgets.QLabel(parent=self.page_tab)
        self.mass.setGeometry(QtCore.QRect(830, 50, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.mass.setFont(font)
        self.mass.setObjectName("mass")
        self.length = QtWidgets.QLabel(parent=self.page_tab)
        self.length.setGeometry(QtCore.QRect(580, 450, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.length.setFont(font)
        self.length.setObjectName("length")
        self.height = QtWidgets.QLabel(parent=self.page_tab)
        self.height.setGeometry(QtCore.QRect(580, 530, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.height.setFont(font)
        self.height.setObjectName("height")
        self.width = QtWidgets.QLabel(parent=self.page_tab)
        self.width.setGeometry(QtCore.QRect(580, 490, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.width.setFont(font)
        self.width.setObjectName("width")
        self.tabWidget.addTab(self.page_tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.time_label.setText(_translate("Form", "System Time: "))
        self.curr_time.setText(_translate("Form", "XX:XX:XX"))
        self.announcement_label.setText(_translate("Form", "Current \n"
"Announcement"))
        self.announcement.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">None</span></p></body></html>"))
        self.authority.setText(_translate("Form", "0 Feet"))
        self.current_velocity_label.setText(_translate("Form", "Current Velocity:"))
        self.train_vars_title.setText(_translate("Form", "Train Variables"))
        self.passenger_count.setText(_translate("Form", "0 People"))
        self.current_velocity.setText(_translate("Form", "0 MPH"))
        self.power.setText(_translate("Form", "0 Watts"))
        self.power_label.setText(_translate("Form", "Power:"))
        self.authority_label.setText(_translate("Form", "Authority:"))
        self.passenger_count_label.setText(_translate("Form", "Passenger Count: "))
        self.environment.setText(_translate("Form", "In Tunnel"))
        self.curr_environment_label.setText(_translate("Form", "Current Environment:"))
        self.slope_label.setText(_translate("Form", "Slope:"))
        self.enviromental_vars_title.setText(_translate("Form", "Environmental Variables"))
        self.slope.setText(_translate("Form", "0 Degrees"))
        self.elevation.setText(_translate("Form", "0 Feet"))
        self.elevation_label.setText(_translate("Form", "Elevation:"))
        self.acceleration.setText(_translate("Form", "0 Feet/S^2"))
        self.air_conditioning.setText(_translate("Form", "0 Degrees"))
        self.air_conditioning_label.setText(_translate("Form", "Air Conditioning:"))
        self.acceleration_label.setText(_translate("Form", "Acceleration:"))
        self.closed_door_text.setText(_translate("Form", "Closed?"))
        self.left_door_label.setText(_translate("Form", "Left Door:"))
        self.enviromental_vars_title_2.setText(_translate("Form", "Lights and Doors"))
        self.right_door_label.setText(_translate("Form", "Right Door:"))
        self.outside_light_label.setText(_translate("Form", "Outside Lights:"))
        self.inside_light_label.setText(_translate("Form", "Inside Lights:"))
        self.brake_failure_label.setText(_translate("Form", "Brake Failure:"))
        self.signal_pickup_failure_title.setText(_translate("Form", "Signal Pickup Failure:"))
        self.train_failures_title.setText(_translate("Form", "Train Failures"))
        self.engine_failure_label.setText(_translate("Form", "Engine Failure:"))
        self.emergency_brake.setText(_translate("Form", "EMERGENCY BRAKE"))
        self.train_number.setText(_translate("Form", "Train Number: "))
        self.train_number_value.setText(_translate("Form", "X"))
        self.crew_count_label.setText(_translate("Form", "Crew Count:"))
        self.crew_count.setText(_translate("Form", "0 People"))
        self.enviromental_vars_title_3.setText(_translate("Form", "Train Dimensions"))
        self.outside_light_label_2.setText(_translate("Form", "Length:"))
        self.outside_light_label_3.setText(_translate("Form", "Width:"))
        self.outside_light_label_4.setText(_translate("Form", "Height:"))
        self.power_label_2.setText(_translate("Form", "Mass:"))
        self.mass.setText(_translate("Form", "0 Pounds"))
        self.length.setText(_translate("Form", "0 Feet"))
        self.height.setText(_translate("Form", "0 Feet"))
        self.width.setText(_translate("Form", "0 Feet"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.page_tab), _translate("Form", "Main Page"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_train_model()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())