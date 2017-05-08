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
