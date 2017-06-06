##################################################
##           TEST CASE OF GAME                  ##
##################################################
#import unittest
# Use pytest instead of the builtin unittest to perform unittest
#     python3 -m pytest -v tests/test_xxx.py

#from games import game
from games.game import Game #or from ..games.game import Game
from games.game import Lottery
from generators.random import BasicRandomNumber

# for py.test
'Tests for game.py with pytest.'''
# Test of Game
def test_init_of_game():
    game1 = Game()
    assert type(game1) is Game

def test_str_of_game():
    game1 = Game()
    game1.value = "hello"
    assert "hello" == game1.value

# Test of Lottory
def test_init_of_lottory():
    lottery1 = Lottery('#1', 3, 1, 365)
    assert lottery1.__str__() == 'Lottery: ##1'
    assert isinstance(lottery1.rand_engine, BasicRandomNumber)
    assert len(lottery1.number_list) == 3

def test_set_randoms_of_lottory():
    pass
    lottery1 = Lottery('#1', 4, 1, 365)
    isinstance(lottery1.number_list, list)
    assert(len(lottery1.number_list) == 4)

def test__set_random_of_lottory():
    lottery1 = Lottery('#1', 3, 1, 365)
    rand = 0
    rand = lottery1._set_random()
    assert not rand == 0
    assert isinstance(rand, int)

def test_get_randoms_of_lottory():
    pass
    lottery1 = Lottery('#1', 3, 1, 365)
    
def test_sum_of_lottory():
    pass
    lottery1 = Lottery('#1', 3, 1, 365)

def test_reset_of_lottory():
    pass
    lottery1 = Lottery('#1', 3, 1, 365)

def test_to_str_of_lottory():
    lottery1 = Lottery('#2', 3, 1, 365)
    assert lottery1.__str__() == 'Lottery: ##2'

# main()
if __name__ == "__main__":
    print('----A Test of Game----')
    #unittest.main()
    lottery1 = Lottery('#2', 3, 1, 365)
    a = lottery1._set_random()
    print(a)
