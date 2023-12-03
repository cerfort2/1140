#Train model interface to house all train objects

from trains_interface.train_model_software import *

class train_model_interface_software(QObject):

    #create signal
    track_model_occupancy_list = pyqtSignal(list)

    #constructor, create list to house trains
    def __init__(self):
        super().__init__()
        self.UI_flag = False
        self.trains = []
    
    #add a new train to the list of trains
    def new_train(self) -> None:
        self.trains.append(train_model_software())

    #access a single train object in the list
    def access_train(self, train_num: int) -> train_model_software:
        return self.trains[train_num - 1]

    #update all trains
    def update_trains(self) -> None:
        for train in self.trains:
            train.update_train(self.UI_flag)

    #get occupancy list
    def get_occupancies(self) -> list[str]:
        out_list = []

        for train in self.trains:
            out_list.append(train.get_occupancy())
        
        self.track_model_occupancy_list.emit(out_list)

    #set slopes from track model
    def set_slopes(self, input_list: list) -> None:
        for i in range(0, len(input_list)):
            self.trains[i].set_slope(input_list[i])

    #set polarities from track model
    def set_polarities(self) -> None:
        for train in self.trains:
            train.update_occupancy()

    def set_route(self, names: list) -> None:
        self.trains[0].routeList = names

    #show GUIs
    def show_GUI(self, train_num: int) -> None:
        self.UI_flag = True
        self.trains[train_num - 1].open_GUI()
        self.trains[train_num - 1].controller.open_GUI()
