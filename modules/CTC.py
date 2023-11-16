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
from PyQt6.QtWidgets import QTreeWidgetItem, QWidget, QFileDialog, QMainWindow, QApplication, QTableWidgetItem, QLabel, QLineEdit, QHeaderView

from modules.Line import Line
from modules.CTC_new import Ui_Form


class Train:
    def __init__(self, trainID, destination, departure_time, arrival_time, stops):
        self.trainID = trainID
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.stops = stops

class CTC(Ui_Form, QWidget):
    occupancy_update = pyqtSignal()
    station_update = pyqtSignal()
    manual_mode = pyqtSignal()
    auto_mode = pyqtSignal()
    maint_mode = pyqtSignal()
    train_dispatched = pyqtSignal(list, int, list)
    schedule_dispatch = pyqtSignal()
    stop_update = pyqtSignal()
    #output_speed = pyqtSignal(list)
    #output_route = pyqtSignal(list)
    #output_authority = pyqtSignal(int)

    def __init__(self):
        super().__init__()
       
        """
        need to ensure a few things for iteration 3
        
        grab block occupancies from track controller, attempt to differentiate between them
        
        get ticket sales from track model, remember time of last calculation
        need to exclude passengers from over an hour ago but keep ones within hour
        
        
        also calculate authority - number of blocks from yard to first stop
        
        for scheduled trains - first add to queue, once departure time is reached, call dispatch_train
        ^^same protocols will follow
                        
        need to import schedule file, all trains added to schedule 
        
        keep track of dispatched trains
        REFERENCE:

        self.dispatch_train_btn - dispatches train
        self.schedule_train_btn - schedules train
        self.arrival_time_dis - arrival time for dispatching train
        self.manual_dispatch_line - selecting line for dispatch/schedule
        self.manual_dispatch_destination - destination station
        self.stop_box_list - stopping stations
        self.add_stop - adds stop
        self.departure_time - departure time for scheduling train
        self.arrival_time - arrival time for scheduling train
        self.schedule_lines_box - selecting schedule for line
        self.schedule - schedule qtreewidget
        self.dispatched - dispatched qtreewidget
        self.block_occupancy - qtablewidget displaying block occupancy
        self.occupancy_line_box - selecting line for block occupancy
        self.throughput_val - value of throughput displayed
        self.dispatched_trains_line - selecting line to show which trains have been dispatched
        self.system_time - displays current time of system
        self.remove_schedule - button to remove from schedule
        """
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
        self.old_station = None
        #self.red_line = Line("Red")
        self.green_line = Line("Green", 'Green Line Info.xlsx')

        self.stops = []
        self.green_line_stations = ["K65: GLENBURY", "L73: DORMONT", "N77: MT LEBANON", "O88: POPLAR", "P96: CASTLE SHANNON", "T105: DORMONT","U114: GLENBURY", "W123: OVERBROOK", "W132: INGLEWOOD", "W141: CENTRAL", "A2: PIONEER", "C9: EDGEBROOK", "D16: MONKEYWAY", "F22: WHITED", "G31: SOUTH BANK", "I39: CENTRAL", "I48: INGLEWOOD", "I57: OVERBROOK"]
        
        self.ticket_sales_log = []
        self.block_occupancies = []
        self.last_ts_updated = None
        self.throughput = 0
        
        self.train_schedule = []
        self.trains_dispatched = []
        self.speed_factor = 1

        self.initialize_connections()
        self.start_threads()
        self.initialize_ui()


#outputs
    def train_dispatch(self, route, authority, speed):
        self.train_dispatched.emit(route, authority, speed)
    """
    def set_suggested_speed(self, speeds):
        self.output_speed.emit(speeds)
        
    def set_route(self, route):
        self.output_route.emit(route)
        
    def set_authority(self, authority):
        self.output_authority(authority)
    """
