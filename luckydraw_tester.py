"""Test case of LuckyDraw.
"""

from generators import random #import generators.random


# main()
if __name__ == "__main__":
    rn = random.RandomNumber(1, 78)
    rn.set_random()
    print(rn)
