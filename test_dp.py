# test_dp.py

import unittest
from dp import dp

class TestDP(unittest.TestCase):
    def test_dp(self):
        clauses = [{1, -2}, {-1, 2}, {3, -2}]
        assignment = {}
        self.assertTrue(dp(clauses, assignment))

if __name__ == "__main__":
    unittest.main()
