import unittest
from shortest_path.shortest_path import find_shortest_path

class test_find_shortest_path(unittest.TestCase):
    def test_case1(self):
        answer = "The destination is the same as the source!"
        assert(find_shortest_path("graph_dij.txt", "1", "1")==answer)
        
    def test_case2(self):
        answer = (['1', '2'], 4)
        assert(find_shortest_path("graph_dij.txt", "1", "2")==answer)
    
    def test_case3(self):
        answer = (['1', '3', '6', '5', '7'], 3)
        assert(find_shortest_path("graph_dij.txt", "1", "7")==answer)
        
    def test_case4(self):
        answer = "We can not reach to destination from source!"
        assert(find_shortest_path("graph_dij.txt", "4", "1")==answer)   
        

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
