import HardwareTrainController
from HardwareTrainController import *
import unittest

class HWTrainControllerTest(unittest.TestCase):

    # def setUp(self):
    #     self.hwtrain = HardwareTrainController()
    
    def test_power1(self):#test in manual
        self.hwtrain = HardwareTrainController()
        self.hwtrain.setManualMode(True)
        self.hwtrain.setCommanded_speed(45)
        self.hwtrain.setCurrentSpeed(40)
        self.hwtrain.setKi(20)
        self.hwtrain.setKp(400)

        ek = 45-40
        uk = (.05/2)*ek
        power = (ek * 400 - uk * 20)

        self.hwtrain.calcPower()

        self.assertEqual(self.hwtrain.getPower(),power)
    
    def test_power2(self):#test in auto
        self.hwtrain = HardwareTrainController()
        self.hwtrain.setManualMode(False)
        self.hwtrain.setCTC(20)
        self.hwtrain.setCurrentSpeed(10)
        self.hwtrain.setKi(20)
        self.hwtrain.setKp(400)

        ek = 20-10
        uk = (.05/2)*ek
        power = (ek * 400 - uk * 20)

        self.hwtrain.calcPower()

        self.assertEqual(self.hwtrain.getPower(),power)

    def test_ebrake(self):
        self.hwtrain = HardwareTrainController()
        self.hwtrain.eBrakePressed()
        self.assertTrue(self.hwtrain.getEbrake(),True)





if __name__=='__main__':
    unittest.main()