from train_model_software import *

import unittest

class train_model_test(unittest.TestCase):

        def setUp(self) -> None:
            self.train = train_model_software()
        
        def test_right_door(self) -> None:
            self.train.set_right_door(True)
            self.assertTrue(self.train.get_right_door())

        def test_left_door(self) -> None:
            self.train.set_left_door(True)
            self.assertTrue(self.train.get_left_door())
        
        def test_acceleration(self) -> None:
            self.train.set_power()
            self.train.set_mass(10000)
            caclulated_acceleration = math.sqrt(self.train.get_power() / (2 * self.train.get_mass() * 0.5))
            self.train.calculate_acceleration(self.train.get_power(), self.train.get_mass(), 0.5)
            self.assertEqual(caclulated_acceleration, self.train.get_acceleration())


if __name__ == '__main__':
     unittest.main()