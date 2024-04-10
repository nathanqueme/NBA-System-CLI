from Team import Team
from Game import Game
from Record import Record
from Utils import Utils

class Season:
    def __init__(
        self,
        schedule: list[Game],
        curr_team_list: list[Team],
        round_number: int,
        records: list[Record]
    ):
        self.schedule = schedule
        self.curr_team_list = curr_team_list
        self.round_number = round_number
        self.records = records

    def run(self):
        option = ''
        while option.lower() != 'r':
            option = self.handle_option()
            
    def handle_option(self):
        choice = self.read_choice()
        if choice == "1":
            self.add_team_to_round()
        elif choice == "2":
            self.display_round()
        elif choice == "3":
            self.play_games()
        elif choice == "4":
            self.display_game_result_records()
        return choice
    
    def read_choice(self):
        print(
            "Welcome to the season page! Please make a selection from the menu:\n"
            "1. Add a team to the round.\n"
            "2. Display the current round.\n"
            "3. Play games.\n"
            "4. Display the game result records.\n"
            "R. Return to previous menu."
        )
        return input("Enter a choice: ")
    
    def add_team_to_round(self):
        pass
    
    def display_round(self):
        pass
    
    def play_games(self):
        pass
    
    def display_game_result_records(self):
        pass
    