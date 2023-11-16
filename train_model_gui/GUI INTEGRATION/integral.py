from PyQt6.QtCore import QObject, pyqtSignal, QTimer
from PyQt6.QtWidgets import QApplication, QComboBox, QMainWindow, QFileDialog
from PyQt6 import QtCore, QtGui, QtWidgets
from SoftwareTrainControllerGUI import *
from train_model_interface_software import train_model_interface_software

##ALL FUNCTIONAL OBJECTS NEED TO DO THE FOLLOWING

#1. Inherit QtCore.QObject, 
# and make sure your init function includes a super().__init__() call

#2. If you are receiving a signal, 
#   make a function with an argument

#3. If you are sending a signal,
# define the signal with a descriptive name(victor please) and give it its type
# Then within the function you return the signal value, instead of returning the value, emit the value.

#4. #profit


class God(QMainWindow):
    def __init__(self):
        super().__init__()
        self.MainTimer = QTimer()
        self.timeStep = 50


       # self.trainControllergui = SoftwareTrainControllerGUI()
        self.traininterface = train_model_interface_software()
        self.traininterface.new_train()
        #self.traininterface.access_train(1).controller.generateSoftwareTrainUI()

    def setupConnections(self):
        #timer
        self.MainTimer.start(self.timeStep)
        self.MainTimer.timeout.connect(self.onTimeoutFunctions)



    #on timeout emissions
    def onTimeoutFunctions(self):
        self.traininterface.update_trains()


    def openSWTrainControllerGUI(self):
        self.widget1 = QWidget()
        self.traininterface.access_train(1).controller.ui.setupUi(self.widget1)
        self.traininterface.access_train(1).controller.ui.connect()
        self.widget1.show()
    
    def openTrainModelGUI(self):
        self.widget2 = QWidget()
        self.traininterface.access_train(1).ui.setupUi(self.widget2)
        self.widget2.show()


        


app = QApplication([])
ui = God()
ui.setupConnections()
ui.openSWTrainControllerGUI()
ui.openTrainModelGUI()
ui.traininterface.access_train(1).controller.setCommandedSpeed(12)
print(ui.traininterface.access_train(1).controller.getAutoCommandedSpeed())
# # Start the event loop.
app.exec()

    

    




    