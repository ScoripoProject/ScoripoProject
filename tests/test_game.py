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
    assert isinstance(lottery1.number_list, list)
    assert isinstance(lottery1.rand_engine, BasicRandomNumber)
    assert len(lottery1.number_list) == 3 # whatever this container holds.

def test_set_randoms_of_lottory():
    lottery1 = Lottery('#1', 4, 1, 365)
    assert len(lottery1.number_list) == 4
    for i in range(0,4):
        assert not lottery1.number_list[0] == 0 # they should not be 0 if the _set_random() call functional.

def test__set_random_of_lottory():
    lottery1 = Lottery('#1', 3, 1, 365)
    rand = 0
    rand = lottery1._set_random()
    assert not rand == 0
    assert isinstance(rand, int)

def test_get_randoms_of_lottory():
    lottery1 = Lottery('#1', 3, 1, 365)
    nlist = lottery1.get_randoms()
    assert isinstance(nlist, list)
    assert len(nlist) == 3
    for i in range(0,3):
        assert not lottery1.number_list[i] == 0 # they should not be 0 if the _set_random() call functional.
    
def test_sum_of_lottory():
    lottery1 = Lottery('#1', 3, 1, 360)
    assump = 0
    assert (lottery1.number_list, list)
    assert (lottery1.get_randoms(), list)
    assert isinstance(lottery1.sum(), int)
    assert lottery1.sum() > 360 # 3 numbers (a.k.a the sum) is larger than 1 number

def test_reset_of_lottory():
    lottery1 = Lottery('#1', 3, 1, 365)
    assert len(lottery1.number_list) == 3
    lottery1.reset()
    assert len(lottery1.number_list) == 0


def test_to_str_of_lottory():
    lottery1 = Lottery('#2', 3, 1, 365)
    assert lottery1.__str__() == 'Lottery: ##2'

# main()
if __name__ == "__main__":
    print('----A Test of Game----')
    #unittest.main()
