import Block
from Block import *
class Wayside():
    #Class Variables
    name:str = ""
    def __init__(self):
        self.blocks:Block = []
        


    def addBlock(self, sw:bool, cr:bool, si:bool, st:bool, na:str, le:str = "", ri:str = ""):
        create:Block = Block(sw, cr, si, st, na)
        if(sw):
            create.setLeft(le)
            create.setRight(ri)
        self.blocks.append(create)
    
