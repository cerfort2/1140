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

## Using the CTC module
- #### To dispatch a train, enter an arrival time into the corresponding line edit in (HH:MM:SS) format. Select the destination station, and add as many stops as you would like. Once you are done, click the "Dispatch Train" button, and a train will be dispatched onto the selected line.
- #### To import a schedule file, enter automatic mode by selecting the labeled radio button. Select the Import Schedule Flie button. A file explorer window will open, allowing you to select a .xlsx or .csv file to import a schedule for the trains. This file must have four headers in this order: departure time, arrival time, arrival station, and a list of stops, separated by commas. The stations should be in the following format block_#: station_name (e.g. C9: EDGEBROOK).
- #### To schedule a train, enter an arrival time, departure time, destination station, and input as many stops as you like. Click the "Schedule Train" button, and a train will be added to the schedule for the selected line.
