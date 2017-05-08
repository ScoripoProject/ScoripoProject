"""A lucky draw system based on pseudo-random number generator.
"""

import random # Python's built-in random

class RandomNumber:
    value = 0 # the value of this random number

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
    	'''to_str()'''
        return 'Random number: {}'.format(self.value, )

    def set_random(self):
	    self.value = random.randint(self.start, self.end)

    def get_random(self):
        self.set_random()
        return self.value