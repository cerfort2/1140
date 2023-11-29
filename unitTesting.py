from trackmodelguitest import Line, Block, TrackModel
import unittest

class Testing(unittest.TestCase):

    def test_(self):
        switch = []
        crossroad = []
        signal = []
        testTrack = TrackModel()
        testTrack.addLine("GreenLine.csv")

        for i in range(len(testTrack.getLine("Green Line").blocks)):
            switch.append(False)

            if(i == 18):
                crossroad.append(False)
            else:
                crossroad.append(True)

            signal.append(False)

        testTrack.controlModel([switch,crossroad,signal])
        assert(testTrack.getLine("Green Line").blocks[18].crossroad[1] == False)


if __name__ == "__main__":
    unittest.main()


            


