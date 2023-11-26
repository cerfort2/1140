import Track   # The code to test
from Track import *

import unittest   # The test framework

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_occupancy(self):
        testing = Track()
        listx = [[0,0],[0,0],[0,0],["A","B"]]
        testing.create(listx)
        assert (testing.getOccupancy() == [0,0])

    def occupancy2(self):
        testing = Track()
        listx = [[0,0],[0,0],[0,0],["A","B"]]
        testing.create(listx)
        testing.setOccupancy([1,1])
        assert (testing.getOccupancy() != [0,0])

if __name__ == '__main__':
    unittest.main()