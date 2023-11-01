#Train model interface to house all train objects

from train_model_software import train_model_software

class train_model_interface_software():

    #constructor, create list to house trains
    def __init__(self):
        self.trains = []
    
    #add a new train to the list of trains
    def new_train(self) -> None:
        self.trains.append(train_model_software())

    #access a single train object in the list
    def access_train(self, train_num: int) -> train_model_software:
        return self.trains[train_num - 1]
