import unittest
import sys
from CTC import CTC  # Import your CTC class from the module it's in
from PyQt6.QtCore import QDateTime
from PyQt6.QtWidgets import QTreeWidgetItem, QWidget, QFileDialog, QMainWindow, QApplication, QTableWidgetItem, QLabel, QLineEdit, QHeaderView

app = QApplication(sys.argv)

class TestCTC(unittest.TestCase):

    def setUp(self):
        #initializing ctc for testing
        self.ctc = CTC()
        self.ctc.initialize_ctc()

    #testing dispatch_train function
    def test_dispatch_train(self):
        #setting up input data for testing
        #testing use case of dispatching a train to O88: POPLAR with stops at glenbuy and dormont
        #arrival time of 9 am and departure time of 8 am
        destination = "O88: POPLAR"
        stops = ["K65: GLENBURY", "L73: DORMONT"]
        arrival_time = QDateTime.fromString("09:00:00", "HH:mm:ss").time()
        departure_time = QDateTime.fromString("08:00:00", "HH:mm:ss").time()

        #calling method to be tested
        route, authority, speeds = self.ctc.dispatch_train(destination, stops, arrival_time, departure_time, "Green Line")  # You might need to mock inputs or set them as attributes of the CTC instance

        #defining expected values 
        expected_route = (['Z151', 'J62', 'K63', 'K64', 'K65', 'K66', 'K67', 'K68', 'L69', 'L70', 'L71', 'L72', 'L73', 'M74', 'M75', 
'M76', 'N77', 'N78', 'N79', 'N80', 'N81', 'N82', 'N83', 'N84', 'N85', 'O86', 'O87', 'O88', 'P89', 'P90', 'P91', 'P92', 'P93', 'P94', 'P95', 'P96', 'P97', 'Q98', 'Q99', 'Q100', 'N85', 'N84', 'N83', 'N82', 'N81', 'N80', 'N79', 'N78', 'N77', 'R101', 'S102', 'S103', 'S104', 'T105', 'T106', 'T107', 'T108', 'T109', 'U110', 'U111', 'U112', 'U113', 'U114', 'U115', 'U116', 'V117', 'V118', 'V119', 'V120', 'V121', 'W122', 'W123', 'W124', 'W125', 'W126', 'W127', 'W128', 'W129', 'W130', 'W131', 'W132', 'W133', 'W134', 'W135', 'W136', 'W137', 'W138', 'W139', 'W140', 'W141', 'W142', 'W143', 'X144', 'X145', 'X146', 'Y147', 'Y148', 'Y149', 'Z150', 'F28', 'F27', 'F26', 'F25', 'F24', 'F23', 'F22', 'F21', 'E20', 
'E19', 'E18', 'E17', 'D16', 'D15', 'D14', 'D13', 'C12', 'C11', 'C10', 'C9', 'C8', 'C7', 'B6', 'B5', 'B4', 'A3', 'A2', 'A1', 'D13', 'D14', 'D15', 'D16', 'E17', 'E18', 'E19', 'E20', 'F21', 'F22', 'F23', 'F24', 'F25', 'F26', 'F27', 'F28', 'G29', 'G30', 'G31', 'G32', 'H33', 'H34', 'H35', 'I36', 'I37', 'I38', 'I39', 'I40', 'I41', 'I42', 'I43', 'I44', 'I45', 'I46', 'I47', 'I48', 'I49', 'I50', 'I51', 'I52', 'I53', 'I54', 'I55', 'I56', 
'I57', 'J58', 'J59', 'J60', 'J61'], [False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, 
False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, 
False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, 
False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, 
False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False])
        expected_authority = 4
        expected_speeds = [5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 
5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 
5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 
5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078, 5.564369093941078]  
        #asserting expected outcomes
        self.assertEqual(route, expected_route)
        self.assertEqual(authority, expected_authority)
        self.assertEqual(speeds, expected_speeds)
        

if __name__ == '__main__':
    unittest.main()
