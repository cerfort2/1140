import Software_Track_Controller.Block
from Software_Track_Controller.Block import *
class Wayside():
    #Class Variables
    
    def __init__(self, tag:str):
        self.blocks:Block = []
        self.name:str = tag

    #Returns wayside name
    def getName(self):
        return self.name
    
    #Adds block to wayside
    def add(self, blo:Block):
        self.blocks.append(blo)
    
    #Returns block at given index 
    def getBlock(self, index:int):
        return self.blocks[index]

    #Returns list of blocks in wayside
    def getBlocks(self):
        return self.blocks
