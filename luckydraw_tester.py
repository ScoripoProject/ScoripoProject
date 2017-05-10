"""Test case of LuckyDraw.
"""

from generators import random #import generators.random


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