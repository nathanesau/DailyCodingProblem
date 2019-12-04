import unittest

import problem61
import problem62
import problem63

class TestProblem61(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(problem61.solve(), True)

class TestProblem62(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(problem62.solve(), True)

class TestProblem63(unittest.TestCase):    
    def test_word_in_matrix(self):
        mat = [['F', 'A', 'C', 'I'], ['O', 'B', 'Q', 'P'], ['A', 'N', 'O', 'B'], ['M', 'A', 'S', 'S']]
        self.assertEqual(problem63.word_in_matrix(mat, 'MASS'), True)
        self.assertEqual(problem63.word_in_matrix(mat, 'FOAM'), True)
        self.assertEqual(problem63.word_in_matrix(mat, 'SPONGE'), False)
        self.assertEqual(problem63.word_in_matrix(mat, 'SPOT'), False)

if __name__ == "__main__":
    unittest.main()