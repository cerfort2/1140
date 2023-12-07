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
        self.timeStep = 50

        self.ctc = CTC()
        self.trackControllerHW = HWTrackControllerGUI()
        #self.trackControllerSW = SoftwareTrackControllerGUI()
        self.trackModel = functionalUI()
        self.trainInterface = train_model_interface_software()
        self.setupConnections()
        self.create_modules()

    def setupConnections(self):
        #GOD UI main page
        self.ctc_btn.clicked.connect(self.openCTCGUI)
        self.track_model_btn.clicked.connect(self.openTrackModelGUI)
        self.track_controller_btn.clicked.connect(self.openTrackControllerHWGUI)
        #self.track_controller_sw_btn.clicked.connect(self.openTrackControllerSW)
        
        
        #timer
        self.MainTimer.start(self.timeStep)
        self.MainTimer.timeout.connect(self.onTimeoutFunctions)


        #Timer functions between CTC and Track Controller
        #Hardware
        self.trackControllerHW.CTCOccupancyHW.connect(self.ctc.get_block_occupancies)
        #Software
        #self.trackControllerSW.ctcOccupancy.connect(self.ctc.get_block_occupancies)
        self.ctc.train_dispatched.connect(self.init_train)

        #Sent from CTC to Track Controller
        self.ctc.train_dispatched.connect(self.trackControllerHW.createNewTrainData)
        #self.ctc.train_dispatched.connect(self.trackControllerSW.sendTrainDetails)

        #CTC to initialize train on dispatch

        #Timer functions between Track Model and Track Controller
        #Hardware
        self.trackModel.trackModel.trackControllerOccupancy.connect(self.trackControllerHW.getOccupancy)
        self.trackModel.trackModel.trackControllerInitializeLine.connect(self.trackControllerHW.greenLine.setTracks)
        self.trackControllerHW.trackModelSuggestedSpeedHW.connect(self.trackModel.trackModel.suggestedSpeed)
        self.trackControllerHW.trackModelAuthorityHW.connect(self.trackModel.trackModel.authority)
        self.trackControllerHW.trackModelSendRouteHW.connect(self.trackModel.trackModel.route)
        self.trackControllerHW.trackModelTrackDataHW.connect(self.trackModel.trackModel.controlModel)
        

        
        #Software
        # self.trackModel.trackModel.trackControllerInitializeLine.connect(self.trackControllerSW.setDisplay)
        # self.trackModel.trackModel.trackControllerOccupancy.connect(self.trackControllerSW.setOccupancy)
        # self.trackControllerSW.trackModelData.connect(self.trackModel.trackModel.controlModel)
        # self.trackControllerSW.trackModelRoute.connect(self.trackModel.trackModel.route)
        # self.trackControllerSW.trackModelSpeed.connect(self.trackModel.trackModel.suggestedSpeed)
        # self.trackControllerSW.trackModelAuthority.connect(self.trackModel.trackModel.authority)
        
        ##
        self.trackModel.trackModel.trainModelRouteNames.connect(self.trainInterface.set_route)




        #Once calls for both
        self.trackModel.trackModel.initTrack()
        self.trainInterface.track_model_occupancy_list.connect(self.trackModel.trackModel.updateOccupancy)
        #self.trackModel.trackModel.CTCticketSales.connect(self.ctc.record_ticket_sales)
        

        

    def init_train(self):
        self.trainInterface.new_train()
        self.trainInterface.show_GUI(1)
        #self.trackModel.trackModel.trainModelSuggestedSpeed.connect(self.trainInterface.access_train(len(self.trainInterface.trains)).set_suggested_speeds)
        #self.trackModel.trackModel.trainModelAuthority.connect(self.trainInterface.access_train(1).new_authoriy)
        #self.trackModel.trackModel.trainModelGrade.connect(self.trainInterface.set_slopes)
        # self.trackModel.trackModel.trainModelApproachingBeacon.connect(self.trainInterface.access_train(1).set_station_data)
        #self.trackModel.trackModel.trainModelSwitchBeacon.connect(self.trainInterface.access_train(1).set_switch_data)
        #self.trackModel.trackModel.trainModelStationBeacon.connect(self.trainInterface.access_train(1).set_station_data)
        self.trackModel.trackModel.trainModelPolarity.connect(self.trainInterface.set_polarities)

        self.trainInterface.access_train(1).occupancy = "Z151"
        # self.trackModel.trackModel.route(["Z151", "J62","K63", "K64", "K65", "K66", "K67", "K68", "L69", "L70", "L71", "L72", "L73"])

    #on timeout emissions
    def onTimeoutFunctions(self):
        # self.trackModel.trackModel.initTrack()
        #self.trackController.sendSpeed()
        self.trackModel.trackModel.emitOccupancy()
        self.trackControllerHW.sendData()
        # self.trackModel.trackModel.emitStationBeacon()
        # self.trackModel.trackModel.emitSwitchBeacon()
        # self.trackModel.trackModel.emitApproachingBeacon()
        self.trainInterface.get_occupancies()
        self.trackModel.updateMap()
        if self.trainInterface.trains != []:
            self.trainInterface.update_trains()
            self.trackModel.trackModel.polarity()
    
    def create_modules(self):
        #setup track model
        self.widget = QWidget()
        self.trackModel.setupUi(self.widget)
        self.trackModel.connect()
        
        self.widget2 = QWidget()
        self.trackControllerHW.setupUi(self.widget2)
        self.trackControllerHW.connectFunctions()
        
        self.widget3 = QWidget()
        self.ctc.setupUi(self.widget3)
        self.ctc.initialize_ctc()

        self.widget4 = QWidget()
        # self.trackControllerSW.setupUi(self.widget4)
        # self.trackControllerSW.connectFunctions()

    def openTrackModelGUI(self):
        self.widget.show()

    def openTrackControllerHWGUI(self):
        self.widget2.show()
    
    def openCTCGUI(self):
        self.widget3.show()
    
    # def openTrackControllerSW(self):
    #     self.widget4.show()




app = QApplication([])
ui = God()
ui.show()
app.exec()

