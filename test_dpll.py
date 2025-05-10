# test_dpll.py

import unittest
from dpll import dpll

class TestDPLL(unittest.TestCase):
    def test_dpll(self):
        clauses = [{1, -2}, {-1, 2}, {3, -2}]
        assignment = {}
        self.assertTrue(dpll(clauses, assignment))

if __name__ == "__main__":
    unittest.main()
