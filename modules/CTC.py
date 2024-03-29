#import os
#import subprocess
import sys
import time
import pandas as pd
import random
import string

from datetime import datetime, timedelta, date

from threading import Thread, Event
from pathlib import Path
from typing import List, Optional

from PyQt6.QtCore import pyqtSignal, QEvent, Qt, QDateTime, QTimer, QObject
from PyQt6.QtWidgets import QTreeWidgetItem, QWidget, QFileDialog, QMainWindow, QApplication, QButtonGroup, QTableWidgetItem, QRadioButton, QLabel, QLineEdit, QHeaderView

from modules.Line import Line
from modules.CTC_ui import Ui_Form


class Train:
    def __init__(self, trainID, destination, departure_time, arrival_time, stops, line):
        self.trainID = trainID
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.stops = stops
        self.line = line

class CTC(Ui_Form, QWidget):
    station_update = pyqtSignal()
    manual_mode = pyqtSignal()
    auto_mode = pyqtSignal()
    maint_mode = pyqtSignal()
    train_dispatched = pyqtSignal(list, list, list)
    schedule_dispatch = pyqtSignal()
    stop_update = pyqtSignal()
    track_opened = pyqtSignal(str)
    track_closed = pyqtSignal(str)
    toggle_switch = pyqtSignal(str, bool)


    def __init__(self):
        super().__init__()
        
    def initialize_ctc(self):
        self.num_trains_dispatched = 0
        self.trainIDs = []
        
        #self.setMinimumSize(920, 608)
        self.system_start_time = QDateTime.fromString("07:00:00", "HH:mm:ss").time()
        self.cur_sys_time = QDateTime.fromString("07:00:00", "HH:mm:ss").time()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        
        self.occupancy_old_text = None
        self.old_line = None
        self.old_maintenance_line = None
        self.green_line_stations = ["K65: GLENBURY", "L73: DORMONT", "N77: MT LEBANON", "O88: POPLAR", "P96: CASTLE SHANNON", "T105: DORMONT", "U114: GLENBURY", "W123: OVERBROOK", "W132: INGLEWOOD", "W141: CENTRAL", "A2: PIONEER", "C9: EDGEBROOK", "D16: MONKEYWAY", "F22: WHITED", "G31: SOUTH BANK", "I39: CENTRAL", "I48: INGLEWOOD", "I57: OVERBROOK"]
        self.red_line_stations = ["C7: SHADYSIDE", "F16: HERRON AVE", "G21: SWISSVILLE", "H25: PENN STATION", "H35: STEEL PLAZA","H45: FIRST AVE","I48: STATION SQUARE","L60: SOUTH HILLS JUNCTION"]
        
        
        self.green_line = Line("Green", 'modules/Green Line Info_.xlsx', self.green_line_stations)
        self.red_line = Line("Red", 'modules/Red Line Info.xlsx', self.red_line_stations)
        self.stops = []

        
        self.green_line_blocks = ['A1', 'A2', 'A3', 'B4', 'B5', 'B6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'D13', 'D14', 'D15', 'D16', 'E17', 'E18', 'E19', 'E20', 'F21', 'F22', 'F23', 'F24', 'F25', 'F26', 'F27', 'F28', 'G29', 'G30', 'G31', 'G32', 'H33', 'H34', 'H35', 'I36', 'I37', 'I38', 'I39', 'I40', 'I41', 'I42', 'I43', 'I44', 'I45', 'I46', 'I47', 'I48', 'I49', 'I50', 'I51', 'I52', 'I53', 'I54', 'I55', 'I56', 'I57', 'J58', 'J59', 'J60', 'J61', 'J62', 'K63', 'K64', 'K65', 'K66', 'K67', 'K68', 'L69', 'L70', 'L71', 'L72', 'L73', 'M74', 'M75', 'M76', 'N77', 'N78', 'N79', 'N80', 'N81', 'N82', 'N83', 'N84', 'N85', 'O86', 'O87', 'O88', 'P89', 'P90', 'P91', 'P92', 'P93', 'P94', 'P95', 'P96', 'P97', 'Q98', 'Q99', 'Q100', 'R101', 'S102', 'S103', 'S104', 'T105', 'T106', 'T107', 'T108', 'T109', 'U110', 'U111', 'U112', 'U113', 'U114', 'U115', 'U116', 'V117', 'V118', 'V119', 'V120', 'V121', 'W122', 'W123', 'W124', 'W125', 'W126', 'W127', 'W128', 'W129', 'W130', 'W131', 'W132', 'W133', 'W134', 'W135', 'W136', 'W137', 'W138', 'W139', 'W140', 'W141', 'W142', 'W143', 'X144', 'X145', 'X146', 'Y147', 'Y148', 'Y149', 'Z150', 'Z151']
        self.red_line_blocks = ['A1', 'A2', 'A3', 'B4', 'B5', 'B6', 'C7', 'C8', 'C9', 'D10', 'D11', 'D12', 'E13', 'E14', 'E15', 'F16', 'F17', 'F18', 'F19', 'F20', 'G21', 'G22', 'G23', 'H24', 'H25', 'H26', 'H27', 'H28', 'H29', 'H30', 'H31', 'H32', 'H33', 'H34', 'H35', 'H36', 'H37', 'H38', 'H39', 'H40', 'H41', 'H42', 'H43', 'H44', 'H45', 'I46', 'I47', 'I48', 'J49', 'J50', 'J51', 'J52', 'J53', 'J54', 'K55', 'K56', 'K57', 'L58', 'L59', 'L60', 'M61', 'M62', 'M63', 'N64', 'N65', 'KN6', 'O67', 'P68', 'P69', 'P70', 'Q71', 'R72', 'S73', 'S74', 'S75', 'T76', 'T77']
        
        self.switch_states = []

        self.ticket_sales_log_green = []
        self.ticket_sales_log_red = []
        self.green_block_occupancies = []
        self.red_block_occupanices = []
        self.last_ts_updated = None
        self.throughput = 0
        
        self.train_schedule_green = []
        self.train_schedule_red = []
        self.trains_dispatched_green = []
        self.trains_dispatched_red = []
        self.speed_factor = 1

        self.initialize_connections()
        self.start_threads()
        self.initialize_ui()


#outputs
    def train_dispatch(self, route, authority, speed):
        self.train_dispatched.emit(route, authority, speed)
    
    def open_track(self, track):
        #output signal to track controller for closed track
        #update on block occupancy ui
        line = self.maintenance_line_sel.currentText()
        number = int(track[1:]) - 1
        color=Qt.GlobalColor.white
        status = "Open"
        if line == "Green Line":
            occupancy_item = self.block_occupancy_green.item(number, 0)
            status_item = self.block_occupancy_green.item(number, 2)
            
        if line == "Red Line":
            occupancy_item = self.block_occupancy_red.item(number, 0)
            status_item = self.block_occupancy_red.item(number, 2)
        
        if not occupancy_item:  # If the item doesn't exist, create it
            occupancy_item = QTableWidgetItem()
            if line == "Green Line":
                self.block_occupancy_green.setItem(number, 0, occupancy_item)
                self.block_occupancy_green.setItem(number, 2, status_item)
                status_item = self.block_occupancy_green.item(number, 2)
                self.block_occupancy_green.setItem(number, 2, status_item)
            if line == "Red Line":
                self.block_occupancy_red.setItem(number, 0, occupancy_item)
                self.block_occupancy_red.setItem(number, 2, status_item)
                status_item = self.block_occupancy_red.item(number, 2)
                self.block_occupancy_red.setItem(number, 2, status_item)
            # Set the background color for the block
        occupancy_item.setBackground(color)
        status_item.setText(status)
        self.track_opened.emit(track)

    def close_track(self, track):
        #self.track_closed.emit(track)
        number = int(track[1:]) - 1
        line = self.maintenance_line_sel.currentText()
        color=Qt.GlobalColor.yellow
        status = "Closed"
        
        if line == "Green Line":
            occupancy_item = self.block_occupancy_green.item(number, 0)
            if not occupancy_item:  # If the item doesn't exist, create it
                occupancy_item = QTableWidgetItem()
            self.block_occupancy_green.setItem(number, 0, occupancy_item)
            status_item = self.block_occupancy_green.item(number, 2)
            self.block_occupancy_green.setItem(number, 2, status_item)
        if line == "Red Line":
            occupancy_item = self.block_occupancy_red.item(number, 0)
            if not occupancy_item:  # If the item doesn't exist, create it
                occupancy_item = QTableWidgetItem()
            self.block_occupancy_red.setItem(number, 0, occupancy_item)
            status_item = self.block_occupancy_red.item(number, 2)
            self.block_occupancy_red.setItem(number, 2, status_item)

        
        status_item.setText(status)
        occupancy_item.setBackground(color)
        self.track_closed.emit(track)

    def send_switch(self, block, b):
        self.toggle_switch.emit(block, b)

#inputs
    def get_block_occupancies(self, occupancies):
        if len(occupancies) == 151:
            self.green_block_occupancies = occupancies
        if len(occupancies) == 77:
            self.red_block_occupanices = occupancies
        self.update_block_occupancy(occupancies)
    
    def get_failures(self, failures):
        self.update_failures(failures)
        
    def update_failures(self, failures):
        # Assuming 'occupancies' is a list of bools where True represents occupied and False represents open
        if len(failures) == 151:
            #green line
            for index, fail in enumerate(failures):
                # Determine the color based on occupancy
                
                color = Qt.GlobalColor.red if fail else Qt.GlobalColor.white
                status = "Failure" if fail else "Open"
                # Assuming the "Occupancy" column is the first column (0-indexed)
                occupancy_item = self.block_occupancy_green.item(index, 0)
                if not occupancy_item:  # If the item doesn't exist, create it
                    occupancy_item = QTableWidgetItem()
                    self.block_occupancy_green.setItem(index, 0, occupancy_item)
                status_item = self.block_occupancy_green.item(index, 2)  # Assuming the "Block Status" column is the third column
                if not status_item:
                    status_item = QTableWidgetItem()
                    self.block_occupancy_green.setItem(index, 2, status_item)
                
                # Set the background color for the block
                if color == Qt.GlobalColor.white and occupancy_item.background().color() == Qt.GlobalColor.yellow:
                    pass
                elif occupancy_item.background().color() == Qt.GlobalColor.green:
                    pass
                else:
                    occupancy_item.setBackground(color)
                    status_item.setText(status)
           
            
        elif len(failures) == 77:
            #red line
            for index, fail in enumerate(failures):
                # Determine the color based on occupancy
                color = Qt.GlobalColor.red if fail else Qt.GlobalColor.white
                status = "Failure" if fail else "Open"
                # Assuming the "Occupancy" column is the first column (0-indexed)
                occupancy_item = self.block_occupancy_red.item(index, 0)
                if not occupancy_item:  # If the item doesn't exist, create it
                    occupancy_item = QTableWidgetItem()
                    self.block_occupancy_red.setItem(index, 0, occupancy_item)
                status_item = self.block_occupancy_red.item(index, 2)  # Assuming the "Block Status" column is the third column
                if not status_item:
                    status_item = QTableWidgetItem()
                    self.block_occupancy_red.setItem(index, 2, status_item)

                # Set the background color for the block
                if color == Qt.GlobalColor.white and occupancy_item.background().color() == Qt.GlobalColor.yellow:
                    pass
                elif occupancy_item.background().color() == Qt.GlobalColor.green:
                    pass
                else:
                    occupancy_item.setBackground(color)
                    status_item.setText(status)     
    
    def updated_dispatched_trains_info(self, queue, occupancies):
        reversed_queue = list(reversed(queue))

        # Iterate over the occupancy list in reverse
        for i in reversed(range(len(occupancies))):
            if occupancies[i]:
                
                for train in reversed_queue:
                    train.cur_position = i
                    
                    reversed_queue.remove(train)
                    
            
    def update_ui_with_new_train_positions(self, queue):
        for train in queue:
            pass
    
    def get_ticket_sales(self, tickets):
        ticket_sales = tickets
        self.record_ticket_sales(ticket_sales)
    
    def get_speed(self, speed):
        self.speed_factor = int(round(1000/speed))
    
    def start_threads(self):
        #Thread(target=self.update_occupancy_ui).start()
        Thread(target=self.check_mode).start()
        Thread(target=self.check_stations).start()
        Thread(target=self.update_throughput).start()
        Thread(target=self.start_dispatch_check).start()
        Thread(target=self.check_maintenance_line).start()

    def initialize_connections(self):
        self.dispatch_train_btn.clicked.connect(self.dispatch_train)
        self.import_schedule_btn.clicked.connect(self.import_schedule)
        self.station_update.connect(self.update_stations)
        self.schedule_train_btn.clicked.connect(self.schedule_train)
        self.manual_mode.connect(self.update_manual_mode)
        self.auto_mode.connect(self.update_auto_mode)
        self.maint_mode.connect(self.update_maintenance_mode)
        self.add_stop.clicked.connect(self.add_stops)
        self.stop_update.connect(self.update_stops)
        self.schedule_dispatch.connect(self.dispatch_scheduled_train)
        self.open_track_btn.clicked.connect(lambda: self.open_track(self.maintenance_block_sel.currentText()))
        self.close_track_btn.clicked.connect(lambda: self.close_track(self.maintenance_block_sel.currentText()))
        self._12_13.toggled.connect(self.update_switch)
        self._1_13.toggled.connect(self.update_switch)
        self._29_30.toggled.connect(self.update_switch)
        self._29_150.toggled.connect(self.update_switch)
        self._57_yard.toggled.connect(self.update_switch)
        self._57_58.toggled.connect(self.update_switch)
        self._62_63.toggled.connect(self.update_switch)
        self._yard_63.toggled.connect(self.update_switch)
        self._76_77.toggled.connect(self.update_switch)
        self._77_101.toggled.connect(self.update_switch)
        self._85_86.toggled.connect(self.update_switch)
        self._85_100.toggled.connect(self.update_switch)
        self._9_10.toggled.connect(self.update_switch)
        self._9_yard.toggled.connect(self.update_switch)
        self._15_16.toggled.connect(self.update_switch)
        self._1_16.toggled.connect(self.update_switch)
        self._27_28.toggled.connect(self.update_switch)
        self._27_76.toggled.connect(self.update_switch)
        self._32_33.toggled.connect(self.update_switch)
        self._32_72.toggled.connect(self.update_switch)
        self._38_39.toggled.connect(self.update_switch)
        self._38_71.toggled.connect(self.update_switch)
        self._43_44.toggled.connect(self.update_switch)
        self._43_67.toggled.connect(self.update_switch)
        self._52_53.toggled.connect(self.update_switch)
        self._52_66.toggled.connect(self.update_switch)

    
    def initialize_ui(self):
        self.manual_mode_btn.setChecked(True)
        self.import_schedule_btn.hide()
        self.maintenance_widget.hide()
        self.tabWidget.removeTab(1)
        green_station_info = ["",
            "PIONEER",
            "",
            "",
            "",
            "",
            "",
            "",
            "EDGEBROOK",
            "",
            "",
            "SWITCH",
            "",
            "",
            "",
            "MONKEYWAY",
            "",
            "",
            "",
            "",
            "",
            "WHITED",
            "",
            "",
            "",
            "",
            "",
            "",
            "SWITCH",
            "",
            "SOUTH BANK",
            "",
            "",
            "",
            "",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "CENTRAL; UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "INGLEWOOD; UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "OVERBROOK; UNDERGROUND",
            "SWITCH TO YARD",
            "",
            "",
            "",
            "SWITCH FROM YARD",
            "",
            "",
            "GLENBURY",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "DORMONT",
            "",
            "",
            "SWITCH",
            "MT LEBANON",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "SWITCH",
            "",
            "POPLAR",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "CASTLE SHANNON",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "DORMONT",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "GLENBURY",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "UNDERGROUND",
            "OVERBROOK; UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "INGLEWOOD; UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "CENTRAL; UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "TO YARD"]
        self.block_occupancy_green.setRowCount(151)
        for row,value in enumerate(green_station_info):
            item = QTableWidgetItem(value)
            self.block_occupancy_green.setItem(row, 1, item)

        self.block_occupancy_red.setRowCount(77)
        red_station_info = ["",
            "",
            "",
            "",
            "",
            "",
            "SHADYSIDE",
            "",
            "SWITCH TO/FROM YARD",
            "",
            "",
            "",
            "",
            "",
            "SWITCH",
            "HERRON AVE",
            "",
            "",
            "",
            "",
            "SWISSVILLE",
            "",
            "",
            "UNDERGROUND",
            "PENN STATION; UNDERGROUND",
            "UNDERGROUND",
            "SWITCH; UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "SWITCH; UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "STEEL PLAZA; UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "SWITCH; UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "SWITCH; UNDERGROUND",
            "UNDERGROUND",
            "FIRST AVE; UNDERGROUND",
            "UNDERGROUND",
            "",
            "STATION SQUARE",
            "",
            "",
            "",
            "SWITCH",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "SOUTH HILLS JUNCTION",
            "",
            "",
            "",
            "",
            "",
            "",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "UNDERGROUND",
            "TO YARD",
        ]
        for row,value in enumerate(red_station_info):
            item = QTableWidgetItem(value)
            self.block_occupancy_red.setItem(row, 1, item)


    def update_maintenance_line_blocks(self):
        self.maintenance_block_sel.clear()
        if self.maintenance_line_sel.currentText() == "Green Line":
            for row, value in enumerate(self.green_line_blocks):
                self.maintenance_block_sel.addItem(value)
        if self.maintenance_line_sel.currentText() == "Red Line":
            for row, value in enumerate(self.red_line_blocks):
                self.maintenance_block_sel.addItem(value)



    def update_time(self):
        #updating current system time based on speed factor
        self.cur_sys_time = self.cur_sys_time.addSecs(self.speed_factor)
        # Update the QLabel with the new timeW
        self.system_time.setText(self.cur_sys_time.toString("HH:mm:ss"))
        # Emit signals if other classes need to be notified of the time change
        # self.time_updated.emit(self.cur_sys_time)

    def update_throughput(self):
        while True:
            return
        
    def check_maintenance_line(self):
        while True:
            if self.maintenance_line_sel.currentText() != self.old_maintenance_line:
                self.old_maintenance_line = self.maintenance_line_sel.currentText()
                self.update_maintenance_line_blocks()
            time.sleep(0.5)



    def check_stations(self):
        while True:
            if (self.manual_dispatch_line.currentText() != self.old_line):
                self.old_line = self.manual_dispatch_line.currentText()
                self.station_update.emit()
                self.stop_update.emit()
            time.sleep(0.5)

    def update_stations(self):
        self.manual_dispatch_destination.clear()
        if self.manual_dispatch_line.currentText() == "Green Line":
            for station in self.green_line_stations:
                if station not in self.stops:
                    self.manual_dispatch_destination.addItem(station)
        if self.manual_dispatch_line.currentText() == "Red Line":
            for station in self.red_line_stations:
                if station not in self.stops:
                    self.manual_dispatch_destination.addItem(station)

    def update_stops(self):
        self.stop_box_list.clear()
        if self.manual_dispatch_line.currentText() == "Green Line":
            for station in self.green_line_stations:
                if station not in self.stops:
                    self.stop_box_list.addItem(station)
        if self.manual_dispatch_line.currentText() == "Red Line":
            for station in self.red_line_stations:
                if station not in self.stops:
                    self.stop_box_list.addItem(station)
        
    
    def update_switch(self):
        if self._12_13.isChecked():
            self.toggle_switch.emit("D13", 0)
        elif self._1_13.isChecked():
            self.toggle_switch.emit("D13", 1)
        if self._29_30.isChecked():
            self.toggle_switch.emit("G29", 0)
        elif self._29_150.isChecked():
            self.toggle_switch.emit("G29", 1)
        if self._57_yard.isChecked():
            self.toggle_switch.emit("J58", 0)
        elif self._57_58.isChecked():
            self.toggle_switch.emit("J58", 1)
        if self._62_63.isChecked():
            self.toggle_switch.emit("J62", 0)
        elif self._yard_63.isChecked():
            self.toggle_switch.emit("J62", 1)
        if self._76_77.isChecked():
            self.toggle_switch.emit("N77", 1)
        elif self._77_101.isChecked():
            self.toggle_switch.emit("N77", 0)
        if self._85_86.isChecked():
            self.toggle_switch.emit("N85", 0)
        elif self._85_100.isChecked():
            self.toggle_switch.emit("N85", 1)
        if self._9_10.isChecked():
            self.toggle_switch.emit("C10", 1)
        elif self._9_yard.isChecked():
            self.toggle_switch.emit("C10", 0)
        if self._15_16.isChecked():
            self.toggle_switch.emit("F16", 1)
        elif self._1_16.isChecked():
            self.toggle_switch.emit("F16", 0)
        if self._27_28.isChecked():
            self.toggle_switch.emit("H27", 0)
        elif self._27_76.isChecked():
            self.toggle_switch.emit("H27", 1)
        if self._32_33.isChecked():
            self.toggle_switch.emit("H33", 1)
        elif self._32_72.isChecked():
            self.toggle_switch.emit("H33", 0)
        if self._38_39.isChecked():
            self.toggle_switch.emit("H38", 0)
        elif self._38_71.isChecked():
            self.toggle_switch.emit("H38", 1)
        if self._43_44.isChecked():
            self.toggle_switch.emit("H44", 1)
        elif self._43_67.isChecked():
            self.toggle_switch.emit("H44", 0)
        if self._52_53.isChecked():
            self.toggle_switch.emit("J52", 0)
        elif self._52_66.isChecked():
            self.toggle_switch.emit("J52", 1)

    def check_mode(self):
        while True:
            if(self.manual_mode_btn.isChecked()):
                self.manual_mode.emit()
            if(self.auto_mode_btn.isChecked()):
                self.auto_mode.emit()
            if(self.maint_mode_btn.isChecked()):
                self.maint_mode.emit()
            time.sleep(0.5)

    def update_manual_mode(self):
        self.import_schedule_btn.hide()
        self.dispatch_train_btn.show()
        self.dispatch_train_btn.setEnabled(True)
        self.manual_widget.show()
        self.maintenance_widget.hide()
        self.schedule_train_btn.show()
        self.departure_time.show()
        self.departure_time_label.show()
        self.arrival_time.show()
        self.add_stop.show()
        self.label.show()

    
    def update_auto_mode(self):
        self.import_schedule_btn.show()
        self.dispatch_train_btn.setEnabled(False)
        self.manual_widget.hide()
        self.maintenance_widget.hide()
        self.add_stop.hide()
        self.schedule_train_btn.hide()
        self.departure_time.hide()
        self.departure_time_label.hide()
        self.arrival_time.hide()
        self.label.hide()

    def update_maintenance_mode(self):
        self.import_schedule_btn.hide()
        self.dispatch_train_btn.hide()
        self.dispatch_train_btn.setEnabled(False)
        self.manual_widget.hide()
        self.maintenance_widget.show()
        self.add_stop.hide()
        self._9_10.setEnabled(True)
        self._15_16.setEnabled(True)
        self._27_28.setEnabled(True)
        self._32_33.setEnabled(True)
        self._38_39.setEnabled(True)
        self._43_44.setEnabled(True)
        self._52_53.setEnabled(True)
        self._12_13.setEnabled(True)
        self._29_30.setEnabled(True)
        self._57_yard.setEnabled(True)
        self._62_63.setEnabled(True)
        self._76_77.setEnabled(True)
        self._85_86.setEnabled(True)


        self.schedule_train_btn.hide()
        self.departure_time.hide()
        self.departure_time_label.hide()
        self.arrival_time.hide()
        self.label.hide()

    def import_schedule(self):
        options = QFileDialog.Option.ReadOnly
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx);;CSV Files (*.csv);;All Files (*)", options=options)

        if filePath:
            # Determine file type and read the file
            if filePath.endswith('.xlsx'):
                df = pd.read_excel(filePath)
            elif filePath.endswith('.csv'):
                df = pd.read_csv(filePath)
            else:
                #self.textEdit.setText("Unsupported file format!")
                return
            
            # Assuming the Excel structure matches the provided format
            arrival_stations = df['Arriving to'].tolist()
            departure_times = df['Departure Time'].tolist()
            arrival_times = df['Arrival Time'].tolist()
            stopping_at = df['Stopping At'].tolist()

            train_ids = []
            destinations = []
            dep_times = []
            arr_times = []
            stops = []
            line = ""
            if 'green' in filePath:
                line = "Green Line"
            elif 'red' in filePath:
                line = "Red Line"
            for dest, d_time, a_time, stop in zip(arrival_stations, departure_times, arrival_times, stopping_at):
                train_id = ''.join(random.choices(string.ascii_letters, k=4)) + ''.join(random.choices(string.digits, k=4))
                # Add each value to its respective list
                train_ids.append(train_id)
                destinations.append(dest)
                dep_time_qtime = QDateTime.fromString(str(d_time), "HH:mm:ss").time()
                arr_time_qtime = QDateTime.fromString(str(a_time), "HH:mm:ss").time()
                dep_time_str = dep_time_qtime.toString("HH:mm:ss")
                arr_time_str = arr_time_qtime.toString("HH:mm:ss")
                dep_times.append(dep_time_str)
                arr_times.append(arr_time_str)
                stops.append([stop.strip() for stop in stop.split(',')])

            # Update the schedule with the new data
            self.update_schedule(train_ids, destinations, dep_times, arr_times, stops, line)


    def add_stops(self):
        stop = self.stop_box_list.currentText()
        line = self.manual_dispatch_line.currentText()
        self.stops.append(stop)
        self.sort_stops(line)
        self.update_stations()
        self.update_stops()
        index = self.stop_box_list.findText(stop)
        self.stop_box_list.removeItem(index)
        
    def sort_stops(self, line):
        # Create a dictionary to map station to its order for sorting
        if line == "Green Line":
            order = {station: index for index, station in enumerate(self.green_line_stations)}
        if line == "Red Line":
            order = {station: index for index, station in enumerate(self.red_line_stations)}    
        # Sort self.stops based on the order in self.green_line_stations
        self.stops.sort(key=lambda x: order[x])
        
    def dispatch_train(self, destination = None, stops = [], arrival_time = None, departure_time = None, dispatched_line = None):
        station_list = []
        if stops != []:
            self.stops = stops
        if not destination:
            destination = self.manual_dispatch_destination.currentText()
        for stop in self.stops:
            station_list.append(stop)
        station_list.append(destination)
        
        if not arrival_time:
            arrival_time = QDateTime.fromString(self.arrival_time_dis.text(), "HH:mm:ss").time()
        if not departure_time:
            departure_time = self.cur_sys_time
        #get line from ui
        if not dispatched_line:
            dispatched_line = self.manual_dispatch_line.currentText()
        num_stops = len(self.stops)

        trainID = ''.join(random.choices(string.ascii_letters, k=4)) + ''.join(random.choices(string.digits, k=4))
        train = Train(trainID, destination, departure_time, arrival_time, self.stops, dispatched_line)
        next_stop = station_list[0]
        
        if dispatched_line == "Green Line":
            route = self.green_line.get_route(station_list)
            speeds = self.green_line.get_velocities(route[3], departure_time, arrival_time, num_stops)
            authority = self.green_line.get_authority(station_list)
            self.trains_dispatched_green.append(train)
            self.dispatched_green.addTopLevelItem(QTreeWidgetItem([str(trainID), "YARD", str(authority[0]), next_stop]))
        if dispatched_line == "Red Line":
            route = self.red_line.get_route(station_list)
            speeds = self.red_line.get_velocities(route[3], departure_time, arrival_time, num_stops)
            authority = self.red_line.get_authority(station_list)
            self.trains_dispatched_red.append(train)
            self.dispatched_red.addTopLevelItem(QTreeWidgetItem([str(trainID), "YARD", str(authority[0]), next_stop]))
        self.stops = []
        self.update_stations()
        self.update_stops()
        self.train_dispatch(route, authority, speeds)
        #self.arrival_time_dis.clear()
        return route, authority, speeds

    #get departure time, arrival time, destination station, stops
    def schedule_train(self):
        destination = self.manual_dispatch_destination.currentText()
        line = self.manual_dispatch_line.currentText()
        station_list = []
        for stop in self.stops:
            station_list.append(stop)
        station_list.append(destination)
        arrival_time = QDateTime.fromString(self.arrival_time.text(), "HH:mm:ss").time()
        departure_time = QDateTime.fromString(self.departure_time.text(), "HH:mm:ss").time()

        #get line from ui
        dispatched_line = self.manual_dispatch_line.currentText()
        num_stops = len(self.stops)
        
        trainID = ''.join(random.choices(string.ascii_letters, k=4)) + ''.join(random.choices(string.digits, k=4))
        stop_string = ""
        for stop in self.stops:
            if stop == self.stops[-1]:
                stop_string += stop
            else:
                stop_string += stop + ","
        train = Train(trainID, destination, departure_time, arrival_time, self.stops, dispatched_line)
        if dispatched_line == "Green Line":
            self.schedule_green.addTopLevelItem(QTreeWidgetItem([str(trainID), destination, departure_time.toString(), arrival_time.toString(), stop_string]))
            self.train_schedule_green.append(train)
        if dispatched_line == "Red Line":
            self.schedule_red.addTopLevelItem(QTreeWidgetItem([str(trainID), destination, departure_time.toString(), arrival_time.toString(), stop_string]))
            self.train_schedule_red.append(train)
        
        #self.update_schedule(train)
        self.stops = []
        self.update_stations()
        self.update_stops()
        self.arrival_time.clear()
        self.departure_time.clear()

    def check_for_dispatched(self):
        for train in self.train_schedule_green:
            if train.departure_time<= self.cur_sys_time:
                self.dispatch_scheduled_train(train)
                self.train_schedule_green.remove(train)
        for train in self.train_schedule_red:
            if train.departure_time<= self.cur_sys_time:
                self.dispatch_scheduled_train(train)
                self.train_schedule_red.remove(train)
    
    def start_dispatch_check(self):
        while True:
            self.check_for_dispatched()
            time.sleep(1)

    def dispatch_scheduled_train(self, train):
        departure_time = train.departure_time
        arrival_time = train.arrival_time
        trainID = train.trainID
        destination = train.destination
        stops = train.stops
        line = train.line
        station_list = []
        for stop in stops:
            station_list.append(stop)
        station_list.append(destination)
        num_stops = len(stops)
        
        next_stop = station_list[0]

        if line =="Green Line":
            route = self.green_line.get_route(station_list)
            speeds = self.green_line.get_velocities(route[3], departure_time, arrival_time, num_stops)
            authority = self.green_line.get_authority(station_list)
            self.dispatched_green.addTopLevelItem(QTreeWidgetItem([str(trainID), "YARD", str(authority[0]), next_stop]))
    
        if line =="Red Line":
            route = self.red_line.get_route(station_list)
            speeds = self.red_line.get_velocities(route[3], departure_time, arrival_time, num_stops)
            authority = self.red_line.get_authority(station_list)
            self.dispatched_red.addTopLevelItem(QTreeWidgetItem([str(trainID), "YARD", str(authority[0]), next_stop]))
    
        
        
        self.remove_train_from_schedule(train)
        self.train_dispatch(route, authority, speeds)

    def remove_train_from_schedule(self, train):
        if train.line == "Green Line":
            root = self.schedule_green.invisibleRootItem()
        if train.line == "Red Line":
            root = self.schedule_red.invisibleRootItem()
        
        for i in range(root.childCount()):
            item = root.child(i)
            if item.text(0) == train.trainID:  # Assuming the train ID is in the first column
                root.removeChild(item)
                break
            
    #updates schedule on main page
    def update_schedule(self, train_ids="0", destination_="0", departure_time_="0", arrival_time_="0", stops_="0", line="Green Line"):
            # Assuming train_ids, departure_, destination_, and departure_time_ are lists
        for t_id, dest, dep_time, arr_time, stop in zip(train_ids, destination_, departure_time_, arrival_time_, stops_):
            # if isinstance(dep_time, str):
            #     dep_time_obj = datetime.strptime(dep_time, "%H:%M:%S").time()
            # else:
            #     dep_time_obj = dep_time
            
            #self.blue_line_schedule.append(QTreeWidgetItem([str(t_id), dest, str(dep_time_obj), str(eta)]))
            dep_time_qtime = QDateTime.fromString(str(dep_time), "HH:mm:ss").time()
            arr_time_qtime = QDateTime.fromString(str(arr_time), "HH:mm:ss").time()
            train = Train(t_id, dest, dep_time_qtime, arr_time_qtime, stop, line)
            stop_string = ""
            for sto in stop:
                if sto == stop[-1]:
                    stop_string += sto
                else:
                    stop_string += sto + ","
            if line =="Green Line":
                self.train_schedule_green.append(train)
                self.schedule_green.addTopLevelItem(QTreeWidgetItem([str(t_id), str(dest), str(dep_time), str(arr_time), stop_string]))
            if line =="Red Line":
                self.train_schedule_red.append(train)
                self.schedule_red.addTopLevelItem(QTreeWidgetItem([str(t_id), str(dest), str(dep_time), str(arr_time), stop_string]))
        return
    

#change to updated_block_occupancy function
#receive block occupancies from track controller, upon receiving, update corresponding blocks

    def update_block_occupancy(self, occupancies):
        # Assuming 'occupancies' is a list of bools where True represents occupied and False represents open
        if len(occupancies) == 151:
            #green line
            for index, is_occupied in enumerate(occupancies):
                # Determine the color based on occupancy
                color = Qt.GlobalColor.green if is_occupied else Qt.GlobalColor.white
                status = "Occupied" if is_occupied else "Open"
                # Assuming the "Occupancy" column is the first column (0-indexed)
                occupancy_item = self.block_occupancy_green.item(index, 0)
                if not occupancy_item:  # If the item doesn't exist, create it
                    occupancy_item = QTableWidgetItem()
                    self.block_occupancy_green.setItem(index, 0, occupancy_item)
                
                # Update the "Block Status" in the third column
                status_item = self.block_occupancy_green.item(index, 2)  # Assuming the "Block Status" column is the third column
                if not status_item:
                    status_item = QTableWidgetItem()
                    self.block_occupancy_green.setItem(index, 2, status_item)
                    

                if occupancy_item.background().color() == Qt.GlobalColor.yellow:
                    pass
                elif (occupancy_item.background().color() == Qt.GlobalColor.red):
                    pass
                else:
                    occupancy_item.setBackground(color)
                    status_item.setText(status)  
        elif len(occupancies) == 77:
            #red line
            for index, is_occupied in enumerate(occupancies):
                # Determine the color based on occupancy
                color = Qt.GlobalColor.green if is_occupied else Qt.GlobalColor.white
                status = "Occupied" if is_occupied else "Open"

                # Assuming the "Occupancy" column is the first column (0-indexed)
                occupancy_item = self.block_occupancy_red.item(index, 0)
                if not occupancy_item:  # If the item doesn't exist, create it
                    occupancy_item = QTableWidgetItem()
                    self.block_occupancy_red.setItem(index, 0, occupancy_item)

                # Update the "Block Status" in the third column
                status_item = self.block_occupancy_red.item(index, 2)  # Assuming the "Block Status" column is the third column
                if not status_item:
                    status_item = QTableWidgetItem()
                    self.block_occupancy_red.setItem(index, 2, status_item)

                if occupancy_item.background().color() == Qt.GlobalColor.yellow:
                    pass
                elif (occupancy_item.background().color() == Qt.GlobalColor.red):
                    pass
                else:
                    occupancy_item.setBackground(color)
                    status_item.setText(status)  


    def record_ticket_sales(self, new_ticket_sales_list):
        # Assume new_ticket_sales_list is a list of ticket sales
        line = new_ticket_sales_list[0]
        for new_ticket_sales in new_ticket_sales_list[1:]:
            # Record each new ticket sale with the current timestamp
            current_time = datetime.now()
            if line == "Green Line":
                self.ticket_sales_log_green.append((current_time, new_ticket_sales))
            if line == "Red Line":
                self.ticket_sales_log_red.append((current_time, new_ticket_sales))
        
        # Call the throughput calculation once after all sales are recorded
        self.calc_throughput(line)


    def calc_throughput(self, line):
        # Get the current time
        current_time = datetime.now()
        # Calculate the cutoff time for the last hour
        one_hour_ago = current_time - timedelta(hours=1)
        
        # Filter the sales that occurred within the last hour
        

        # Calculate the total throughput for the last hour
        

        # Optionally remove old entries outside of the 1-hour window
        
        if line == "Green Line":
            recent_sales = [sales for timestamp, sales in self.ticket_sales_log_green if timestamp > one_hour_ago]
            total_throughput = sum(recent_sales)
            self.ticket_sales_log_green = [(timestamp, sales) for timestamp, sales in self.ticket_sales_log_green if timestamp > one_hour_ago]
            self.throughput_green.display(total_throughput)
        if line == "Red Line":
            recent_sales = [sales for timestamp, sales in self.ticket_sales_log_red if timestamp > one_hour_ago]
            total_throughput = sum(recent_sales)
            self.ticket_sales_log_red = [(timestamp, sales) for timestamp, sales in self.ticket_sales_log_red if timestamp > one_hour_ago]
            self.throughput_red.display(total_throughput)
    
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CTC()
    widget = QWidget()
    window.setupUi(widget)
    window.initialize_ctc()
    widget.show()
    sys.exit(app.exec())