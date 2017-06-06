##################################################
##           TEST CASE OF RANDOM                ##
##################################################
import unittest
# Use pytest instead of the builtin unittest to perform unittest
#     python3 -m pytest -v tests/test_xxx.py

from generators import random #import generators.random

class RandomTestCase(unittest.TestCase):
    '''Tests for random.py.'''
    def setUp(self):
        self.rn = random.BasicRandomNumber(1,78)
        self.rn.set_random()

    def tearDown(self):
        self = None

    def test_is_BasicRandomNumber_a_Random(self):
        self.assertIsInstance(self.rn, random.BasicRandomNumber )
    
    def test_is_BasicRandomNumber_in_range(self):
        self.assertIn(self.rn.get_random(), range(1,78))

class TestBasicRandomNumber():
    '''Tests for random.py with pytest.'''
    def setup(self):
        self.rn = random.BasicRandomNumber(1, 78)
        self.rn.set_random()
        print('Create a BasicRandomNumber.')
        print(type(self))

    def teardown(self):
        self.rn = None
        print('Delete a BasicRandomNumber.')

    def test_what(self):
        self.rn.set_random()
        assert self.rn.get_random() in range(1, 78)

# for py.test
    '''Tests for random.py with pytest.'''
def test_is_BasicRandomNumber_in_range_too():
    rn = random.BasicRandomNumber(1, 78)
    rn.set_random()
    assert rn.get_random() in range(1, 78)

def test_add__():
    rn1 = random.BasicRandomNumber(1, 78)
    rn2 = random.BasicRandomNumber(1, 78)
    rn1.set_random()
    rn2.set_random()

    a = rn1.get_random()
    b = rn2.get_random()
    assert (rn1 + rn2) == (a+b)


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
    #unittest.main()
