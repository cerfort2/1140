# ECE 1140 
# Authors: Chris Erfort, Myles Fernau, Zach Baldwin, Anuj Lele, Victor Chiang, Krishna Patel, Connor Paladino


## Installation guide:

#### This installation guide assumes you are using a vanilla ubuntu virtual machine.

#### If you do not have the github CLI, you must install it with the following command:
```bash
apt install git -y
```


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

