import unittest
from linearSearch import linearSearch as LS
import time
import matplotlib.pyplot as plt


class TestLinearSearch(unittest.TestCase):

    def test_linearSearch(self):
        testArray1 = [1,3,54,20,11,7]
        self.assertEqual(LS(testArray1, 1),True)
        self.assertEqual(LS(testArray1, 7),True)
        self.assertEqual(LS(testArray1, 20),True)
        self.assertEqual(LS(testArray1, 0),False)

    def benchmark_linearSearch(self):
        xpoints =[]
        ypoints = []

        for i in range(100000,2000000,25000):    
            testArray = list(range(1,i)) 
            key = i  # key is the no present in array
            initTime = time.time_ns()
            LS(testArray, key)
            finalTime = time.time_ns()
            ypoints.append((finalTime - initTime)/1000000) 
            xpoints.append(i)

        # to plot
        plt.xlabel("size of array")
        plt.ylabel("time in millisseconds") 
        plt.title("Linear Search")
        plt.scatter(xpoints, ypoints)
        plt.show()
        

if __name__ == '__main__':
    unittest.main(exit = False)
    testInstance = TestLinearSearch()
    testInstance.benchmark_linearSearch()
