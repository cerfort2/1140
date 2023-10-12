#import os
#import subprocess
import time
import pandas as pd

from datetime import datetime, timedelta

from threading import Thread, Event
from pathlib import Path
from typing import List, Optional

from PyQt6.QtCore import pyqtSignal, QEvent, Qt
from PyQt6.QtWidgets import QTreeWidgetItem, QWidget, QFileDialog, QMainWindow, QApplication, QTableWidgetItem


from CTC_ui import Ui_MainWindow


class CTC(QMainWindow):
    occupancy_update = pyqtSignal()
    station_update = pyqtSignal()
    manual_mode = pyqtSignal()
    auto_mode = pyqtSignal()
    maint_mode = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.num_trains_dispatched = 0
        self.trainID = 0
        #MainWindow = QMainWindow()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setMinimumSize(920, 608)  # Adjust these dimensions as per your needs
        
        self.occupancy_old_text = None
        self.old_station = None
        
        self.red_line = ['SHADYSIDE', 'HERRON AVE', 'SWISSVILLE', 'PENN STATION', 'FIRST AVE', 'STATION SQUARE', 'SOUTH HILLS JUNCTION']
        self.green_line_both = ['PIONEER', 'EDGEBROOK', 'WHITE', 'SOUTH BANK', 'CENTRAL', 'INGLEWOOD', 'OVERBROOK', 'GLENBURY', 'DORMONT', 'MT LEBANON', 'POPLAR', 'CASTLE SHANNON']
        self.blue_line = ['Station A', 'Station B', 'Station C']
        self.blue_line_times = [1,1,1]
        self.blue_lines_blocks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        self.blue_line_schedule = []

        self.station_a_throughput = 0
        self.station_b_throughput = 0
        self.station_c_throughput = 0

        self.initialize_connections()
        self.start_threads()
        self.initialize_ui()

    def start_threads(self):
        Thread(target=self.update_occupancy_ui).start()
        Thread(target=self.check_mode).start()
        Thread(target=self.check_stations).start()

    def initialize_connections(self):
        self.ui.dispatch_train_btn.clicked.connect(self.dispatch_train)
        #self.ui.manual_mode_btn.isChecked.connect(self.update_mode_tb)
        self.ui.import_schedule_btn.clicked.connect(self.import_schedule)
        self.ui.apply_changes.clicked.connect(self.apply_tb)
        self.station_update.connect(self.update_stations)
        self.ui.schedule_train_btn.clicked.connect(self.schedule_train)
        self.manual_mode.connect(self.update_manual_mode)
        self.auto_mode.connect(self.update_auto_mode)

    
    def initialize_ui(self):
        self.ui.block_occupancy.setVerticalHeaderLabels([str(i) for i in range(1, 16)])
        self.ui.manual_dispatch_departure.addItem("Station A")
        self.ui.manual_dispatch_departure.addItem("Station B")
        self.ui.manual_dispatch_departure.addItem("Station C")
        self.ui.manual_mode_btn.setChecked(True)

    def check_stations(self):
        while True:
            if (self.ui.manual_dispatch_departure != self.old_station):
                self.station_update.emit()
            time.sleep(0.5)
            

    def update_stations(self):
        if (self.ui.manual_dispatch_departure.currentText() == "Station A"):
            self.old_station = "Station A"
            self.ui.manual_dispatch_destination.clear()
            self.ui.manual_dispatch_destination.addItem("Station B")
            self.ui.manual_dispatch_destination.addItem("Station C")
        elif (self.ui.manual_dispatch_departure.currentText() == "Station B"):
            self.old_station = "Station B"
            self.ui.manual_dispatch_destination.clear()
            self.ui.manual_dispatch_destination.addItem("Station A")
            self.ui.manual_dispatch_destination.addItem("Station C")
        elif (self.ui.manual_dispatch_departure.currentText() == "Station C"):
            self.old_station = "Station C"
            self.ui.manual_dispatch_destination.clear()
            self.ui.manual_dispatch_destination.addItem("Station A")
            self.ui.manual_dispatch_destination.addItem("Station B")


    def check_occupancy(self):
        if(self.ui.occupancy_line_box.currentText() != self.occupancy_old_text):
            self.occupancy_update.emit()

    def update_occupancy_ui(self):
        if (self.ui.occupancy_line_box.currentText() == "Red Line"):
            self.occupancy_old_text = "Red Line"
            self.ui.block_occupancy.setVerticalHeaderLabels([str(i) for i in range(1, 61)])
        elif(self.ui.occupancy_line_box.currentText() == "Green Line"):
            self.occupancy_old_text = "Green Line"
            self.ui.block_occupancy.setVerticalHeaderLabels([str(i) for i in range(1, 142)])
        elif(self.ui.occupancy_line_box.currentText() == "Blue Line"):
            self.occupancy_old_text = "Blue Line"
            self.ui.block_occupancy.setVerticalHeaderLabels([str(i) for i in range(1, 16)])

    def check_mode(self):
        while True:
            if(self.ui.manual_mode_btn.isChecked()):
                self.manual_mode.emit()
            if(self.ui.auto_mode_btn.isChecked()):
                self.auto_mode.emit()
            if(self.ui.maint_mode_btn.isChecked()):
                self.maint_mode.emit()
            time.sleep(0.5)

    def update_manual_mode(self):
        self.ui.import_schedule_btn.hide()
        self.ui.dispatch_train_btn.setEnabled(True)
        self.ui.manual_widget.show()
        # for i in range(self.ui.manual_layout.count()):
        #     widget = self.ui.manual_layout.itemAt(i).widget()
        #     if widget is not None:
        #         widget.show()
        self.ui.schedule_train_btn.show()
        self.ui.departure_time.show()
        self.ui.departure_time_label.show()

    
    def update_auto_mode(self):
        self.ui.import_schedule_btn.show()
        self.ui.dispatch_train_btn.setEnabled(False)
        self.ui.manual_widget.hide()
        # for i in range(self.ui.manual_layout.count()):
        #     widget = self.ui.manual_layout.itemAt(i).widget()
        #     if widget is not None:
        #         widget.hide()
        self.ui.schedule_train_btn.hide()
        self.ui.departure_time.hide()
        self.ui.departure_time_label.hide()

    def import_schedule(self):
        options = QFileDialog.Option.ReadOnly
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)", options=options)

        if filePath:
            self.ui.label.setText(f'Selected File: {filePath}')
            if filePath.endswith('.xlsx'):
                df = pd.read_excel(filePath)
            elif filePath.endswith('.csv'):
                df = pd.read_csv(filePath)
            else:
                self.textEdit.setText("Unsupported file format!")
                return

            train_ids = df['Train ID'].tolist()
            departing_stations = df['Departing From'].tolist()
            arriving_stations = df['Arriving to'].tolist()
            departure_times = df['Departure Time'].tolist()
            self.update_schedule(train_ids, departing_stations, arriving_stations, departure_times)

            #lines = df['Line'].tolist()
            #infrastructures = df['Infrastructure'].tolist()
            #times = df['Time to Station'].tolist()
        return



    def dispatch_train(self):
        #self.num_trains_dispatched += 1
        #self.train = self.ui.train_sel.getCurrentValue()
        #speed = self.ui.mph_box.getCurrentValue()
        #route = self.ui.route_box.getCurrentValue()
        #authority = self.ui.authority_box.getCurrentValue()
        self.update_schedule()
        item = QTableWidgetItem()
        item.setBackground(Qt.GlobalColor.green)
        self.ui.block_occupancy.setItem(0, 0, item)
        return #[speed, route, authority]
    
    #updates schedule on main page
    def update_schedule(self, train_ids="0", departure_="0", destination_="0", departure_time_="0"):
        if(self.ui.manual_mode_btn.isChecked()):
            train = self.trainID
            self.trainID+=1
            departure = self.ui.manual_dispatch_departure.currentText()
            destination = self.ui.manual_dispatch_destination.currentText()
            delta = self.calculate_time(departure, destination)
            dep_time = datetime.strptime(datetime.now().strftime("%H:%M:%S"), "%H:%M:%S")
            dep_time_str = dep_time.strftime("%H:%M:%S")
            eta = (dep_time + delta).strftime("%H:%M:%S")
            self.blue_line_schedule.append(QTreeWidgetItem([str(train), departure, destination, str(dep_time_str), str(eta)]))
            self.ui.schedule.addTopLevelItem(QTreeWidgetItem([str(train), departure, destination, str(dep_time_str), str(eta)]))
        elif self.ui.auto_mode_btn.isChecked():
            # Assuming train_ids, departure_, destination_, and departure_time_ are lists
            for t_id, dep, dest, dep_time in zip(train_ids, departure_, destination_, departure_time_):
                if isinstance(dep_time, datetime.time):
                    hrs, mins, secs = dep_time.hour, dep_time.minute, dep_time.second
                else:
                    hrs, mins, secs = map(int, dep_time.split(':'))

                delta_dep_time = timedelta(hours=hrs, minutes=mins, seconds=secs)

                delta = self.calculate_time(dep, dest)
                eta = (datetime.datetime.combine(datetime.date.today(), delta_dep_time) + delta).time().strftime("%H:%M:%S")
                self.blue_line_schedule.append(QTreeWidgetItem([str(t_id), dep, dest, dep_time, eta]))
                self.ui.schedule.addTopLevelItem(QTreeWidgetItem([str(t_id), dep, dest, dep_time, eta]))
    
        return
    
    def apply_tb(self):
        block_combos = [self.ui.track_tb, self.ui.maintenance_tb, self.ui.block_occupancy_tb]
        state_combos = [self.ui.track_state_tb, self.ui.maintenance_state_tb, self.ui.block_state_tb]

        # Loop over each block
        for block_combo, state_combo in zip(block_combos, state_combos):
            block_num = block_combo.currentText()
            block_state = state_combo.currentText()

            # Check if block_state is empty and skip if it is
            if not block_state:
                continue

            # Define color-coding logic
            if block_state == "Occupied":
                color = Qt.GlobalColor.green
            elif block_state == "Maintenance":
                color = Qt.GlobalColor.yellow
            elif block_state == "Failure":
                color = Qt.GlobalColor.red

            # Update the QTableWidget
            block_row = int(block_num) - 1  # assuming block numbers start from 1 and are sequential
            item = self.ui.block_occupancy.item(block_row, 0)  # assuming the "occupied" column is the first one

            if not item:  # If item doesn't exist, create one
                item = QTableWidgetItem()
                self.ui.block_occupancy.setItem(block_row, 0, item)

            item.setBackground(color)

            # Update the last column of the row to "Closed" for "Maintenance" or "Failure" state
            if block_state in ["Maintenance", "Failure"]:
                last_column = self.ui.block_occupancy.columnCount() - 1
                close_item = self.ui.block_occupancy.item(block_row, last_column)
                
                if not close_item:
                    close_item = QTableWidgetItem()
                    self.ui.block_occupancy.setItem(block_row, last_column, close_item)

                close_item.setText("Closed")

        throughput = self.calc_throughput()
        self.ui.throughput_val.display(throughput)

        self.update_ui_tb()
        return

    
    def update_ui_tb(self):
        return

    def calculate_time(self, station_a, station_b):
        #for blue line
        hrs = 0
        mins = 0
        secs = 0
        if(station_a == "Station A"):
            if(station_b == "Station B"):
                mins+=1
            if(station_a == "Station C"):
                mins+=1
        if(station_a == "Station B"):
            if(station_b == "Station A"):
                mins+=1
            if(station_a == "Station C"):
                mins+=1
        if(station_a == "Station C"):
            if(station_b == "Station A"):
                mins+=1
            if(station_a == "Station B"):
                mins+=1
        delta = timedelta(hours = hrs, minutes = mins, seconds = secs)
        return delta


    def calc_throughput(self):
        if self.ui.throughput_station_tb.currentText() == "Station A":
            self.station_a_throughput = self.ui.throughput_tb.value()
        elif self.ui.throughput_station_tb.currentText() == "Station B":
            self.station_b_throughput = self.ui.throughput_tb.value()
        elif self.ui.throughput_station_tb.currentText() == "Station C":
            self.station_c_throughput = self.ui.throughput_tb.value()

        total_throughput = self.station_a_throughput + self.station_b_throughput + self.station_c_throughput
        return total_throughput
        
    def close_track(self, track_num):
        return
    
    def schedule_train(self):
        train = self.trainID
        self.trainID+=1
        departure = self.ui.manual_dispatch_departure.currentText()
        destination = self.ui.manual_dispatch_destination.currentText()
        delta = self.calculate_time(departure, destination)
        dep_time = datetime.strptime(datetime.now().strftime("%H:%M:%S"), "%H:%M:%S")
        dep_time_str = dep_time.strftime("%H:%M:%S")
        eta = (dep_time + delta).strftime("%H:%M:%S")
        self.blue_line_schedule.append(QTreeWidgetItem([str(train), departure, destination, str(dep_time_str), str(eta)]))
        self.ui.schedule.addTopLevelItem(QTreeWidgetItem([str(train), departure, destination, str(dep_time_str), str(eta)]))
        return
    
    #updates the ui of tb when manual mode is selected/deselected
    def update_mode_tb(self):
        return
    
    
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ctc_widget = CTC()
    MainWindow.setCentralWidget(ctc_widget)
    MainWindow.show()
    sys.exit(app.exec())