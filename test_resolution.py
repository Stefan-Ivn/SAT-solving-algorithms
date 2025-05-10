# test_resolution.py

import unittest
from resolution import resolution

class TestResolution(unittest.TestCase):
    def test_resolution(self):
        clauses = [frozenset([1, -2]), frozenset([-1, 2]), frozenset([3, -2])]
        self.assertTrue(resolution(clauses))

if __name__ == "__main__":
    unittest.main()