#inputs
    def get_block_occupancies(self, occupancies):
        self.block_occupancies = occupancies
        self.update_block_occupancy(self.block_occupancies)
    
    def get_ticket_sales(self, tickets):
        ticket_sales = tickets
        self.record_ticket_sales(ticket_sales)
        


    def start_threads(self):
        Thread(target=self.update_occupancy_ui).start()
        Thread(target=self.check_mode).start()
        Thread(target=self.check_stations).start()
        Thread(target=self.update_throughput).start()
        Thread(target=self.start_dispatch_check).start()

    def initialize_connections(self):
        self.dispatch_train_btn.clicked.connect(self.dispatch_train)
        self.import_schedule_btn.clicked.connect(self.import_schedule)
        self.station_update.connect(self.update_stations)
        self.schedule_train_btn.clicked.connect(self.schedule_train)
        self.manual_mode.connect(self.update_manual_mode)
        self.auto_mode.connect(self.update_auto_mode)
        self.add_stop.clicked.connect(self.add_stops)
        self.stop_update.connect(self.update_stops)
        self.schedule_dispatch.connect(self.dispatch_scheduled_train)

    
    def initialize_ui(self):
        self.manual_mode_btn.setChecked(True)
        self.import_schedule_btn.hide()


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

    def updated_dispatched_trains_info(self):
        while True:
            return
        
    def check_stations(self):
        while True:
            if (self.manual_dispatch_destination != self.old_station):
                self.old_station = self.manual_dispatch_destination
                self.station_update.emit()
                self.stop_update.emit()
            time.sleep(0.5)

    def update_stations(self):
        if self.manual_dispatch_line.currentText() == "Green Line":
            for station in self.green_line_stations:
                if station not in self.stops:
                    self.manual_dispatch_destination.addItem(station)

    def update_stops(self):
        self.stop_box_list.clear()
        if self.manual_dispatch_line.currentText() == "Green Line":
            current_destination = self.manual_dispatch_destination.currentText()
            for station in self.green_line_stations:
                if station != current_destination and station not in self.stops:
                    self.stop_box_list.addItem(station)


    def check_occupancy(self):
        if(self.occupancy_line_box.currentText() != self.occupancy_old_text):
            self.occupancy_update.emit()

    def update_occupancy_ui(self):
        if (self.occupancy_line_box.currentText() == "Red Line"):
            self.occupancy_old_text = "Red Line"
            self.block_occupancy.setVerticalHeaderLabels([str(i) for i in range(1, 61)])
        elif(self.occupancy_line_box.currentText() == "Green Line"):
            self.occupancy_old_text = "Green Line"
            self.block_occupancy.setRowCount(141)
            self.block_occupancy.setVerticalHeaderLabels([str(i) for i in range(1, 142)])
            for i, infrastructure in enumerate(self.infrastructure_data):
                item = QTableWidgetItem(infrastructure)
                item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                self.block_occupancy.setItem(i, 1, item)  # Column index 1 for the second column
                self.block_occupancy.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)


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
        self.dispatch_train_btn.setEnabled(True)
        self.manual_widget.show()
        # for i in range(self.manual_layout.count()):
        #     widget = self.manual_layout.itemAt(i).widget()
        #     if widget is not None:
        #         widget.show()
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
        self.add_stop.hide()
        # for i in range(self.manual_layout.count()):
        #     widget = self.manual_layout.itemAt(i).widget()
        #     if widget is not None:
        #         widget.hide()
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

            for dest, d_time, a_time, stop in zip(arrival_stations, departure_times, arrival_times, stopping_at):
                train_id = ''.join(random.choices(string.ascii_letters, k=4)) + ''.join(random.choices(string.digits, k=4))
                # Add each value to its respective list
                train_ids.append(train_id)
                destinations.append(dest)
                dep_times.append(d_time)
                arr_times.append(a_time)
                stops.append([stop.strip() for stop in stop.split(',')])

            # Update the schedule with the new data
            self.update_schedule(train_ids, destinations, dep_times, arr_times, stops)

            # Provide some feedback or update the UI to reflect the changes
            # self.label.setText(f'Schedule imported successfully from {filePath}')
            # ... other UI updates ...
        return


    def add_stops(self):
        stop = self.stop_box_list.currentText()
        if stop in self.stops:
            return
        else:
            self.stops.append(stop)
        index = self.stop_box_list.findText(stop)
        self.stop_box_list.removeItem(index)
        
    def dispatch_train(self):
        destination = self.manual_dispatch_destination.currentText()
        station_list = [destination]
        for stop in self.stops:
            station_list.append(stop)
        arrival_time = QDateTime.fromString(self.arrival_time_dis.text(), "HH:mm:ss").time()
        departure_time = self.cur_sys_time

        #get line from ui
        dispatched_line = self.manual_dispatch_line.currentText()
        num_stops = len(self.stops)
        if dispatched_line == "Green Line":
            route = self.green_line.get_route(station_list)
            speeds = self.green_line.get_velocities(route[0], departure_time, arrival_time, num_stops)
            if len(station_list) == 1:
                next_stop = station_list[0]
            else:
                next_stop = station_list[1]
            authority = self.green_line.get_authority(next_stop)

        trainID = ''.join(random.choices(string.ascii_letters, k=4)) + ''.join(random.choices(string.digits, k=4))
        train = Train(trainID, destination, departure_time, arrival_time, self.stops)
        self.trains_dispatched.append(train)
        self.dispatched.addTopLevelItem(QTreeWidgetItem([str(trainID), "YARD", str(authority), next_stop]))
        print(route)
        print(authority)
        print(speeds)

        self.suggested_speed_tb.setText(str(speeds))
        self.authority_tb.setText(str(authority))
        self.route_tb.setText(str(route[0]))

        #setting route, authority, suggested speed
        self.train_dispatch(route, authority, speeds)
        self.stops = []
        self.arrival_time_dis.clear()

    #get departure time, arrival time, destination station, stops
    def schedule_train(self):
        destination = self.manual_dispatch_destination.currentText()
        station_list = [destination]
        for stop in self.stops:
            station_list.append(stop)
        arrival_time = QDateTime.fromString(self.arrival_time.text(), "HH:mm:ss").time()
        departure_time = QDateTime.fromString(self.departure_time.text(), "HH:mm:ss").time()

        #get line from ui
        dispatched_line = self.manual_dispatch_line.currentText()
        num_stops = len(self.stops)
        if dispatched_line == "Green Line":
            route = self.green_line.get_route(station_list)
            speeds = self.green_line.get_velocities(route[0], departure_time, arrival_time, num_stops)
            if len(station_list) == 1:
                next_stop = station_list[0]
            else:
                next_stop = station_list[1]
            authority = self.green_line.get_authority(next_stop)

        trainID = ''.join(random.choices(string.ascii_letters, k=4)) + ''.join(random.choices(string.digits, k=4))
        stop_string = ""
        for stop in self.stops:
            if stop == self.stops[-1]:
                stop_string += stop
            else:
                stop_string += stop + ","
                
        self.schedule.addTopLevelItem(QTreeWidgetItem([str(trainID), destination, departure_time.toString(), arrival_time.toString(), stop_string]))
        train = Train(trainID, destination, departure_time, arrival_time, self.stops)
        self.train_schedule.append(train)
        
        #self.update_schedule(train)
        self.stops = []
        self.arrival_time.clear()
        self.departure_time.clear()

    def check_for_dispatched(self):
        current_time = self.cur_sys_time
        for train in self.train_schedule:
            if train.departure_time.toString() == self.cur_sys_time.toString():
                self.dispatch_scheduled_train(train)
                self.train_schedule.remove(train)
    
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
        station_list = [destination]
        for stop in self.stops:
            station_list.append(stop)
        route = self.green_line.get_route(station_list)
        num_stops = len(self.stops)

        speeds = self.green_line.get_velocities(route[0], departure_time, arrival_time, num_stops)
        if len(station_list) == 1:
            next_stop = station_list[0]
        else:
            next_stop = station_list[1]

        authority = self.green_line.get_authority(next_stop)
        self.dispatched.addTopLevelItem(QTreeWidgetItem([str(trainID), "YARD", str(authority), next_stop]))
        
        self.remove_train_from_schedule(trainID)
        self.train_dispatch(route, authority, speeds)

    def remove_train_from_schedule(self, trainID):
        root = self.schedule.invisibleRootItem()
        for i in range(root.childCount()):
            item = root.child(i)
            if item.text(0) == trainID:  # Assuming the train ID is in the first column
                root.removeChild(item)
                break
            
    #updates schedule on main page
    def update_schedule(self, train_ids="0", destination_="0", departure_time_="0", arrival_time_="0", stops_="0"):
        if(self.manual_mode_btn.isChecked()):
            train = self.trainID
            self.trainID+=1
            departure = self.manual_dispatch_departure.currentText()
            destination = self.manual_dispatch_destination.currentText()
            delta = self.calculate_time(departure, destination)
            dep_time = datetime.strptime(datetime.now().strftime("%H:%M:%S"), "%H:%M:%S")
            dep_time_str = dep_time.strftime("%H:%M:%S")
            eta = (dep_time + delta).strftime("%H:%M:%S")
            self.blue_line_schedule.append(QTreeWidgetItem([str(train), destination, str(dep_time_str), str(eta)]))
            self.schedule.addTopLevelItem(QTreeWidgetItem([str(train), destination, str(dep_time_str), str(eta)]))
        elif self.auto_mode_btn.isChecked():
            # Assuming train_ids, departure_, destination_, and departure_time_ are lists
            for t_id, dest, dep_time, arr_time, stop in zip(train_ids, destination_, departure_time_, arrival_time_, stops_):
                # if isinstance(dep_time, str):
                #     dep_time_obj = datetime.strptime(dep_time, "%H:%M:%S").time()
                # else:
                #     dep_time_obj = dep_time
                
                #self.blue_line_schedule.append(QTreeWidgetItem([str(t_id), dest, str(dep_time_obj), str(eta)]))
                train = Train(t_id, dest, dep_time, arr_time, stop)
                self.train_schedule.append(train)
                self.schedule.addTopLevelItem(QTreeWidgetItem([str(t_id), str(dest), str(dep_time), str(arr_time), str(stop)]))
        return
    

