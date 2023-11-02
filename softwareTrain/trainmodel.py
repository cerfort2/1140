from SoftwareTrainController import SoftwareTrainController
import math, time

class train_model_software():

    #new train constructor
    def __init__(self) -> None:

        #set local vars to test vals
        self.authority = 100.0
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
        self.mass = 45842.3
        self.announcement = "Test Announcementf"

        #create instance of train controller
        self.controller = SoftwareTrainController()
    

    #
    #GETTERS AND SETTERS
    #

    #recieve power from train controller, update power in model
    def set_power(self) -> None:
        self.power = self.controller.getPower()

    #power getter
    def get_power(self) -> float:
        return self.power

    #set speed for both controller and model
    #uses the calculate_speed function
    def set_speed(self) -> None:
        self.controller.setCurrentSpeed(self.calculate_speed(self.speed, self.acceleration, 0.5))
        self.speed = self.calculate_speed(self.speed, self.acceleration, 0.5)
    
    #speed getter
    def get_speed(self) -> float:
        return self.speed

    #authority setter
    def set_authority(self) -> None:
        self.authority -= self.calculate_travel(self.speed, 0.5)
        self.controller.setAuthority(self.authority)
        
    #authority getter
    def get_authority(self) -> None:
        return self.authority

    #
    #CALCULATORS
    #

    #calculate a new speed across a certain time interval
    def calculate_speed(self, prev_speed: float, prev_acceleration : float, delta_time: float) -> float:
        calced = prev_speed + ((delta_time / 2) * (prev_acceleration + self.calculate_acceleration(self.power, self.mass, delta_time)))
        return calced if calced > 0 else 0

    #calculate the acceleration across a certain time period
    #THIS DOES NOT YET ACCOUNT FOR GRAVITY
    def calculate_acceleration(self, power: float, mass: float, delta_time: float) -> float:
        if power >= 0:
            self.acceleration = math.sqrt(power / (2 * mass * delta_time))
            return self.acceleration - 1.2 * (self.controller.getServiceBrake() / 100)
        return 0 - 1.2 * (self.controller.getServiceBrake() / 100)
        
    #calculates time traveled over a time period
    def calculate_travel(self, speed: float, delta_time: float) -> float:
        return speed * delta_time

    
    #updates all train values
    def update_train(self) -> None:
        self.set_power()
        self.set_speed()
        self.set_authority()


#new_train = train_model_software()
#while(1):
# new_train.update_train()
# time.sleep(0.5)