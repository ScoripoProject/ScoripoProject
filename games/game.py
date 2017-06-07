"""A lucky draw system based on pseudo-random number generator.
"""

#import generators.random
#from ..generators.random import RandomNumber #PROBLEM:cannot do relative import
from generators.random import RandomNumber, BasicRandomNumber
from abc import ABCMeta, abstractmethod # MetaClass for defining Abstract Base Classes


class Game(metaclass=ABCMeta):
    '''An abstract base class of games.

    This module implements algorithm for playing game.
    Used to extend to implement different ways that play games.

    Remark: 每次取3~5個隨機號碼時，必須是由外界給啟動指令的
	https://en.wikipedia.org/wiki/Information

    Attributes:
    * status             a string representing the status of this game
    * SIZE_OF_LOTTERY    how much lottery (ticket) this game has
    * MIN                the mix value of random number
    * MAX                the max value of random number
    * lottery_numbers    a list contains lottery objects

    Class hierarchy:
    |--* Game
    |
    \----* SingleGame
    |
    \----* SequentialGame

    '''
    def __init__(self):
        self.status = "Initializing"
        self.SIZE_OF_LOTTERY = 49
        self.MIN = 1
        self.MAX = 65535
        self.lottery_numbers = [] # a list of Lottery

    def __str__(self):
        '''to_str()'''
        return 'Game: {}'.format(self.value, )

    def setup(self):
        pass

    def _draw(self, lottery_numbers):
        pass
        
    def _setup_lottery_numbers(size):
        pass
        
    @abstractmethod
    def run(self):
        '''Run the game.
        
        1. Create a list of 49 lottery numbers.
        2. For each lottery number, attach 3 to 5 random numbers.
        3. Sum up that random numbers.
        4. If the (sum % 6) == 1 or 4, remove the lottery number from the list.
        5. For the rest lottery numbers in the list, attach 3 to 5 NEW random numbers.
        6. Repeat step 3~4, until 10~12 lottery numbers remain in the list.
        7.
        '''

class SingleGame(Game):
    '''An class of playing single game.

    This module implements algorithm for playing a single game.

    Attributes:
    * status             a string representing the status of this game
    * SIZE_OF_LOTTERY    how much lottery (ticket) this game has
    * no_of_rand_in_lottery how much random number each lottery has
    * MIN                the mix value of random number
    * MAX                the max value of random number
    * lottery_numbers    a list contains Lottery objects

    '''
    def __init__(self):
        '''Initize the game deck.'''
        # TODO: use super().__init__()
        self.status = "Initializing"
        print('A new Single Game has been created.')
        self.SIZE_OF_LOTTERY = 49
        self.MIN = 1
        self.MAX = 65535
        self.lottery_numbers = [] # a list of Lottery
        self.no_of_rand_in_lottery = 3
        print('An empty list of lottery numbers is prepared.')
        self.status = "Start"

    def setup(self):
        self.jamming = _get_jamming() # jaming from the real world
        self._prepare_game_deck() # prepare the lottery_numbers

    def _draw(self, lottery_numbers):
        pass
        
    def _setup_lottery_numbers(size):
        pass
        
    def _get_jamming():
        '''Get jamming from the real world'''
        pass

    def _prepare_game_deck():
        pass

    def run(self):
        '''Run the game.
        
        1. Create a list of 49 lottery numbers.
        2. For each lottery number, attach 3 to 5 random numbers.
        3. Sum up that random numbers.
        4. If the (sum % 6) == 1 or 4, remove the lottery number from the list.
        5. For the rest lottery numbers in the list, attach 3 to 5 NEW random numbers.
        6. Repeat step 3~4, until 10~12 lottery numbers remain in the list.
        7.
        '''


class Lottery:
    '''Each Lottery holds 3~5 numbers that are generated randomly.'''

    def __init__(self, title, no_of_numbers, rand_start, rand_end):
        self.title = title # the name of lottery itself.
        self.number_list = [] # a list of numbers that is random, size from 3~5
        self.rand_engine = BasicRandomNumber(rand_start, rand_end)

        self.set_randoms(no_of_numbers)

    def __str__(self):
        return 'Lottery: #{}'.format(self.title)

    def set_randoms(self, no_of_numbers):
        '''Generate a list of numbers.

        New random numbers will be appended to the end of the list.
        Therefore, self.reset() should be called to empty the list in each round.        
        '''
        for i in range(no_of_numbers):
            self.number_list.append(self._set_random())
        #self.number_list = [self._set_random() for i in range(no_of_numbers)]
        
    def _set_random(self):
        '''Generate a random number.'''
        self.rand_engine.set_random()  # Set a random number to a randomnumber.value
        return self.rand_engine.get_random() # then get the value of randomnumber.value

    def get_randoms(self):
        '''Return a list of object of RandomNumber.'''
        return self.number_list

    def sum(self):
        '''Sum up the value in number_list.'''
        #numbers = [self.number_list[i].get_random() for i in self.number_list]
        return sum(self.number_list)

    def reset(self):
        '''Reset lottery to empty.

         Be called each time a Lottery draws a set of new random numbers.
         '''
        del self.number_list[:]
