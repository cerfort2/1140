import Software_Track_Controller.Block
from Software_Track_Controller.Block import *
class PLC():
    auth = 0
    def __init__(self, blo:Block = []):
        self.blocks = blo


    def logic(self, name):
        #module_name = file_path.replace('.py', '')
        file = name.lower()
        logic = __import__(file)
        logicrun = getattr(logic, "plc")
        logicrun(self.blocks)

        
    def collision(self, name):
        #module_name = file_path.replace('.py', '')
        file = name.lower()
        logic = __import__(file)
        logicrun = getattr(logic, "plcc")
        return logicrun(self.blocks)
    



