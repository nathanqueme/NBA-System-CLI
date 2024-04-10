from Teams import Teams
from Season import Season

class Association:
    def __init__(self, teams: Teams, season: Season):
        self.teams = teams
        self.season = season
    
    def run(self):
        option = ''
        while option != 'x':
            option = self.use_option()
        print("Done")
        
    def use_option(self):
        choice = self.read_choice()
        
        return choice
    
    def read_choice():
        return input("Enter option: ")