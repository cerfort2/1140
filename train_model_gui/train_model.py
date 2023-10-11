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
        pass

    def display(self):
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec())

    def update_vals(self):
        pass
        
        
new_model_ui = train_model()
new_model_ui.display()