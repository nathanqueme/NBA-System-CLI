from Team import Team
from Game import Game
from Record import Record
from Utils import Utils

class Season:
    def __init__(self):
        self.schedule: list[Game] = []
        self.curr_team_list: list[Team] = []
        self.round_number: int = 1
        self.records: list[Record] = []

    def run(self):
        option = ''
        while option != 'R':
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
        elif choice != "R":
            print("Please enter a number between 1 and 4 or press R to return to the previous menu.")
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
        while len(self.curr_team_list) > 0:
            while True: 
                available_teams = [team.name for team in self.curr_team_list]
                print("The existing teams are as follows: \n" + " ".join(available_teams))
                team_name = input("Please enter the team's name that you want to schedule: \n").strip()

                # Search
                matching_team: Team | None = None

                for team in self.curr_team_list:
                    if team.name == team_name:
                        matching_team = team
                        break
                    
                if matching_team is None:
                    print("No such team! Please try again")
                else:
                    break
                
            if len(self.schedule) == 0 or self.schedule[-1].is_full():
                self.schedule.append(Game(term=len(self.schedule) + 1))

            self.schedule[-1].add_team(matching_team)
            self.curr_team_list.pop(self.curr_team_list.index(matching_team))
            print(f"Team {team_name} has been added at the Game {len(self.schedule)} position {len(self.schedule[-1].teams)}")
           
    def display_round(self):
        Utils.GameHeader()
        for game in self.schedule:
            first = game.teams[0].name if len(game.teams) > 0 else "N/A"
            second = game.teams[1].name if len(game.teams) > 1 else "N/A"
            print(Utils.GamesFormat(first, " vs", second))
        Utils.GameEnd()
    
    def play_games(self):
        if all([game.is_full() for game in self.schedule]) and len(self.schedule) > 0:
            for game in self.schedule:
                game.play()
                self.records.append(Record(
                    game.results[0].name, 
                    game.results[1].name, 
                    game.term, 
                    self.round_number
                ))
                self.curr_team_list.append(game.results[0]) 
            print("All games finished! You can use 4 to check the results.")
            if self.round_number == 2:
                print("This season ends!")
                print(f"{self.schedule[0].results[0].name} is the Champion!!")
            self.round_number += 1
            self.schedule = [] # reset
        else:
            print("No game in the current round, please add teams to the round first!")
    
    def display_game_result_records(self):
        Utils.RecordHeader()
        for record in self.records:
            print(Utils.RecordFormat(
                record.round_number, 
                record.game_number, 
                record.win_team, 
                record.lose_team
            ))
        Utils.RecordEnd()
    
    def add_team_to_season(self, team: Team):
        self.curr_team_list.append(team)