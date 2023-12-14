import typing
from PyQt6.QtCore import QObject, pyqtSignal, QTimer
from PyQt6.QtWidgets import QApplication, QComboBox, QMainWindow, QFileDialog
from PyQt6 import QtCore, QtGui, QtWidgets

from Hardware_Track_Controller.UIFunctionality import *
from Track_Model.trackmodelguitest import *
from Software_Track_Controller.SwTrackControlSetup import *
from modules.CTC import *
from modules.Home_ui import Ui_Form as Home
from trains_interface.train_model_interface_software import train_model_interface_software

##ALL FUNCTIONAL OBJECTS NEED TO DO THE FOLLOWING

#1. Inherit QtCore.QObject, 
# and make sure your init function includes a super().__init__() call

#2. If you are receiving a signal, 
#   make a function with an argument

#3. If you are sending a signal,
# define the signal with a descriptive name(victor please) and give it its type
# Then within the function you return the signal value, instead of returning the value, emit the value.

#4. #profit

"""class CTC(QObject):
    
    def __init__(self) -> None:
        super().__init__()
"""
class TrackC(QObject):
    def __init__(self) -> None:
        super().__init__()

    def getOccupancy(self, occupancy):
        print("I am the track Controller and this is what I received : " + str(occupancy)) 

class TrackM(QObject):
    firstSignal = pyqtSignal(list)

    def __init__(self) -> None:
        super().__init__()

class TrainM(QObject):
    def __init__(self) -> None:
        super().__init__()

class TrainC(QObject):
    def __init__(self) -> None:
        super().__init__()

class God(Home, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.MainTimer = QTimer()
        self.timeStep = 1000

        self.ctc = CTC()

        #HW Track Controller
        #self.trackController = HWTrackControllerGUI()

        #SW Track Controller
        self.trackController = SoftwareTrackControllerGUI()

        self.trackModel = functionalUI()
        self.trainInterface = train_model_interface_software()
        self.setupConnections()
        self.create_modules()


    def setupConnections(self):
        #GOD UI main page
        self.ctc_btn.clicked.connect(self.openCTCGUI)
        self.track_model_btn.clicked.connect(self.openTrackModelGUI)
        self.track_controller_sw_btn.clicked.connect(self.opentrackControllerGUI)
        #self.track_controller_sw_btn.clicked.connect(self.openTrackControllerSW)

        #Simulation speed and Pause
        self.verticalSlider.valueChanged.connect(self.simulationSpeedCalculation)
        self.checkBox.stateChanged.connect(self.simulationSpeedCalculation)
        
        
        #timer
        self.MainTimer.start(self.timeStep)
        self.MainTimer.timeout.connect(self.onTimeoutFunctions)


        #Timer functions between CTC and Track Controller
        #Hardware
        self.trackController.CTCOccupancy.connect(self.ctc.get_block_occupancies)

        #CTC to initialize train on dispatch
        self.ctc.train_dispatched.connect(self.init_train)

        #Sent from CTC to Track Controller
        self.ctc.train_dispatched.connect(self.trackController.createNewTrainData)

        #self.ctc.close

        #Timer functions between Track Model and Track Controller
        self.trackModel.trackModel.trackControllerOccupancy.connect(self.trackController.getOccupancy)
        self.trackController.trackModelSuggestedSpeed.connect(self.trackModel.trackModel.suggestedSpeed)
        self.trackController.trackModelAuthority.connect(self.trackModel.trackModel.authority)
        self.trackController.trackModelSendRoute.connect(self.trackModel.trackModel.route)
        self.trackController.trackModelTrackData.connect(self.trackModel.trackModel.controlModel)
        self.trackController.trackModelStoppedTrains.connect(self.trackModel.trackModel.stopAtBlocks)
        #self.trackmodel.trackmodel.trackController"".connect(self.trackController.getFailure)



        #Only have one of these lines commented out:
        #HW Track Controller
        #self.trackModel.trackModel.trackControllerInitializeLine.connect(self.trackController.greenLine.setTracks)
        #self.trackModel.trackModel.trackControllerInitializeLine.connect(self.trackController.redLine.setTracks)
        #SW Track Controller
        self.trackModel.trackModel.trackControllerInitializeLine.connect(self.trackController.setDisplay)

        
        #Between Train model and Track model
        self.trackModel.trackModel.trainModelRouteNames.connect(self.trainInterface.set_route)
        self.trackModel.trackModel.trainModelStopAtBlocks.connect(self.trainInterface.wayside_stops)
        self.trainInterface.track_model_occupancy_list.connect(self.trackModel.trackModel.updateOccupancy)
        self.trackModel.trackModel.trainModelStationBeacon.connect(self.trainInterface.unpack_beacons)
        self.trackModel.trackModel.trainModelBlockInfo.connect(self.trainInterface.unpack_blocks)
        #must add this connection
        # self.trackModel.trackModel.trainModelStationBeacon.connect(self.trainInterface.?)

        
        #self.trackModel.trackModel.CTCticketSales.connect(self.ctc.record_ticket_sales)
        

    def init_train(self):
        self.trainInterface.new_train()
        self.trainInterface.show_GUI(len(self.trainInterface.trains))

    #on timeout emissions
    def onTimeoutFunctions(self):
        #self.trackController.sendSpeed()
        self.trackModel.trackModel.emitOccupancy()
        self.trackController.sendData()
        # self.trackModel.trackModel.emitSwitchBeacon()
        # self.trackModel.trackModel.emitApproachingBeacon()
        self.trainInterface.get_occupancies()
        if self.trainInterface.trains != []:
            self.trackModel.trackModel.emitStationBeacon()
            self.trainInterface.update_trains()
            self.trackModel.trackModel.polarity()
            self.trackModel.trackModel.getOccupiedBlockInfo()
    
    def simulationSpeedCalculation(self):
        if self.checkBox.isChecked():
            self.timeStep = 9999999 #large time step to simulate pause
        else:
            print(self.verticalSlider.value())
            self.timeStep = 1000/self.verticalSlider.value()

        self.MainTimer.start(int(self.timeStep))

    def create_modules(self):
        #Track Model
        self.widget = QWidget()
        self.trackModel.setupUi(self.widget)
        self.trackModel.connect()
        
        #HW Track Controller
        self.widget2 = QWidget()
        self.trackController.setupUi(self.widget2)
        self.trackController.connectFunctions()
        
        #CTC
        self.widget3 = QWidget()
        self.ctc.setupUi(self.widget3)
        self.ctc.initialize_ctc()


    def openTrackModelGUI(self):
        self.widget.show()

    def opentrackControllerGUI(self):
        self.widget2.show()
    
    def openCTCGUI(self):
        self.widget3.show()
    




app = QApplication([])
ui = God()
ui.show()
app.exec()

