"""Test case of LuckyDraw.
"""

from generators import random #import generators.random


# main()
if __name__ == "__main__":
    print('----A Random Number----')
    rn = random.RandomNumber(1, 78)
    rn.set_random()
    print(rn)

    print('----A Random Number with Bias----')
    rn_bias = random.RandomNumber(1, 78)
    print(rn_bias)
    print(rn_bias.generate_random_with_bias(0.57))