"""A lucky draw system based on pseudo-random number generator.
"""

import random # Python's built-in random

class RandomNumber:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_random(self):
	    return random.randint(self.start, self.end)