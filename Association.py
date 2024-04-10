from Teams import Teams
from Season import Season

class Association:
    def __init__(self, teams: Teams, season: Season):
        self.teams = teams
        self.season = season
    
    def run(self):
        option = ''
        while option != 'x':
            option = self.handle_option()
        print("Done")
        
    def handle_option(self):
        choice = self.read_choice()
        if choice == "1":
            print("Exploring teams")
            self.teams.explore()
        elif choice == "2":
            print("Arranging a new season")
            self.season.arrange()
        return choice
    
    def read_choice():
        print(
            "Welcome to the Association! Please make a selection from the menu:\n"
            "1. Explore the teams.\n"
            "2. Arrange a new season.\n"
            "X. Exit the system."
        )
        return input("Enter a choice: ")
    