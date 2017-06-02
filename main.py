"""An executable that drives the lottery draw.
"""
import sys
import datetime
from games.game import Game
from generators.random import BasicRandomNumber

class Menu:
    '''Display a menu and respond to choice when run.'''
    def  __init__(self):
        self.game = Game()
        self.choice = {
            "1": self.show_datetime,
            "2": self.play_single_game,
            "3": self.play_sequential_game,
            "4": self.save_data,
            "5": self.quit
        }

    def display_menu(self):
        print("""

Game Menu

1. Show datetime
2. Play Single Game
3. Play Sequential_game
4. Save Data
5. Quit

""")

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choice.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice.".format(choice))

### Building the Menu ###
    def show_datetime(self):
        print("Now is: {}".format(datetime.date.today()) )


    def play_single_game(self):
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def play_sequential_game(self):
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("You note has been added.")

    def save_data(self):
        id = input("Enter a note id: ")
        memo = input("Enter a note: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)        

    def quit(self):
        print("Thank you for playing game today.")
        sys.exit(0) #successful termination

if __name__ == "__main__":
    Menu().run()