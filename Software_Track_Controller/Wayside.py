import Software_Track_Controller.Block
from Software_Track_Controller.Block import *
class Wayside():
    #Class Variables
    
    def __init__(self, tag:str):
        self.blocks:Block = []
        self.name:str = tag

    def getName(self):
        return self.name
    
    def add(self, blo:Block):
        self.blocks.append(blo)


    def addBlock(self, sw:bool, cr:bool, si:bool, na:str, le:str = "", ri:str = ""):
        create:Block = Block(sw, cr, si, na)
        if(sw):
            create.setLeft(le)
            create.setRight(ri)
        self.blocks.append(create)
    
    def getBlock(self, index:int):
        return self.blocks[index]
