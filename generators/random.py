"""A lucky draw system based on pseudo-random number generator.
"""

import random # Python's built-in random

class RandomNumber:

    def __init__(self, start, end):
        self.value = 0 # the value of this random number
        self.start = start
        self.end = end

    def __str__(self):
        '''to_str()'''
        return 'Random number: {}'.format(self.value, )

    def set_random(self):
        '''Set a random number to the current value'''
        rnd = self.generate_random()
        self.value = rnd

    def get_random(self):
        '''Return a random number without changing the current value'''
        return self.value

    def generate_random(self):
        '''Generate a random number'''
        return random.randint(self.start, self.end)
    
    # TODO: It's not good to use set_random(), maybe we should change this class to ABC
    def generate_random_with_bias(self, bias=1.0):
        '''Generate a random number with bias'''
        return round( (random.random() * 100 * bias) % self.end) # TODO: think about what is the different of *100 and *1000?

