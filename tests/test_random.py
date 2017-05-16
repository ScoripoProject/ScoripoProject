##################################################
##           TEST CASE OF RANDOM                ##
##################################################
import unittest
from generators import random #import generators.random

class RandomTestCase(unittest.TestCase):
    '''Tests for random.py.'''
    def setUp(self):
        self.rn = random.BasicRandomNumber(1,78)
        self.rn.set_random()

    def tearDown(self):
        self = None

    def test_is_BasicRandomNumber_a_Random(self):
        self.assertIn(self.rn.get_random(), range(1, 78) )
    
    def test_is_BasicRandomNumber_in_range(self):
        self.assertIn(self.rn.get_random(), range(1,78))


# main()
if __name__ == "__main__":
    print('----A Random Number----')
    rn = random.BasicRandomNumber(1, 78)
    rn.set_random()
    print(rn)

    print('----A Random Number with Bias----')
    rn_bias = random.BiasRandomNumber(1, 78, 0.57)
    rn_bias.set_random()
    print(rn_bias)
    #help(random.BiasRandomNumber)
    unittest.main()
