from SoftwareTrainControllerGUI import 

class train_model_software():

    #new train constructor
    def __init__(self) -> None:
        self.authority = 1000.0
        self.speed = 0.0
        self.passengers = 0
        self.power = 0.0
        self.environment = "Tunnel"
        self.slope = 13
        self.elevation = 407
        self.acceleration = 0.0
        self.temperature = 71
        self.engine_failure = False
        self.brake_failure = False
        self.signal_failure = False
        self.inside_lights = True
        self.outside_lights = True
        self.right_door = False
        self.left_door = False
        self.announcement = "Test Announcementf"
    
    #recieve power from train controller, update power in model
    def set_power(self) -> None:
        self.power = 