#change to updated_block_occupancy function
#receive block occupancies from track controller, upon receiving, update corresponding blocks

    def update_block_occupancy(self, occupancies):
        # Assuming 'occupancies' is a list of bools where True represents occupied and False represents open

        for index, is_occupied in enumerate(occupancies):
            # Determine the color based on occupancy
            color = Qt.GlobalColor.green if is_occupied else Qt.GlobalColor.white
            status = "Occupied" if is_occupied else "Open"

            # Assuming the "Occupancy" column is the first column (0-indexed)
            occupancy_item = self.block_occupancy.item(index, 0)
            if not occupancy_item:  # If the item doesn't exist, create it
                occupancy_item = QTableWidgetItem()
                self.block_occupancy.setItem(index, 0, occupancy_item)

            # Set the background color for the block
            occupancy_item.setBackground(color)

            # Update the "Block Status" in the third column
            status_item = self.block_occupancy.item(index, 2)  # Assuming the "Block Status" column is the third column
            if not status_item:
                status_item = QTableWidgetItem()
                self.block_occupancy.setItem(index, 2, status_item)
            status_item.setText(status)

    def record_ticket_sales(self, new_ticket_sales):
        # Record new ticket sales with the current timestamp
        current_time = datetime.now()
        self.ticket_sales_log.append((current_time, new_ticket_sales))
        # Call the throughput calculation
        self.calc_throughput()

    def calc_throughput(self):
        # Get the current time
        current_time = datetime.now()
        # Calculate the cutoff time for the last hour
        one_hour_ago = current_time - timedelta(hours=1)
        
        # Filter the sales that occurred within the last hour
        recent_sales = [sales for timestamp, sales in self.ticket_sales_log if timestamp > one_hour_ago]

        # Calculate the total throughput for the last hour
        total_throughput = sum(recent_sales)

        # Optionally remove old entries outside of the 1-hour window
        self.ticket_sales_log = [(timestamp, sales) for timestamp, sales in self.ticket_sales_log if timestamp > one_hour_ago]

        # Return or update the UI with the total throughput
        return total_throughput
    
    def close_tracks(self, track_list):
        for track in track_list:
            return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CTC()
    widget = QWidget()
    window.setupUi(widget)
    window.initialize_ctc()
    widget.show()
    sys.exit(app.exec())
