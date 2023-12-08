# ECE 1140 
# Authors: Chris Erfort, Myles Fernau, Zach Baldwin, Anuj Lele, Victor Chiang, Krishna Patel, Connor Paladino


## Installation guide:


#### Clone the repository with the following command:
```bash
git clone https://github.com/cerfort2/1140
```

#### Open the folder in a code editor such as Visual Studio Code

#### You now must install the necessary libraries to run the program.
#### Run the following commands:

```bash
pip install pyserial
```
```bash
pip install pandas
```
```bash
pip install pyqt6
```
```bash
pip install pyserial
```

### To run the system:
- #### Run SignalClass.py
- #### A User Interface with options to select CTC, Track Controller, Track Model, Train Model, Train Controller will appear
- #### Do not close out of this interface
- #### Select the *Track Model* and click *Upload Track Layout*
- #### After uploading, click the *CTC* module and click the *Dispatch Train* button after entering a time (HH:MM:SS)
- #### Open the Track Model again and the train will appear on the map
- #### You may monitor the speed using the *Train Controller* module

## Installing the Hardware Train Controller

## Installing the Hardware Track Controller
- #### Obtain a Arduino Mega Board, A Serial Communication Cord, DFRobot LCD2004 Screen, A breadboard with a red and light lcd, 2 150+ ohm resistors, and wire connectors
- #### Connect 4 wires to the Arduino one in 29, one in 39, and other 2 for GND and 5V
- #### Connect the GND and 5V accordingly to the breadboard. Then connect wire in 29 to the positive end of the terminal of the RED Light and 39 to postive end of GREEN Light
- #### On the back of DFRobot LCD conect wires to the connections accordingly into Arduino Board for 5V, GND, SCL, SDA
- #### Plug Arduino into PC/Laptop and open Trains.ino and Update Board and COM port being used
- #### Click "Upload Code" button and installation is complete

## Using the CTC module
- #### To dispatch a train, enter an arrival time into the corresponding line edit in (HH:MM:SS) format. Select the destination station, and add as many stops as you would like. Once you are done, click the "Dispatch Train" button, and a train will be dispatched onto the selected line.
- #### To import a schedule file, enter automatic mode by selecting the labeled radio button. Select the Import Schedule Flie button. A file explorer window will open, allowing you to select a .xlsx or .csv file to import a schedule for the trains. This file must have four headers in this order: departure time, arrival time, arrival station, and a list of stops, separated by commas. The stations should be in the following format block_#: station_name (e.g. C9: EDGEBROOK).
- #### To schedule a train, enter an arrival time, departure time, destination station, and input as many stops as you like. Click the "Schedule Train" button, and a train will be added to the schedule for the selected line.
- #### To open or close a track section, first enter maintenance mode by selecting the corresponding radio button. To open or close a track section, select the block in the dropdown or in the block occupancy display and click the "Toggle Track Closure" button.

## Using the Software Train Controller
- #### Change the mode the train by selecting the drop down at the top of the user interface
- #### The emergency brake and service brakes are toggles. This means you must click the service/emergency brake twice for the train to move again
- #### Send an announcement to the Train Model by typing in the announcement box and pressing *Notify*
- #### To change the speed of the train, type or use the up and down arrows to adjust it.
- #### Change the Proportional and Integral gains of the train by typing or using the up and down arrows to adjust it

## Using HW Track Controller
- #### Select "Track Controller" tab in the God Module to access the Track Controller UI
- #### To upload a PLC logic via .ino Arduino file, press "Open PLC File" button on the UI and navigate to the file to launch the .ino file. Once in Arduino IDE you can select "Upload Code" to upload the code to the connected Arduino Board
- #### In Manual mode PLC Logic will still be executed, but selection of Lights, Switches, and Crossroads can be manually changed. Select a certain line you would like to control and select A wayside you would like to select. On wayside selection the current blocks and failures that are occupied are displayed on the right hand side. Selection of each in that certain wayside will be populated where you can select the signal you would like to change and change statuses
- #### In Automatic mode PLC logic will be executed, changing statuses are not allowed. Selection of Light, Wayside, and other statuses are allowed to be viewed by selection on hardware, but not edited
