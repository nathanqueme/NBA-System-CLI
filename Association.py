from Player import Player
from Players import Players
from Team import Team
from Teams import Teams
from Season import Season

class Association:
    def __init__(self):
        suns_players = [
            Player("Devin Booker", 2500.00, 26, "Suns", 1),
            Player("Chris Paul", 1500.00, 37, "Suns", 3),
            Player("Deandre Ayton", 2000.00, 24, "Suns", 22),
            Player("Kevin Durant", 3000.00, 34, "Suns", 35),
            Player("Terrence Ross", 1000.00, 32, "Suns", 8)
        ]
        bulls_players = [ 
            Player("Andre Drummond", 1500.00, 29, "Bulls", 3),
            Player("Zach LaVine", 3000.00, 28, "Bulls", 8),
            Player("Dalen Terry", 900.00, 20, "Bulls", 25),
            Player("Terry Taylor", 1000.00, 23, "Bulls", 32),
            Player("Carlik Jones", 800.00, 25, "Bulls", 22)
        ]
        hawks_players = [
            Player("Trae Young", 2200.00, 24, "Hawks", 11),
            Player("John Collins", 2000.00, 25, "Hawks", 20),
            Player("Aaron Holiday", 800.00, 26, "Hawks", 3),
            Player("Jalen Johnson", 1000.00, 21, "Hawks", 1),
            Player("Trent Forrest", 1200.00, 24, "Hawks", 2)
        ]
        nets_players = [
            Player("Mikal Bridges", 2400.00, 26, "Nets", 1),
            Player("Ben Simmons", 2000.00, 26, "Nets", 10),
            Player("Patty Mills", 900.00, 34, "Nets", 8),
            Player("Joe Harris", 1200.00, 31, "Nets", 12),
            Player("Seth Curry", 1900.00, 32, "Nets", 30)
        ]
        teams_arr = [
            Team("Suns", Players()),
            Team("Bulls", Players()),
            Team("Hawks", Players()),
            Team("Nets", Players()),
        ]
        for player in suns_players:
            teams_arr[0].players.add_player(player)
        for player in bulls_players:
            teams_arr[1].players.add_player(player)
        for player in hawks_players:
            teams_arr[2].players.add_player(player)
        for player in nets_players:
            teams_arr[3].players.add_player(player)
        teams = Teams()
        for team in teams_arr:
            teams.add_team(team)
        self.teams: Teams = teams
        self.season: Season = Season()
    
    def run(self):
        option = ''
        while option != 'x':
            option = self.handle_option()
        print("Done")
        
    def handle_option(self):
        choice = self.read_choice()
        if choice == "1":
            self.teams.run()
        elif choice == "2":
            for team in self.teams.teams:
                self.season.add_team_to_season(team)
            self.season.run()
        return choice
    
    def read_choice(self):
        print(
            "Welcome to the Association! Please make a selection from the menu:\n"
            "1. Explore the teams.\n"
            "2. Arrange a new season.\n"
            "X. Exit the system."
        )
        return input("Enter a choice: ")


if __name__ == "__main__":
    association = Association()
    association.run()
    