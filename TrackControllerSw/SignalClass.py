import typing
from PyQt6.QtCore import QObject, pyqtSignal, QTimer
from PyQt6.QtWidgets import QApplication, QComboBox, QMainWindow, QFileDialog
from PyQt6 import QtCore, QtGui, QtWidgets
from SwTrackControlSetup import *

##ALL FUNCTIONAL OBJECTS NEED TO DO THE FOLLOWING

#1. Inherit QtCore.QObject, 
# and make sure your init function includes a super().__init__() call

#2. If you are receiving a signal, 
#   make a function with an argument

#3. If you are sending a signal,
# define the signal with a descriptive name(victor please) and give it its type
# Then within the function you return the signal value, instead of returning the value, emit the value.

#4. #profit
class TrackC(QObject):
    def __init__(self) -> None:
        super().__init__()


class God(QMainWindow):
    def __init__(self):
        super().__init__()
        self.MainTimer = QTimer()
        self.timeStep = 1000

        self.trackControllerSW = SoftwareTrackControllerGUI()

    def setupConnections(self):
        #timer
        self.MainTimer.start(self.timeStep)
        self.MainTimer.timeout.connect(self.onTimeoutFunctions)
        

    #on timeout emissions
    def onTimeoutFunctions(self):
        pass

    def openTrackControllerSWGUI(self):
        self.widget3 = QWidget()
        self.trackControllerSW.setupUi(self.widget3)
        self.trackControllerSW.retranslateUi(self.widget3)
        self.trackControllerSW.connectFunctions()
        self.widget3.show()
        








        


app = QApplication([])
ui = God()
ui.openTrackControllerSWGUI()
# # Start the event loop.
app.exec()

    

    




    



