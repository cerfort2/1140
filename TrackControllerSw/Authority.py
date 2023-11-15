import Block
from Block import *
from PyQt6 import QtCore
from PyQt6.QtCore import pyqtSignal
class Authority():
    def __init__(self, travel, blo, first):
        self.route = travel
        self.blocks = blo
        trackModelAuthority.emit(first)

    
    def getRoute(self):
        #return route
        trackModelRoute.emit(route)

    def calculate(self):
        for i in range(len(self.blocks)):
            if(self.blocks[i].getOccupancy()):
                if(self.route[0][0] == self.blocks[i].getName()):
                    stop = self.route[1][0]
                    auth = 0
                    while(not stop):
                        auth = auth + 1
                        stop = self.route[1][auth]
                    self.route[0].pop(0)
                    self.route[1].pop(0)
                    #return auth
                    trackModelAuthority.emit(auth)
        #return null
        trackModelAuthority.emit()
                        


    