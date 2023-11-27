from GreenLineWaysides import GreenLine #Testing the greenline wayside Class
import unittest #For testing

class Testing(unittest.TestCase):

    def test_createTracksTest(self): #Test the creation of tracks from the track model
        testing = GreenLine()
        listCreation = [[0,0,0], [0,0,0], [0,0,0], ["A","B","C"]]
        for i in range(3):
            testing.Waysides[0].createTrack(listCreation[0][i], listCreation[1][i], listCreation[2][i], listCreation[3][i])
        assert(testing.Waysides[0].getTrackName(0) == "A")
    
    def test_occupancy(self): #Test to ensure changing occupancy works
        testing = GreenLine()
        listCreation = [[0,0,0], [0,0,0], [0,0,0], ["A","B","C"]]
        for i in range(3):
            testing.Waysides[0].createTrack(listCreation[0][i], listCreation[1][i], listCreation[2][i], listCreation[3][i])
        testing.Waysides[0].getTrack(0).setOccupancy(True)
        assert(testing.Waysides[0].getTrack(0).getOccupancy() == True)


if __name__ == '__main__':
    unittest.main()