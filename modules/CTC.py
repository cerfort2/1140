import os
import subprocess
import time

from pathlib import Path
from typing import List, Optional

from PyQt6.QtCore import pyqtSignal, QEvent, Qt
from PyQt6.QtWidgets import QTreeWidgetItem, QWidget


from ui_gen.CTC import Ui_MainWindow


class CTC(QMainWidget):
    def __init__(self):
        self.num_trains = 5
        self.ui.dispatch_btn.clicked.connect(self.dispatch_trains)
        self.ui = Ui_MainWindow()
    

    def dispatch_train(self):
        self.num_trains -= 1
        self.train = self.ui.train_sel.getCurrentValue()
        speed = self.ui.mph_box.getCurrentValue()
        route = self.ui.route_box.getCurrentValue()
        authority = self.ui.authority_box.getCurrentValue()

        self.update_schedule()

        return [speed, route, authority]
    
    def update_schedule(self):
        return


    def calc_throughput(self, passengers):
        #self.throughput = passengers/time_elapsed
        return
        
    def close_track(self, track_num):
        return
    
    def schedule_train(self):
        return