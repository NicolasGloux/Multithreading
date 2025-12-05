import unittest
import numpy as np
from numpy.testing import assert_allclose
from task import Task

class TestTaskResolution(unittest.TestCase):
    def setUp(self):
        self.size = 5
        self.task = Task(size=self.size)

    def test_ax_equals_b(self):
        self.task.work() 

        x = self.task.x 
        A = self.task.a 
        B_actual = np.dot(A, x) 
        B_desired = self.task.b 

        assert_allclose(B_actual, B_desired, 
                        rtol=1e-07, atol=0)

if __name__ == '__main__':
    unittest.main()
