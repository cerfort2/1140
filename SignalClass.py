import typing
from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QApplication, QComboBox, QMainWindow, QFileDialog
from PyQt6 import QtCore, QtGui, QtWidgets 



# class Connection(QtCore.QObject):
#     def __init__(self, data) -> None:
#         super().__init__()
#         self.signal = QtCore.pyqtSignal()

class CTC:
    def __init__(self):
        ctcsignal = QtCore.py

class TrackC:
    def __init__(self) -> None:
        pass

class TrackM:
    def __init__(self) -> None:
        pass

class TrainM:
    def __init__(self) -> None:
        pass

class TrainC:
    def __init__(self):
        pass



class God():
    def __init__(self):
        self.ctc = CTC()
        self.trackController = TrackC()
        self.trackModel = TrackM()
        self.trainModel = TrainM()
        self.trainController = TrainC() 

    def setupConnections(self):
        pass




    

app = QApplication([])

ui = God()
ui.setupConnections()

# # Start the event loop.
app.exec()




    

    




    



