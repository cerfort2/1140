import os
import sys
import subprocess
import time

from pathlib import Path
from typing import List, Optional

from PyQt6.QtCore import pyqtSignal, QEvent, Qt
from PyQt6.QtWidgets import QTreeWidgetItem, QWidget
from PyQt6 import QtCore, QtGui, QtWidgets


from train_model_setup import Ui_Dialog

class train_model():

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec())

    def update_schedule(self):
        return


    def calc_throughput(self, passengers):
        #self.throughput = passengers/time_elapsed
        return
        
    def close_track(self, track_num):
        return
    
    def schedule_train(self):
        return


new_model_ui = train_model()