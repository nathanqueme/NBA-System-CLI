from Team import Team
from Utils import Utils

class Teams:
    def __init__(self, teams: list[Team]):
        self.teams = teams
        
    def run(self):
        option = ''
        while option.lower() != 'r':
            option = self.handle_option()
        
    def handle_option(self):
        choice = self.read_choice()
        if choice == "1":
            self.display_teams()
        elif choice == "2":
            self.display_players()
        elif choice == "3":
            self.add_team()
        elif choice == "4":
            self.manage_team()
        elif choice == "5":
            self.delete_team()
        elif choice == "6":
            self.display_players_by_level()
        return choice
    
    def read_choice(self):
        print(
            "Welcome to the Teams Page! Please make a selection from the menu:\n"
            "1. Display all teams.\n"
            "2. Display all players.\n"
            "3. Add a new team.\n"
            "4. Manage an existing team.\n"
            "5. Delete an existing team.\n"
            "6. Display all players by an level.\n"
            "R. Return to previous menu."
        )
        return input("Enter a choice: ")
    
    def display_teams(self):
        pass
    
    def display_players(self):
        pass
    
    def add_team(self):
        pass
    
    def manage_team(self):
        pass
    
    def delete_team(self):
        pass
    
    def display_players_by_level(self):
        pass
    
    