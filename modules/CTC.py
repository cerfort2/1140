#import os
#import subprocess
import time
import pandas as pd
import random
import string

from datetime import datetime, timedelta, date

from threading import Thread, Event
from pathlib import Path
from typing import List, Optional

from PyQt6.QtCore import pyqtSignal, QEvent, Qt
from PyQt6.QtWidgets import QTreeWidgetItem, QWidget, QFileDialog, QMainWindow, QApplication, QTableWidgetItem, QLabel, QLineEdit

from Line import Line
from CTC_ui import Ui_MainWindow


class CTC(QWidget):
    occupancy_update = pyqtSignal()
    station_update = pyqtSignal()
    manual_mode = pyqtSignal()
    auto_mode = pyqtSignal()
    maint_mode = pyqtSignal()
    train_dispatched = pyqtSignal()
    output_speed = pyqtSignal(List)
    output_route = pyqtSignal(List)
    output_authority = pyqtSignal(int)

    def __init__(self, parent):
        super().__init__(parent)
        self.num_trains_dispatched = 0
        self.trainIDs = []
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setMinimumSize(920, 608)
        self.system_start_time = "07:00:00"
        self.cur_sys_time = "07:00:00"
        
        self.occupancy_old_text = None
        self.old_station = None
        #self.red_line = Line("Red")
        self.green_line = Line("Green", 'Green Line Info.xlsx')

        self.line_edits = []
        
        self.block_occupancies = []
        self.ticket_sales = 0
        self.throughput = 0
        
        self.train_schedule = []
        self.speed_factor = 1

        self.initialize_connections()
        self.start_threads()
        self.initialize_ui()

        """
        need to ensure a few things for iteration 3
        
        grab block occupancies from track controller, attempt to differentiate between them
        
        get ticket sales from track model, remember time of last calculation
        need to exclude passengers from over an hour ago but keep ones within hour
        
        need to be able to dispatch a train
        once dispatched, current system time is departure time, arrival time is input
        destination station input, all stops input - update ui for this
        will calculate suggested speed based off this data, cannot exceed speed limits - must implement this
        can check if suggested speed is over speed limit
        if suggested speed has to go over speed limit, then throw error
        also calculate route - list of blocks from yard to destination station (back to yard?)
        
        also calculate authority - number of blocks from yard to first stop
        
        for scheduled trains - first add to queue, once departure time is reached, call dispatch_train
        ^^same protocols will follow
        
        can create train object that holds all this data to keep track of dispatched trains
        
        station list should auto-populate from imported file
        
        need to import schedule file, all trains added to schedule 
        
        keep track of dispatched trains
        """



    def set_suggested_speed(self, speeds):
        self.output_speed.emit(speeds)
        
    def set_route(self, route):
        self.output_route.emit(route)
        
    def set_authority(self, authority):
        self.output_authority(authority)
    
    def get_block_occupancies(self, occupancies):
        self.block_occupancies = occupancies
    
    def get_ticket_sales(self, tickets):
        self.ticket_sales = tickets
        


    def start_threads(self):
        Thread(target=self.update_occupancy_ui).start()
        Thread(target=self.check_mode).start()
        Thread(target=self.check_stations).start()
        Thread(target=self.update_throughput).start()

    def initialize_connections(self):
        self.ui.dispatch_train_btn.clicked.connect(self.dispatch_train)
        self.ui.import_schedule_btn.clicked.connect(self.import_schedule)
        self.ui.apply_changes.clicked.connect(self.apply_tb)
        #self.station_update.connect(self.update_stations)
        self.ui.schedule_train_btn.clicked.connect(self.schedule_train)
        self.manual_mode.connect(self.update_manual_mode)
        self.auto_mode.connect(self.update_auto_mode)

    
    def initialize_ui(self):
        self.ui.block_occupancy.setVerticalHeaderLabels([str(i) for i in range(1, 16)])
        self.ui.manual_dispatch_departure.addItem("Station A")
        self.ui.manual_dispatch_departure.addItem("Station B")
        self.ui.manual_dispatch_departure.addItem("Station C")
        self.ui.manual_mode_btn.setChecked(True)
        self.ui.label_9.hide()
        self.ui.manual_dispatch_departure.hide()
        self.ui.manual_dispatch_destination.addItem("Station A")
        self.ui.manual_dispatch_destination.addItem("Station B")
        self.ui.manual_dispatch_destination.addItem("Station C")

    def update_throughput(self):
        while True:
            return

    def check_stations(self):
        while True:
            if (self.ui.manual_dispatch_departure != self.old_station):
                self.station_update.emit()
            time.sleep(0.5)


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
            #self.ui.label.setText(f'Selected File: {filePath}')
            if filePath.endswith('.xlsx'):
                df = pd.read_excel(filePath)
            elif filePath.endswith('.csv'):
                df = pd.read_csv(filePath)
            else:
                self.textEdit.setText("Unsupported file format!")
                return
            #can randomly generate train IDs
            #train_ids = df['Train ID'].tolist()
            #departing_stations = df['Departing From'].tolist() - don't need
            arriving_stations = df['Arriving to'].tolist()
            departure_times = df['Departure Time'].tolist()
            self.update_schedule(train_ids, departing_stations, arriving_stations, departure_times)

            #lines = df['Line'].tolist()
            #infrastructures = df['Infrastructure'].tolist()
            #times = df['Time to Station'].tolist()
        return

    def add_stop(self):
        new_label = QLabel(f"Label")
        new_line_edit = QLineEdit()
        self.line_edits.append(new_line_edit)
        self.stop_layout.addWidget(new_label)
        self.stop_layout.addWidget(new_line_edit)
        
    def dispatch_train(self):
        destination = self.ui.manual_dispatch_destination.currentText()
        departure_time = 
        #get line from ui
        dispatched_line = self.ui.lines_box.getCurrentText()
        if dispatched_line == "Green Line":
            route = self.green_line.get_route(destination)
            speeds = self.green_line.get_velocities(route)
            authority = self.green_line.get_authority()
        random_sequence = ''.join(random.choices(string.ascii_letters, k=4)) + ''.join(random.choices(string.digits, k=4))

        #departure = self.ui.manual_dispatch_departure.currentText()
        destination = self.ui.manual_dispatch_destination.currentText()
        #delta = self.calculate_time(departure, destination)
        dep_time = datetime.strptime(datetime.now().strftime("%H:%M:%S"), "%H:%M:%S")
        #dep_time_str = dep_time.strftime("%H:%M:%S")
        #eta = (dep_time + delta).strftime("%H:%M:%S")
        #self.blue_line_schedule.append(QTreeWidgetItem([str(train), departure, destination, str(dep_time_str), str(eta)]))
        self.ui.dispatched.addTopLevelItem(QTreeWidgetItem([str(train), str(current_block),str(authority), destination]))
        item = QTableWidgetItem()
        item.setBackground(Qt.GlobalColor.green)
        #setting route, authority, suggested speed
        self.set_route(route)
        self.set_suggested_speed(speeds)
        self.set_authority(authority)
        #reset stop layout
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
            self.blue_line_schedule.append(QTreeWidgetItem([str(train), destination, str(dep_time_str), str(eta)]))
            self.ui.schedule.addTopLevelItem(QTreeWidgetItem([str(train), destination, str(dep_time_str), str(eta)]))
        elif self.ui.auto_mode_btn.isChecked():
            # Assuming train_ids, departure_, destination_, and departure_time_ are lists
            for t_id, dep, dest, dep_time in zip(train_ids, departure_, destination_, departure_time_):
                if isinstance(dep_time, str):
                    dep_time_obj = datetime.strptime(dep_time, "%H:%M:%S").time()
                else:
                    dep_time_obj = dep_time

                delta = self.calculate_time(dep, dest)
                eta = (datetime.combine(date.today(), dep_time_obj) + delta).time().strftime("%H:%M:%S")

                self.blue_line_schedule.append(QTreeWidgetItem([str(t_id), dest, str(dep_time_obj), str(eta)]))
                self.ui.schedule.addTopLevelItem(QTreeWidgetItem([str(t_id), dest, str(dep_time_obj), str(eta)]))
    
        return
    

