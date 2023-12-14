#Train Model object class, all objects are created in the train model interface
import math, time
from trains_interface.SoftwareTrainController import *
from Hardware_Train_Controller.HardwareTrainController import *
from trains_interface.train_model_GUI import *

class train_model_software():

    #new train constructor
    def __init__(self) -> None:

        #set local vars to test vals
        self.authority = 0.0
        self.speed = 0.0
        self.passengers = 0
        self.power = 0.0
        self.environment = ""
        self.slope = 0.0
        self.elevation = 0.0
        self.acceleration = 0.0
        self.temperature = 71
        self.engine_failure = False
        self.brake_failure = False
        self.signal_failure = False
        self.inside_lights = True
        self.outside_lights = False
        self.right_door = False
        self.left_door = False
        self.mass = 45842.3
        self.announcement = ""
        self.beacon_list = []
        self.current_polarity = True
        self.occupancy = ""
        self.underground_list = []
        self.underground_val = False
        self.speed_list = []
        self.speed_limit = 0
        self.open_side = "Right"
        self.current_station = ""
        self.suggested_speed_list =[]
        self.routeList = []
        self.stationAuthorities = []
        self.authority_list = []
        self.station_bools = []
        self.currentMove = 0
        self.train_number = 0
        #create instance of train controller
        self.controller = SoftwareTrainController()
        # self.controller = HardwareTrainController()

        #create ui item
        self.ui = train_model_GUI()
    


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
        self.controller.setCurrentSpeed(self.calculate_speed(self.speed, self.acceleration, 1))
        self.speed = self.calculate_speed(self.speed, self.acceleration, 1)

    #speed getter
    def get_speed(self) -> float:
        return self.speed

    #authority setter
    def set_authority(self) -> None:
        travel = self.calculate_travel(self.speed, 1)
        self.authority -= travel
        self.currentMove += travel
        self.update_occupancy()
        if self.authority < 0:
            self.authority = 0
        self.controller.authority=self.authority
        
    #get new authority value
    def new_authoriy(self, input: int) -> None:
        self.authority = float(input)
    
    #authority getter
    def get_authority(self) -> None:
        return self.authority

    #passenger setter
    def set_passengers(self, count: int) -> None:
        self.passengers = count

    #passenger getter
    def get_passengers(self) -> int:
        return self.passengers
    
    #environment setter
    def set_environment(self, type: str) -> None:
        self.environment = type

    #environment getter
    def get_environment(self) -> str:
        return self.environment
    
    #slope setter
    def set_slope(self, degree: float) -> None:
        self.slope = degree

    #slope getter
    def get_slope(self) -> float:
        return self.slope
    
    #elevation setter
    def set_elevation(self, count: float) -> None:
        self.elevation = count

    #elevation getter
    def get_elevation(self) -> float:
        return self.elevation
    
    #acceleration setter
    def set_acceleration(self, count: float) -> None:
        self.acceleration = count

    #acceleration getter
    def get_acceleration(self) -> float:
        return self.acceleration

    #temperature setter
    def set_temperature(self, temp: int) -> None:
        self.temperature = temp

    #temperature getter
    def get_temperature(self) -> int:
        return self.temperature

    #engine failure setter
    def set_engine_failure(self, fail: bool) -> None:
        self.engine_failure = fail

    #engine failure getter
    def get_engine_failure(self) -> bool:
        return self.engine_failure

    #brake failure setter
    def set_brake_failure(self, fail: bool) -> None:
        self.brake_failure = fail

    #brake failure getter
    def get_brake_failure(self) -> bool:
        return self.brake_failure
    
    #signal failure setter
    def set_signal_failure(self, fail: bool) -> None:
        self.signal_failure = fail

    #signal failure getter
    def get_signal_failure(self) -> bool:
        return self.signal_failure
    
    #inside lights setter
    def set_inside_lights(self, light: bool) -> None:
        self.inside_lights = light

    #inside lights getter
    def get_inside_lights(self) -> bool:
        return self.inside_lights
    
    #outside lights setter
    def set_outside_lights(self, light: bool) -> None:
        self.outside_lights = light

    #outside lights getter
    def get_outside_lights(self) -> bool:
        return self.outside_lights
    
    #right doorsetter
    def set_right_door(self, door: bool) -> None:
        self.right_door = door

    #right door getter
    def get_right_door(self) -> bool:
        return self.right_door
    
    #left doorsetter
    def set_left_door(self, door: bool) -> None:
        self.left_door = door

    #left door getter
    def get_left_door(self) -> bool:
        return self.left_door
    
    #mass setter
    def set_mass(self, mass: float) -> None:
        self.mass = mass

    #mass getter
    def get_mass(self) -> float:
        return self.mass
    
    #announcement setter
    def set_announcement(self, announcement: str) -> None:
        self.announcement = announcement

    #announcement getter
    def get_announcement(self) -> str:
        return self.announcement

    #occupancy setter
    def set_occupancy(self, occupancy: str) -> None:
        self.occupancy = occupancy
    
    #occupancy getter
    def get_occupancy(self) -> str:
        return self.occupancy

    #suggested speed getter
    def get_suggested_speed(self) -> int:
        return self.suggested_speed_list[0]


    #
    #CALCULATORS
    #

    #calculate a new speed across a certain time interval
    def calculate_speed(self, prev_speed: float, prev_acceleration : float, delta_time: float) -> float:
        calculated = prev_speed + ((delta_time / 2) * (prev_acceleration + self.calculate_acceleration(self.power, self.mass, delta_time)))
        return calculated if calculated > 0 else 0

    #calculate the acceleration across a certain time period
    #THIS DOES NOT YET ACCOUNT FOR GRAVITY
    def calculate_acceleration(self, power: float, mass: float, delta_time: float) -> float:
        self.acceleration = math.sqrt(power / (2 * mass * delta_time))
        if self.controller.serviceBrake or self.controller.eBrake:
            return self.acceleration - 1.2 * self.controller.serviceBrake - 2.3 * int(self.controller.eBrake) - (9.81 * math.sin(math.radians(self.slope)))
        else:
            return self.acceleration - (9.81 * math.sin(math.radians(self.slope)))
    
    #calculates time traveled over a time period
    def calculate_travel(self, speed: float, delta_time: float) -> float:
        return speed * delta_time
    

    #
    #CALCULATING BEACONS AND OCCUPANCY
    #

    # #beacon getter for beacon strings
    # def set_beacon_list_out_station(self, beacon_val: str) -> None:

    #     self.beacon_list = []
    #     self.authority = 0
    #     self.underground_list = []
    #     self.speed_list = []
    #     iterator = 0

    #     temp = ""

    #     for i in range(0, len(beacon_val)):

    #         if beacon_val[i] == " ":
    #             continue
    #         elif beacon_val[i] != "/" and beacon_val[i] != ";":
    #             temp += beacon_val[i]
    #         else:
    #             if iterator == 0:
    #                 self.beacon_list.append(temp)
    #                 temp = ""
    #                 iterator += 1
    #             elif iterator == 1:
    #                 #self.authority += float(temp)
    #                 temp = ""
    #                 iterator += 1
    #             elif iterator == 2:
    #                 self.underground_list.append(bool(temp))
    #                 temp = ""
    #                 iterator += 1
    #             else:
    #                 self.speed_list.append(temp)
    #                 temp = ""
    #                 iterator = 0
        
    #     #self.occupancy = self.beacon_list[0]

    # #get suggest speed list from CTC
    # def set_suggested_speeds(self, speed_list: list) -> None:
    #     self.suggested_speed_list = speed_list
        
    # #setting station data
    def set_station_data(self, beacon_val: str) -> None:
        if self.signal_failure:
            return
        #Split by ;
        splitPackets = beacon_val.split("; ")

        #Split first packet by /
        firstPacket = splitPackets[0].split("/")

        #Station Name
        self.current_station = firstPacket[0]
        self.announcement = "Arriving at: " + self.current_station

        #Station Side
        if(len(firstPacket) == 3):
            self.right_door = True
            self.left_door = True
        else:
            if firstPacket[1] == 'Right':
                self.right_door = True
            else:
                self.left_door = True


    # #switch beacon
    # def set_switch_data(self, beacon_val: str) -> None:

    #     blockList = beacon_val.split("; ")
    #     blockList = blockList[:len(blockList) - 1]

    #     for block in blockList:
    #         infoList = block.split("/")
    #         self.beacon_list.append(infoList[0])
    #         self.authority += float(infoList[1])
    #         self.authority_list.append(infoList[1])
    #         self.underground_list.append(infoList[2])
    #         self.speed_list.append(infoList[3])

    #     #self.occupancy = self.beacon_list[0]
    #     self.currentMove = 0
    
    #occupancy updater
    def update_occupancy(self) -> None:

        if self.authority == 0 and len(self.stationAuthorities) > 1:
            self.stationAuthorities = self.stationAuthorities[1:]
            self.authority = self.stationAuthorities[0]
            self.controller.dwelling = True
            self.controller.dwellTime = 60

        #if self.authority == 0:
           # 1 == 1

        if (self.occupancy == "Z151" and self.routeList == ["Z151"]) or (self.occupancy == "T77" and self.routeList == ["T77"]):
            self.widget2.close()
            self.controller.widget2.close()

        if self.currentMove > float(self.authority_list[0]):

            self.current_polarity = not self.current_polarity
            self.currentMove -= float(self.authority_list[0])
            
            if len(self.authority_list) > 1:
                self.authority_list = self.authority_list[1:]

            if len(self.routeList) > 1:
                self.routeList = self.routeList[1:]
                self.occupancy = self.routeList[0]
                
            if len(self.suggested_speed_list) > 1:
                self.suggested_speed_list = self.suggested_speed_list[1:]
            
    def unpack_route(self, monsters_data) -> None:
        print("monsters full data")
        self.suggested_speed_list = monsters_data[1]
        self.stationAuthorities = monsters_data[2]
        self.routeList = monsters_data[0][0]
        self.station_bools = monsters_data[0][1]
        self.authority_list = monsters_data[0][2]

        self.authority = self.stationAuthorities[0]
        



    #function to open train GUI on current train
    def open_GUI(self) -> None:
        self.widget2 = QWidget()
        self.ui.setupUi(self.widget2)
        self.widget2.show()

    #
    #OVERALL TRAIN UPDATE FUNCTION
    #

    #updates all train values and recieve inputs from the controller
    def update_train(self, UI_flag: bool) -> None:
        if UI_flag:
            self.scrape_ui()
        self.set_power()
        self.set_speed()
        self.set_authority()
        self.set_temperature(self.controller.temperature)
        self.set_engine_failure(self.controller.engineFailure)
        self.set_brake_failure(self.controller.brakeFailure)
        self.set_signal_failure(self.controller.signalFailure)
        self.set_inside_lights(self.controller.getIntLights())
        self.set_outside_lights(self.controller.getExteriorLights())
        self.set_right_door(self.controller.getRightDoor())
        self.set_left_door(self.controller.getLeftDoor())
        self.set_announcement(self.controller.getAnnouncement())
        self.controller.nextstop = self.current_station
        if self.controller.dwelling == True:
            self.controller.leftDoor = self.left_door
            self.controller.rightDoor = self.right_door
        
        self.controller.setCommandedSpeed(self.get_suggested_speed())
        if UI_flag:
            self.controller.update_time()
        if UI_flag:
            self.update_ui()

        self.adTimer += 1
        if self.adTimer == 10 and self.adNum == 1:
            self.ui.ad.setPixmap(self.ui.ad2)
            self.adNum = 2
            self.adTimer = 0
        elif self.adTimer == 10 and self.adNum == 2:
            self.ui.ad.setPixmap(self.ui.ad3)
            self.adNum = 3
            self.adTimer = 0
        elif self.adTimer == 10 and self.adNum == 3:
            self.ui.ad.setPixmap(self.ui.ad1)
            self.adNum = 1
            self.adTimer = 0

    #update train ui
    def update_ui(self) -> None:
        self.ui.slope.setText(str(self.slope) + " Degrees")
        self.ui.elevation.setText(str(round(self.elevation, 2)) + " Feet")
        if self.underground_val == True:
            self.ui.environment.setText("In a Tunnel")
        else:
            self.ui.environment.setText("Outside")
        self.ui.passenger_count.setText(str(round(self.passengers, 2)) + " People")
        self.ui.power.setText(str(round(self.power, 2)) + " Watts")
        self.ui.current_velocity.setText(str(round(self.speed * 2.23694, 2)) + " MPH")
        self.ui.authority.setText(str(round(self.authority * 3.28084, 2)) + " Feet")
        self.ui.acceleration.setText(str(round(self.acceleration * 3.280839895013123, 2)) + "Ft/s^2")
        self.ui.air_conditioning.setText("71 Degrees")

        self.ui.inside_lights.setChecked(self.inside_lights)
        self.ui.outside_lights.setChecked(self.outside_lights)
        self.ui.left_door.setChecked(self.left_door)
        self.ui.right_door.setChecked(self.right_door)

        self.ui.engine_failure.setChecked(self.engine_failure)
        self.ui.brake_failure.setChecked(self.brake_failure)
        self.ui.signal_failure.setChecked(self.signal_failure)

        self.ui.train_number_value.setText(str(self.train_number))
        self.ui.crew_count.setText("2 People")
        self.ui.mass.setText(str(round(self.mass / 2.2, 2)) + " lbs")

        self.ui.length.setText(str(round(32.2 * 3.28084, 2)) + " feet")
        self.ui.length.setText(str(round(3.42 * 3.28084, 2)) + " feet")
        self.ui.length.setText(str(round(2.65 * 3.28084, 2)) + " feet")

        self.ui.announcement.setText(self.announcement)
    
    #get values from ui
    def scrape_ui(self) -> None:
        self.ui.emergency_brake.clicked.connect(self.controller.eBrakePressed)

        if self.ui.engine_failure.isChecked():
            self.controller.engineFailure = True
        else:
            self.controller.engineFailure = False
        if self.ui.brake_failure.isChecked():
            self.controller.brakeFailure = True
        else:
            self.controller.brakeFailure = False
        if self.ui.signal_failure.isChecked():
            self.controller.signalFailure = True
        else:
            self.controller.signalFailure = False

