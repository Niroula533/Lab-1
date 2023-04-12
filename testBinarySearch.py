import unittest
from binarySearch import binarySearch
import time
import matplotlib.pyplot as plt


class TestbinarySearch(unittest.TestCase):

    def test_binarySearch(self):
        testArray1 = [1,3,7,11,20,56,61,527]
        self.assertEqual(binarySearch(testArray1, 1, 0, len(testArray1)-1),True)
        self.assertEqual(binarySearch(testArray1, 11, 0, len(testArray1)-1),True)
        self.assertEqual(binarySearch(testArray1, 527, 0, len(testArray1)-1),True)
        self.assertEqual(binarySearch(testArray1, 0, 0, len(testArray1)-1),False)

    def benchmark_binarySearch(self):
        xpoints =[]
        ypoints = []

        for i in range(1,100):    
            testArray = list(range(1,i)) 
            key = i  # key is the not present in array
            initTime = time.time_ns()
            binarySearch(testArray, key, 0, i-2)
            finalTime = time.time_ns()
            ypoints.append((finalTime - initTime)) 
            xpoints.append(i)

        # to plot
        plt.xlabel("size of array")
        plt.ylabel("time in nanoseconds") 
        plt.title("Binary Search")
        plt.plot(xpoints, ypoints)
        plt.show()
        

if __name__ == '__main__':
    unittest.main(exit = False)
    testInstance = TestbinarySearch()
    testInstance.benchmark_binarySearch()

    