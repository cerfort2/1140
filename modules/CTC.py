#import os
#import subprocess
#import time
import pandas as pd

from datetime import datetime, timedelta

from threading import Thread, Event
from pathlib import Path
from typing import List, Optional

from PyQt6.QtCore import pyqtSignal, QEvent, Qt
from PyQt6.QtWidgets import QTreeWidgetItem, QWidget, QFileDialog, QMainWindow


from ui_gen.CTC import Ui_MainWindow


class CTC(QWidget):
    def __init__(self):
        self.num_trains_dispatched = 0
        self.trainID = 0
        
        self.ui = Ui_MainWindow()
        self.ui.show(self)
        self.initialize_connections()
        self.start_threads()
        

        self.red_line = ['SHADYSIDE', 'HERRON AVE', 'SWISSVILLE', 'PENN STATION', 'FIRST AVE', 'STATION SQUARE', 'SOUTH HILLS JUNCTION']
        self.green_line_both = ['PIONEER', 'EDGEBROOK', 'WHITE', 'SOUTH BANK', 'CENTRAL', 'INGLEWOOD', 'OVERBROOK', 'GLENBURY', 'DORMONT', 'MT LEBANON', 'POPLAR', 'CASTLE SHANNON']
        self.blue_line = ['Station A', 'Station B', 'Station C']
        self.blue_line_times = [1,1,1]




        

    def initialize_connections(self):
        self.ui.dispatch_btn.clicked.connect(self.dispatch_trains)
        self.ui.manual_mode_tb.clicked.connect(self.update_mode_tb)
        self.ui.import_schedule_btn.clicked.connect(self.import_schedule)

    def start_threads(self):
        Thread(target=self.update_occupancy_ui).start()
        Thread(target=self.update_mode).start()

    def update_occupancy_ui(self):
        if (self.ui.occupancy_line_box.currentText() == "Red Line"):
            self.ui.block_occupancy.setVerticalHeaderLabels([str(i) for i in range(1, 61)])
        elif(self.ui.occupancy_line_box.currentText() == "Green Line"):
            self.ui.block_occupancy.setVerticalHeaderLabels([str(i) for i in range(1, 142)])
        elif(self.ui.occupancy_line_box.currentText() == "Blue Line"):
            self.ui.block_occupancy.setVerticalHeaderLabels([str(i) for i in range(1, 16)])

    def update_mode(self):
        if(self.ui.manual_mode_btn.isChecked()):
            self.ui.auto_mode_btn.setChecked(False)
            self.ui.maint_mode_btn.setChecked(False)
            self.ui.import_schedule_btn.setEnabled(False)

        if(self.ui.auto_mode_btn.isChecked()):
            self.ui.auto_mode_btn.setChecked(False)
            self.ui.maint_mode_btn.setChecked(False)
        if(self.ui.maint_mode_btn.isChecked()):
            self.ui.manual_mode_btn.setChecked(False)
            self.ui.maint_mode_btn.setChecked(False)

    def import_schedule(self):
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)", options=options)

        if filePath:
            self.label.setText(f'Selected File: {filePath}')
            if filePath.endswith('.xlsx'):
                df = pd.read_excel(filePath)
            elif filePath.endswith('.csv'):
                df = pd.read_csv(filePath)
            else:
                self.textEdit.setText("Unsupported file format!")
                return
        
        lines = df['Line'].tolist()
        infrastructures = df['Infrastructure'].tolist()
        times = df['Time to Station'].tolist()

        return



    def dispatch_train(self):
        #self.num_trains_dispatched += 1
        #self.train = self.ui.train_sel.getCurrentValue()
        #speed = self.ui.mph_box.getCurrentValue()
        #route = self.ui.route_box.getCurrentValue()
        #authority = self.ui.authority_box.getCurrentValue()

        self.update_schedule()

        return #[speed, route, authority]
    
    #updates schedule on main page
    def update_schedule(self):
        if(self.ui.manual_mode_btn.isChecked()):
            train = self.trainID
            self.trainID+=1
            departure = self.ui.manual_dispatch_departure.currentText()
            destination = self.ui.manual_dispatch_destination.currentText()
            delta = self.calculate_time(departure, destination)
            dep_time = datetime.strptime("00:00:00", "%H:%M:%S")
            eta = dep_time + delta
            self.ui.schedule.addTopLevelItem(QTreeWidgetItem[train, departure, destination, dep_time, eta])
        if(self.ui.auto_mode_btn.isChecked()):
            train = self.trainID
            self.trainID+=1
        
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


    def calc_throughput(self, passengers):
        #self.throughput = passengers/time_elapsed
        return
        
    def close_track(self, track_num):
        return
    
    def schedule_train(self):
        return
    
    #updates the ui of tb when manual mode is selected/deselected
    def update_mode_tb(self):
        return
    
    
