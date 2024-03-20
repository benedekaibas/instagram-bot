import unittest
from code.from_file import SearchFromFile

class TestSearchFromFile(unittest.TestCase):
    def setUp(self):
        self.searcher = SearchFromFile()

    def test_open_file(self):
        lines = self.searcher.open_file()
        self.assertIsInstance(lines, list)  # check that open_file returns a list
        self.assertTrue(all(isinstance(line, str) for line in lines))  # check that all elements 

if __name__ == "__main__":
    unittest.main()