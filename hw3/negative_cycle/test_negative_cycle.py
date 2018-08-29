import unittest
from negative_cycle.negative_cycle import detect_negative_cycle

class test_negative_cycle(unittest.TestCase):
    def test_case1(self):
        answer = ['There is a negative cycle', ['7', '8', '5']]
        assert(detect_negative_cycle("graph1.txt")==answer)
        
    def test_case2(self):
        answer = "There is no negative cycle!"
        assert(detect_negative_cycle("graph2.txt")==answer)
    
    def test_case3(self):
        answer = ['There is a negative cycle', ['2', '1']]
        assert(detect_negative_cycle("graph3.txt")==answer)
        

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
