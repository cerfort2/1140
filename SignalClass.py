import typing
from PyQt6.QtCore import QObject, pyqtSignal, QTimer
from PyQt6.QtWidgets import QApplication, QComboBox, QMainWindow, QFileDialog
from PyQt6 import QtCore, QtGui, QtWidgets

##ALL FUNCTIONAL OBJECTS NEED TO DO THE FOLLOWING

#1. Inherit QtCore.QObject, 
# and make sure your init function includes a super().__init__() call

#2. If you are receiving a signal, 
#   make a function with an argument

#3. If you are sending a signal,
# define the signal with a descriptive name(victor please) and give it its type
# Then within the function you return the signal value, instead of returning the value, emit the value.

#4. #profit

class CTC(QObject):
    def __init__(self) -> None:
        super().__init__()

class TrackC(QObject):
    def __init__(self) -> None:
        super().__init__()

    def getOccupancy(self, occupancy):
        print("I am the track Controller and this is what I received : " + str(occupancy)) 

class TrackM(QObject):
    firstSignal = pyqtSignal(list)

    def __init__(self) -> None:
        super().__init__()
        
    
    def setOccupancy(self):
        self.firstSignal.emit([[True, False, True],["hi"],["bye"]])

class TrainM(QObject):
    def __init__(self) -> None:
        super().__init__()

class TrainC(QObject):
    def __init__(self) -> None:
        super().__init__()


class God():
    def __init__(self):
        self.MainTimer = QTimer()
        self.timeStep = 1000

        self.ctc = CTC()
        self.trackController = TrackC()
        self.trackModel = TrackM()
        self.trainModel = TrainM()
        self.trainController = TrainC() 

    def setupConnections(self):
        ###timer
        self.MainTimer.start(self.timeStep)
        self.MainTimer.timeout.connect(self.onTimeoutFunctions)

        self.trackModel.firstSignal.connect(self.trackController.getOccupancy)

    ##on timeout emissions
    def onTimeoutFunctions(self):
        self.trackModel.setOccupancy()





        


app = QApplication([])

ui = God()
ui.setupConnections()
# # Start the event loop.
app.exec()

    

    




    



