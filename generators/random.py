"""A lucky draw system based on pseudo-random number generator.
"""

import random # Python's built-in random
from abc import ABCMeta, abstractmethod # MetaClass for defining Abstract Base Classes


class RandomNumber(metaclass=ABCMeta):
    '''An abstract base class of random nunber generator.

    This module implements algorithm for generating random number.
    Used to extend to implement different ways that generate random number.

    Attributes:
    * value     an integer representing the value of a random number
    * start      the possible starting number of random number
    * end        the possible ending number of random number

    Class hierarchy:
    |--* RandomNumber
    |
    \----* BasicRandomNumber
    |
    \----* BiasRandomNumber

    '''
    def __init__(self, start, end):
        self.value = 0 # the value of this random number
        self.start = start
        self.end = end

    def __str__(self):
        '''to_str()'''
        return 'Random number: {}'.format(self.value, )

    def set_random(self):
        '''Ask for generating a random number, and set it to self.value'''
        rnd = self.generate_random()
        self.value = rnd

    def get_random(self):
        '''Return a random number without changing the current value'''
        return self.value

    @abstractmethod
    def generate_random(self):
        '''Generate a random number'''
        return random.randint(self.start, self.end)

    def __add__(self, other):
        return self.value + other.value

class BasicRandomNumber(RandomNumber):

    def generate_random(self):
        '''Generate a random number'''
        return random.randint(self.start, self.end)
    
class BiasRandomNumber(RandomNumber):
    '''Generate a random number with bias'''

    def __init__(self, start, end, bias=1.0):
        super().__init__(start, end)
        self.bias = bias

    def generate_random(self):
        '''Generate a random number with bias'''
        return round( (random.random() * 100 * self.bias) % self.end) # TODO: think about what is the different of *100 and *1000?