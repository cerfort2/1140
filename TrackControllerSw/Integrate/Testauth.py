#Test auth
import Block
from Block import *
import Authority
from Authority import *

if __name__ == "__main__":
    blocks:Block = []
    for i in range(10):
        blocks.append(Block(False,False,False,"A" + str(i + 1)))
    auth:Authority = Authority(blocks)
    rou = [["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10"],[False,False,False,False,True,False,False,False,False,True]]
    auth.newRoute(rou)
    blocks[0].setOccupancy(True)
    print(auth.calculate(0))
    print(auth.calculate(0))
    blocks[0].setOccupancy(False)
    blocks[1].setOccupancy(True)
    print(auth.calculate(0))
    print(auth.calculate(0))
    blocks[1].setOccupancy(False)
    blocks[2].setOccupancy(True)
    print(auth.calculate(0))
    print(auth.calculate(0))
    blocks[2].setOccupancy(False)
    blocks[3].setOccupancy(True)
    print(auth.calculate(0))
    print(auth.calculate(0))
    blocks[3].setOccupancy(False)
    blocks[4].setOccupancy(True)
    print(auth.calculate(0))
    print(auth.calculate(0))
    print(auth.calculate(0))
    blocks[4].setOccupancy(False)
    blocks[5].setOccupancy(True)
    print(auth.calculate(0))
    print(auth.calculate(0))
    blocks[5].setOccupancy(False)
    blocks[6].setOccupancy(True)
    print(auth.calculate(0))
    print(auth.calculate(0))
    blocks[6].setOccupancy(False)
    blocks[7].setOccupancy(True)
    print(auth.calculate(0))
    print(auth.calculate(0))
    blocks[7].setOccupancy(False)
    blocks[8].setOccupancy(True)
    print(auth.calculate(0))
    print(auth.calculate(0))
    blocks[8].setOccupancy(False)
    blocks[9].setOccupancy(True)
    print(auth.calculate(0))
    print(auth.calculate(0))