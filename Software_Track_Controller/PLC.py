import Software_Track_Controller.Block
from Software_Track_Controller.Block import *
class PLC():
    def __init__(self, blo:Block = []):
        self.blocks = blo

    #Calls the plc file of the current track
    def logic(self, name):
        file = name.lower()
        logic = __import__(file)
        logicrun = getattr(logic, "plc")
        logicrun(self.blocks)

    #Calls the plc collision logic of the current track    
    def collision(self, name):
        file = name.lower()
        logic = __import__(file)
        logicrun = getattr(logic, "plcc")
        return logicrun(self.blocks)
    



