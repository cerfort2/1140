import typing
from PyQt6.QtCore import QObject, pyqtSignal, QTimer
from PyQt6.QtWidgets import QApplication, QComboBox, QMainWindow, QFileDialog
from PyQt6 import QtCore, QtGui, QtWidgets
from UIFunctionality import *
from trackmodelguitest import *
from SoftwareTrainControllerGUI import *
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


class God(QMainWindow):
    def __init__(self):
        super().__init__()
        self.MainTimer = QTimer()
        self.timeStep = 1000

        self.ctc = CTC()
        self.trackControllerHW = HWTrackControllerGUI()
        self.trackControllerSW = SoftwareTrackControllerGUI()
        self.trackModel = functionalUI()
        self.trainModel = TrainM()
        self.trainController = SoftwareTrainControllerGUI() 

    def setupConnections(self):
        #timer
        self.MainTimer.start(self.timeStep)
        self.MainTimer.timeout.connect(self.onTimeoutFunctions)


        self.trackModel.trackModel.trackControllerOccupancy.connect(self.trackControllerHW.getOccupancy)
        self.trackModel.trackModel.trackControllerInitializeLine.connect(self.trackControllerHW.greenLine.setTracks)
        self.trackControllerHW.trackModelSuggestedSpeedHW.connect(self.trackModel.trackModel.suggestedSpeed)
        self.trackModel.trackModel.trackControllerInitializeLine.connect(self.trackControllerSW.setDisplay)
        self.trackControllerSW.trackModelData.connect(self.trackModel.trackModel.controlModel)

        #Once calls
        self.trackModel.trackModel.initTrack()
        

    #on timeout emissions
    def onTimeoutFunctions(self):
        self.trackControllerSW.getData()
        # self.trackControllerSW.mode_handler()
        self.trackControllerHW.sendSpeed()
        self.trackModel.trackModel.emitOccupancy()
        self.trainController.update_time()

    def openTrackModelGUI(self):
        self.widget = QWidget()
        self.trackModel.setupUi(self.widget)
        self.trackModel.connect()
        self.widget.show()

    def openTrainControllerGUI(self):
        self.widget1 = QWidget()
        self.trainController.setupUi(self.widget1)
        self.trainController.connect()
        self.widget1.show()

    def openTrackControllerHWGUI(self):
        self.widget2 = QWidget()
        self.trackControllerHW.setupUi(self.widget2)
        self.trackControllerHW.connectFunctions()
        self.widget2.show()

    def openTrackControllerSWGUI(self):
        self.widget3 = QWidget()
        self.trackControllerSW.setupUi(self.widget3)
        self.trackControllerSW.retranslateUi(self.widget3)
        self.trackControllerSW.connectFunctions()
        self.widget3.show()
        








        


app = QApplication([])
ui = God()
ui.setupConnections()
ui.openTrackModelGUI()
ui.openTrainControllerGUI()
ui.openTrackControllerHWGUI()
ui.openTrackControllerSWGUI()
# # Start the event loop.
app.exec()

    

    




    



