#Train Model UI Driver Class, utilize other classes for calculation to update the UI of the train given inputs.

from PyQt6 import QtCore, QtGui, QtWidgets
import os, sys

class Train_Model_UI(object):
    

    #constructor class, initialize all vars 
    def __init__(self) -> None:
        self.curr_authoriy = None
        self.curr_velocity = None
        self.curr_people = None
        self.curr_power = None
        self.curr_environment = None
        self.curr_slope = None
        self.curr_elevation = None
        self.curr_acceleration = None
        self.curr_temperature = None
        self.curr_engine_failure = None
        self.curr_brake_failure = None
        self.curr_signal_failure = None
        self.curr_left_door = None
        self.curr_right_door = None
        self.curr_inside_lights = None
        self.curr_outside_lights = None
        self.curr_announcement = None


    #pass in an  array to set current data of the train to inputted values
    def load_train_data(self) -> None:
        pass


    #UI setup function, initializes all of UI
    def ui_setup(self, Dialog) -> None:
        #add var defs
        _translate = QtCore.QCoreApplication.translate

        #initialize the UI
        Dialog.setObjectName("Dialog")
        Dialog.resize(1400, 700)

        #initialize tab widget
        self.tabWidget = QtWidgets.QTabWidget(parent=Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1400, 700))
        self.tabWidget.setObjectName("tabWidget")

        #initialize tabs for tab widget, self.main_page, self.test_bench
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main_page), _translate("Dialog", "Main Page"))
        self.test_bench = QtWidgets.QWidget()
        self.test_bench.setObjectName("test_bench")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.test_bench), _translate("Dialog", "Test Bench"))

        #add labels to main page
        font = QtGui.QFont()
        font.setPointSize(16)

        self.time_label = QtWidgets.QLabel(parent=self.main_page)
        self.time_label.setGeometry(QtCore.QRect(10, 10, 120, 16))
        self.time_label.setFont(font)
        self.time_label.setObjectName("time_label")
        


    #function to deploy the UI
    def deploy_ui(self) -> None:
        if __name__ == "__main__":
            app = QtWidgets.QApplication(sys.argv)
            Dialog = QtWidgets.QDialog()
            ui = Train_Model_UI()
            ui.ui_setup(Dialog)
            Dialog.show()
            sys.exit(app.exec())


new_model = Train_Model_UI()
new_model.deploy_ui()