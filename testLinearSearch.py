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

    
# def run_linear_search(n):
#     data = sample(range(1, n+1), n)

#     start_time = time_ns()
#     linear_search(data, data[-1])
#     end_time = time_ns()

#     time_taken = end_time-start_time
#     print(time_taken)
#     return time_taken




# def plot_linear():
#     x_values = []
#     y_values = []
#     for i in range(10000, 100000, 10000):
#         x_values.append(i)
#         y_values.append(run_linear_search(i))

#     plt.plot(x_values, y_values)
#     plt.title("Linear Search")
#     plt.xlabel("Number of Data ( n )")
#     plt.ylabel("Time taken  ( t )")
#     plt.show()