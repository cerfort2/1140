# Form implementation generated from reading ui file './ui_files/CTC.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 610)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 911, 591))
        self.tabWidget.setObjectName("tabWidget")
        self.ctc_mainpage = QtWidgets.QWidget()
        self.ctc_mainpage.setObjectName("ctc_mainpage")
        self.import_schedule_btn = QtWidgets.QPushButton(parent=self.ctc_mainpage)
        self.import_schedule_btn.setGeometry(QtCore.QRect(10, 100, 231, 91))
        self.import_schedule_btn.setObjectName("import_schedule_btn")
        self.schedule = QtWidgets.QTreeWidget(parent=self.ctc_mainpage)
        self.schedule.setGeometry(QtCore.QRect(10, 320, 461, 231))
        self.schedule.setObjectName("schedule")
        self.dispatch_train_btn = QtWidgets.QPushButton(parent=self.ctc_mainpage)
        self.dispatch_train_btn.setGeometry(QtCore.QRect(10, 10, 231, 71))
        self.dispatch_train_btn.setObjectName("dispatch_train_btn")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.ctc_mainpage)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(360, 200, 160, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.manual_mode_btn = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.manual_mode_btn.setObjectName("manual_mode_btn")
        self.verticalLayout.addWidget(self.manual_mode_btn)
        self.auto_mode_btn = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.auto_mode_btn.setObjectName("auto_mode_btn")
        self.verticalLayout.addWidget(self.auto_mode_btn)
        self.maint_mode_btn = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.maint_mode_btn.setObjectName("maint_mode_btn")
        self.verticalLayout.addWidget(self.maint_mode_btn)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.ctc_mainpage)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 289, 511, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lines_box = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget)
        self.lines_box.setObjectName("lines_box")
        self.lines_box.addItem("")
        self.horizontalLayout.addWidget(self.lines_box)
        self.occupancy_line_box = QtWidgets.QComboBox(parent=self.ctc_mainpage)
        self.occupancy_line_box.setGeometry(QtCore.QRect(470, 30, 71, 31))
        self.occupancy_line_box.setObjectName("occupancy_line_box")
        self.occupancy_line_box.addItem("")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(parent=self.ctc_mainpage)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(550, 0, 341, 361))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.block_occupancy = QtWidgets.QTableWidget(parent=self.verticalLayoutWidget_4)
        self.block_occupancy.setObjectName("block_occupancy")
        self.block_occupancy.setColumnCount(3)
        self.block_occupancy.setRowCount(15)
        item = QtWidgets.QTableWidgetItem()
        self.block_occupancy.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.block_occupancy.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.block_occupancy.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.block_occupancy.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.block_occupancy.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.block_occupancy.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.block_occupancy.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.block_occupancy.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.block_occupancy.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.block_occupancy.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.block_occupancy.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.block_occupancy.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.block_occupancy.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.block_occupancy.setItem(8, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.block_occupancy.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.block_occupancy.setItem(9, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.block_occupancy.setItem(10, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.block_occupancy.setItem(10, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.block_occupancy.setItem(11, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.block_occupancy.setItem(12, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.block_occupancy.setItem(13, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.block_occupancy.setItem(14, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.block_occupancy.setItem(14, 2, item)
        self.verticalLayout_4.addWidget(self.block_occupancy)
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(parent=self.ctc_mainpage)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(340, 110, 184, 80))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_30 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_10)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_10.addWidget(self.label_30)
        self.throughput_val = QtWidgets.QLCDNumber(parent=self.verticalLayoutWidget_10)
        self.throughput_val.setObjectName("throughput_val")
        self.verticalLayout_10.addWidget(self.throughput_val)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.ctc_mainpage)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(9, 250, 341, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.departure_time_label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.departure_time_label.setObjectName("departure_time_label")
        self.horizontalLayout_3.addWidget(self.departure_time_label)
        self.departure_time = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_2)
        self.departure_time.setObjectName("departure_time")
        self.horizontalLayout_3.addWidget(self.departure_time)
        self.schedule_train_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.schedule_train_btn.setObjectName("schedule_train_btn")
        self.horizontalLayout_3.addWidget(self.schedule_train_btn)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(parent=self.ctc_mainpage)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(290, 10, 160, 92))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_15 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_6.addWidget(self.label_15)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_16 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_5)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_16)
        self.label_17 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_5)
        self.label_17.setStyleSheet("background-color: rgb(12, 255, 61);")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_17)
        self.label_18 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_5)
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_18)
        self.label_20 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_5)
        self.label_20.setStyleSheet("background-color: rgb(255, 255, 65);")
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_20)
        self.label_19 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_5)
        self.label_19.setObjectName("label_19")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_19)
        self.label_21 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_5)
        self.label_21.setStyleSheet("background-color: rgb(255, 20, 36);")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_21)
        self.verticalLayout_6.addLayout(self.formLayout)
        self.manual_widget = QtWidgets.QWidget(parent=self.ctc_mainpage)
        self.manual_widget.setGeometry(QtCore.QRect(0, 90, 291, 151))
        self.manual_widget.setObjectName("manual_widget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(parent=self.manual_widget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, -10, 271, 151))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.manual_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.manual_layout.setContentsMargins(0, 0, 0, 0)
        self.manual_layout.setObjectName("manual_layout")
        self.manual_dispatch_line = QtWidgets.QComboBox(parent=self.gridLayoutWidget_2)
        self.manual_dispatch_line.setObjectName("manual_dispatch_line")
        self.manual_dispatch_line.addItem("")
        self.manual_layout.addWidget(self.manual_dispatch_line, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.manual_layout.addWidget(self.label_10, 2, 0, 1, 1)
        self.manual_dispatch_destination = QtWidgets.QComboBox(parent=self.gridLayoutWidget_2)
        self.manual_dispatch_destination.setObjectName("manual_dispatch_destination")
        self.manual_layout.addWidget(self.manual_dispatch_destination, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.manual_layout.addWidget(self.label_8, 0, 0, 1, 1)
        self.manual_dispatch_departure = QtWidgets.QComboBox(parent=self.gridLayoutWidget_2)
        self.manual_dispatch_departure.setObjectName("manual_dispatch_departure")
        self.manual_layout.addWidget(self.manual_dispatch_departure, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.manual_layout.addWidget(self.label_9, 1, 0, 1, 1)
        self.dispatched = QtWidgets.QTreeWidget(parent=self.ctc_mainpage)
        self.dispatched.setGeometry(QtCore.QRect(490, 400, 411, 161))
        self.dispatched.setObjectName("dispatched")
        self.label_14 = QtWidgets.QLabel(parent=self.ctc_mainpage)
        self.label_14.setGeometry(QtCore.QRect(490, 370, 252, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.tabWidget.addTab(self.ctc_mainpage, "")
        self.ctc_testbench = QtWidgets.QWidget()
        self.ctc_testbench.setObjectName("ctc_testbench")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.ctc_testbench)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 240, 251, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_11 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.line_throughput_tb = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_2)
        self.line_throughput_tb.setObjectName("line_throughput_tb")
        self.line_throughput_tb.addItem("")
        self.horizontalLayout_2.addWidget(self.line_throughput_tb)
        self.throughput_station_tb = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_2)
        self.throughput_station_tb.setObjectName("throughput_station_tb")
        self.throughput_station_tb.addItem("")
        self.throughput_station_tb.addItem("")
        self.throughput_station_tb.addItem("")
        self.horizontalLayout_2.addWidget(self.throughput_station_tb)
        self.throughput_tb = QtWidgets.QSpinBox(parent=self.verticalLayoutWidget_2)
        self.throughput_tb.setObjectName("throughput_tb")
        self.horizontalLayout_2.addWidget(self.throughput_tb)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.apply_changes = QtWidgets.QPushButton(parent=self.ctc_testbench)
        self.apply_changes.setGeometry(QtCore.QRect(720, 10, 181, 71))
        self.apply_changes.setObjectName("apply_changes")
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(parent=self.ctc_testbench)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(10, 10, 671, 211))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.comboBox = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_9)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.verticalLayout_9.addWidget(self.comboBox)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_9)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_9)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.maintenance_state_tb = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_9)
        self.maintenance_state_tb.setObjectName("maintenance_state_tb")
        self.maintenance_state_tb.addItem("")
        self.maintenance_state_tb.setItemText(0, "")
        self.maintenance_state_tb.addItem("")
        self.gridLayout.addWidget(self.maintenance_state_tb, 4, 2, 1, 1)
        self.track_tb = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_9)
        self.track_tb.setObjectName("track_tb")
        self.track_tb.addItem("")
        self.track_tb.addItem("")
        self.track_tb.addItem("")
        self.track_tb.addItem("")
        self.track_tb.addItem("")
        self.track_tb.addItem("")
        self.track_tb.addItem("")
        self.track_tb.addItem("")
        self.track_tb.addItem("")
        self.track_tb.addItem("")
        self.track_tb.addItem("")
        self.track_tb.addItem("")
        self.track_tb.addItem("")
        self.track_tb.addItem("")
        self.track_tb.addItem("")
        self.gridLayout.addWidget(self.track_tb, 3, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_9)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_9)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.comboBox_8 = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_9)
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.gridLayout.addWidget(self.comboBox_8, 1, 1, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_9)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.setItemText(0, "")
        self.comboBox_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_3, 2, 2, 1, 1)
        self.maintenance_tb = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_9)
        self.maintenance_tb.setObjectName("maintenance_tb")
        self.maintenance_tb.addItem("")
        self.maintenance_tb.addItem("")
        self.maintenance_tb.addItem("")
        self.maintenance_tb.addItem("")
        self.maintenance_tb.addItem("")
        self.maintenance_tb.addItem("")
        self.maintenance_tb.addItem("")
        self.maintenance_tb.addItem("")
        self.maintenance_tb.addItem("")
        self.maintenance_tb.addItem("")
        self.maintenance_tb.addItem("")
        self.maintenance_tb.addItem("")
        self.maintenance_tb.addItem("")
        self.maintenance_tb.addItem("")
        self.maintenance_tb.addItem("")
        self.gridLayout.addWidget(self.maintenance_tb, 4, 1, 1, 1)
        self.track_state_tb = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_9)
        self.track_state_tb.setObjectName("track_state_tb")
        self.track_state_tb.addItem("")
        self.track_state_tb.setItemText(0, "")
        self.track_state_tb.addItem("")
        self.gridLayout.addWidget(self.track_state_tb, 3, 2, 1, 1)
        self.comboBox_9 = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_9)
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.gridLayout.addWidget(self.comboBox_9, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_9)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.block_state_tb = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_9)
        self.block_state_tb.setObjectName("block_state_tb")
        self.block_state_tb.addItem("")
        self.block_state_tb.setItemText(0, "")
        self.block_state_tb.addItem("")
        self.gridLayout.addWidget(self.block_state_tb, 5, 2, 1, 1)
        self.label_77 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_9)
        self.label_77.setObjectName("label_77")
        self.gridLayout.addWidget(self.label_77, 1, 0, 1, 1)
        self.block_occupancy_tb = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_9)
        self.block_occupancy_tb.setObjectName("block_occupancy_tb")
        self.block_occupancy_tb.addItem("")
        self.block_occupancy_tb.addItem("")
        self.block_occupancy_tb.addItem("")
        self.block_occupancy_tb.addItem("")
        self.block_occupancy_tb.addItem("")
        self.block_occupancy_tb.addItem("")
        self.block_occupancy_tb.addItem("")
        self.block_occupancy_tb.addItem("")
        self.block_occupancy_tb.addItem("")
        self.block_occupancy_tb.addItem("")
        self.block_occupancy_tb.addItem("")
        self.block_occupancy_tb.addItem("")
        self.block_occupancy_tb.addItem("")
        self.block_occupancy_tb.addItem("")
        self.block_occupancy_tb.addItem("")
        self.gridLayout.addWidget(self.block_occupancy_tb, 5, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_9)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 0, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_9)
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 0, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_9)
        self.label_29.setObjectName("label_29")
        self.gridLayout.addWidget(self.label_29, 0, 2, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout)
        self.label_13 = QtWidgets.QLabel(parent=self.ctc_testbench)
        self.label_13.setGeometry(QtCore.QRect(550, 230, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.ctc_testbench)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(370, 270, 521, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox_11 = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_11, 1, 2, 1, 1)
        self.comboBox_10 = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_10, 1, 1, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_4, 0, 0, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_6, 0, 2, 1, 1)
        self.comboBox_7 = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_7, 1, 0, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_5, 0, 1, 1, 1)
        self.comboBox_12 = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_12.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_12, 2, 0, 1, 1)
        self.comboBox_13 = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        self.comboBox_13.setObjectName("comboBox_13")
        self.comboBox_13.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_13, 2, 1, 1, 1)
        self.comboBox_14 = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        self.comboBox_14.setObjectName("comboBox_14")
        self.comboBox_14.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_14, 2, 2, 1, 1)
        self.tabWidget.addTab(self.ctc_testbench, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.import_schedule_btn.setText(_translate("MainWindow", "Import Schedule"))
        self.schedule.headerItem().setText(0, _translate("MainWindow", "Train"))
        self.schedule.headerItem().setText(1, _translate("MainWindow", "Arriving At"))
        self.schedule.headerItem().setText(2, _translate("MainWindow", "Departure Time"))
        self.schedule.headerItem().setText(3, _translate("MainWindow", "ETA"))
        self.dispatch_train_btn.setText(_translate("MainWindow", "Dispatch Train"))
        self.manual_mode_btn.setText(_translate("MainWindow", "Manual Mode"))
        self.auto_mode_btn.setText(_translate("MainWindow", "Automatic Mode"))
        self.maint_mode_btn.setText(_translate("MainWindow", "Maintenance Mode"))
        self.label_4.setText(_translate("MainWindow", "Current Schedule"))
        self.lines_box.setItemText(0, _translate("MainWindow", "Blue Line"))
        self.occupancy_line_box.setItemText(0, _translate("MainWindow", "Blue Line"))
        self.label_7.setText(_translate("MainWindow", "OCCUPANCY"))
        item = self.block_occupancy.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Occupied"))
        item = self.block_occupancy.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Infrastructure"))
        item = self.block_occupancy.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Block Status"))
        __sortingEnabled = self.block_occupancy.isSortingEnabled()
        self.block_occupancy.setSortingEnabled(False)
        item = self.block_occupancy.item(0, 1)
        item.setText(_translate("MainWindow", "Station A"))
        item = self.block_occupancy.item(0, 2)
        item.setText(_translate("MainWindow", "Open"))
        item = self.block_occupancy.item(1, 2)
        item.setText(_translate("MainWindow", "Open"))
        item = self.block_occupancy.item(2, 2)
        item.setText(_translate("MainWindow", "Open"))
        item = self.block_occupancy.item(3, 2)
        item.setText(_translate("MainWindow", "Open"))
        item = self.block_occupancy.item(4, 2)
        item.setText(_translate("MainWindow", "Open"))
        item = self.block_occupancy.item(5, 2)
        item.setText(_translate("MainWindow", "Open"))
        item = self.block_occupancy.item(6, 1)
        item.setText(_translate("MainWindow", "SWITCH"))
        item = self.block_occupancy.item(6, 2)
        item.setText(_translate("MainWindow", "Open"))
        item = self.block_occupancy.item(7, 2)
        item.setText(_translate("MainWindow", "Open"))
        item = self.block_occupancy.item(8, 2)
        item.setText(_translate("MainWindow", "Open"))
        item = self.block_occupancy.item(9, 2)
        item.setText(_translate("MainWindow", "Open"))
        item = self.block_occupancy.item(10, 1)
        item.setText(_translate("MainWindow", "STATION B"))
        item = self.block_occupancy.item(10, 2)
        item.setText(_translate("MainWindow", "Open"))
        item = self.block_occupancy.item(11, 2)
        item.setText(_translate("MainWindow", "Open"))
        item = self.block_occupancy.item(12, 2)
        item.setText(_translate("MainWindow", "Open"))
        item = self.block_occupancy.item(13, 2)
        item.setText(_translate("MainWindow", "Open"))
        item = self.block_occupancy.item(14, 1)
        item.setText(_translate("MainWindow", "STATION C"))
        item = self.block_occupancy.item(14, 2)
        item.setText(_translate("MainWindow", "Open"))
        self.block_occupancy.setSortingEnabled(__sortingEnabled)
        self.label_30.setText(_translate("MainWindow", "Throughput (passengers per hour)"))
        self.departure_time_label.setText(_translate("MainWindow", "Departure Time (HH:MM:DD):"))
        self.schedule_train_btn.setText(_translate("MainWindow", "Schedule Train"))
        self.label_15.setText(_translate("MainWindow", "Ledger"))
        self.label_16.setText(_translate("MainWindow", "Occupied by train:"))
        self.label_18.setText(_translate("MainWindow", "Maintenance:"))
        self.label_19.setText(_translate("MainWindow", "Failure:"))
        self.manual_dispatch_line.setItemText(0, _translate("MainWindow", "Blue Line"))
        self.label_10.setText(_translate("MainWindow", "Select Destination Station"))
        self.label_8.setText(_translate("MainWindow", "Select Line"))
        self.label_9.setText(_translate("MainWindow", "Select Departure Station"))
        self.dispatched.headerItem().setText(0, _translate("MainWindow", "Train ID"))
        self.dispatched.headerItem().setText(1, _translate("MainWindow", "Current Block"))
        self.dispatched.headerItem().setText(2, _translate("MainWindow", "Authority"))
        self.dispatched.headerItem().setText(3, _translate("MainWindow", "Destination"))
        self.label_14.setText(_translate("MainWindow", "Blue Line Train Info"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ctc_mainpage), _translate("MainWindow", "Main Page"))
        self.label_11.setText(_translate("MainWindow", "TICKET SALES (hourly)"))
        self.line_throughput_tb.setItemText(0, _translate("MainWindow", "Blue Line"))
        self.throughput_station_tb.setItemText(0, _translate("MainWindow", "Station A"))
        self.throughput_station_tb.setItemText(1, _translate("MainWindow", "Station B"))
        self.throughput_station_tb.setItemText(2, _translate("MainWindow", "Station C"))
        self.apply_changes.setText(_translate("MainWindow", "Apply Changes"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Blue Line"))
        self.label_2.setText(_translate("MainWindow", "Set Crossing State"))
        self.label_3.setText(_translate("MainWindow", "Set Track Failure"))
        self.maintenance_state_tb.setItemText(1, _translate("MainWindow", "Active"))
        self.track_tb.setItemText(0, _translate("MainWindow", "1"))
        self.track_tb.setItemText(1, _translate("MainWindow", "2"))
        self.track_tb.setItemText(2, _translate("MainWindow", "3"))
        self.track_tb.setItemText(3, _translate("MainWindow", "4"))
        self.track_tb.setItemText(4, _translate("MainWindow", "5"))
        self.track_tb.setItemText(5, _translate("MainWindow", "6"))
        self.track_tb.setItemText(6, _translate("MainWindow", "7"))
        self.track_tb.setItemText(7, _translate("MainWindow", "8"))
        self.track_tb.setItemText(8, _translate("MainWindow", "9"))
        self.track_tb.setItemText(9, _translate("MainWindow", "10"))
        self.track_tb.setItemText(10, _translate("MainWindow", "11"))
        self.track_tb.setItemText(11, _translate("MainWindow", "12"))
        self.track_tb.setItemText(12, _translate("MainWindow", "13"))
        self.track_tb.setItemText(13, _translate("MainWindow", "14"))
        self.track_tb.setItemText(14, _translate("MainWindow", "15"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "7->8"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "7->12"))
        self.label_5.setText(_translate("MainWindow", "Set Maintenance"))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "7"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Closed"))
        self.maintenance_tb.setItemText(0, _translate("MainWindow", "1"))
        self.maintenance_tb.setItemText(1, _translate("MainWindow", "2"))
        self.maintenance_tb.setItemText(2, _translate("MainWindow", "3"))
        self.maintenance_tb.setItemText(3, _translate("MainWindow", "4"))
        self.maintenance_tb.setItemText(4, _translate("MainWindow", "5"))
        self.maintenance_tb.setItemText(5, _translate("MainWindow", "6"))
        self.maintenance_tb.setItemText(6, _translate("MainWindow", "7"))
        self.maintenance_tb.setItemText(7, _translate("MainWindow", "8"))
        self.maintenance_tb.setItemText(8, _translate("MainWindow", "9"))
        self.maintenance_tb.setItemText(9, _translate("MainWindow", "10"))
        self.maintenance_tb.setItemText(10, _translate("MainWindow", "11"))
        self.maintenance_tb.setItemText(11, _translate("MainWindow", "12"))
        self.maintenance_tb.setItemText(12, _translate("MainWindow", "13"))
        self.maintenance_tb.setItemText(13, _translate("MainWindow", "14"))
        self.maintenance_tb.setItemText(14, _translate("MainWindow", "15"))
        self.track_state_tb.setItemText(1, _translate("MainWindow", "Failure"))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "5"))
        self.label_6.setText(_translate("MainWindow", "Set Block Occupancy"))
        self.block_state_tb.setItemText(1, _translate("MainWindow", "Occupied"))
        self.label_77.setText(_translate("MainWindow", "Set Switch State"))
        self.block_occupancy_tb.setItemText(0, _translate("MainWindow", "1"))
        self.block_occupancy_tb.setItemText(1, _translate("MainWindow", "2"))
        self.block_occupancy_tb.setItemText(2, _translate("MainWindow", "3"))
        self.block_occupancy_tb.setItemText(3, _translate("MainWindow", "4"))
        self.block_occupancy_tb.setItemText(4, _translate("MainWindow", "5"))
        self.block_occupancy_tb.setItemText(5, _translate("MainWindow", "6"))
        self.block_occupancy_tb.setItemText(6, _translate("MainWindow", "7"))
        self.block_occupancy_tb.setItemText(7, _translate("MainWindow", "8"))
        self.block_occupancy_tb.setItemText(8, _translate("MainWindow", "9"))
        self.block_occupancy_tb.setItemText(9, _translate("MainWindow", "10"))
        self.block_occupancy_tb.setItemText(10, _translate("MainWindow", "11"))
        self.block_occupancy_tb.setItemText(11, _translate("MainWindow", "12"))
        self.block_occupancy_tb.setItemText(12, _translate("MainWindow", "13"))
        self.block_occupancy_tb.setItemText(13, _translate("MainWindow", "14"))
        self.block_occupancy_tb.setItemText(14, _translate("MainWindow", "15"))
        self.label_27.setText(_translate("MainWindow", "Signal"))
        self.label_28.setText(_translate("MainWindow", "Block"))
        self.label_29.setText(_translate("MainWindow", "State"))
        self.label_13.setText(_translate("MainWindow", "Change Train Data"))
        self.comboBox_11.setItemText(0, _translate("MainWindow", "Alternate Route"))
        self.comboBox_10.setItemText(0, _translate("MainWindow", "Train ID"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Select Line"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Delays"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "Select Line"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Train ID"))
        self.comboBox_12.setItemText(0, _translate("MainWindow", "Select Line"))
        self.comboBox_13.setItemText(0, _translate("MainWindow", "Train ID"))
        self.comboBox_14.setItemText(0, _translate("MainWindow", "Emergency Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ctc_testbench), _translate("MainWindow", "Test Bench"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())