#change to updated_block_occupancy function
#receive block occupancies from track controller, upon receiving, update corresponding blocks
    def update_block_occupancy(self):
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
            color = Qt.GlobalColor.white
            if block_state == "Occupied":
                color = Qt.GlobalColor.green
            elif block_state == "Active":
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

        return


    def calc_throughput(self):
        #get last time throughput was calculated
        #get ticket sales from track model
        
        return total_throughput

    #get departure time, arrival time, destination station, stops
    def schedule_train(self):
        #trainID = 
        departure = self.ui.manual_dispatch_departure.currentText()
        
        delta = self.calculate_time(departure, destination)
        

        dep_time_str = self.ui.departure_time.text()
        dep_time_obj = datetime.strptime(dep_time_str, "%H:%M:%S")
        

        eta_obj = (datetime.combine(datetime.today(), dep_time_obj.time()) + delta).time()
        eta_str = eta_obj.strftime("%H:%M:%S")
        
        self.blue_line_schedule.append(QTreeWidgetItem([str(train), destination, dep_time_str, eta_str]))
        self.ui.schedule.addTopLevelItem(QTreeWidgetItem([str(train), destination, dep_time_str, eta_str]))
        return

    #checks for any changes in ui / variables and updates ui accordingly
    def update_ui(self):
        return
    
    def close_tracks(self, track_list):
        for track in track_list:
            return



    
if __name__ != "__main__":
    parent_widget = QWidget()
    ctc_widget = CTC()
    MainWindow.setCentralWidget(ctc_widget)
    MainWindow.show()