from Player import Player
from Players import Players
from Team import Team
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
            self.teams.run()
        elif choice == "2":
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
    suns_players = [
        Player("Chris Paul", 2000.00, 2, 30, "Suns", 1),
        Player("Devin Booker", 2000.00, 3, 30, "Suns", 2),
        Player("Mikal Bridges", 2000.00, 2, 30, "Suns", 3),
        Player("Jae Crowder", 2000.00, 4, 30, "Suns", 4),
        Player("Deandre Ayton", 2000.00, 2, 30, "Suns", 5)
    ]
    bulls_players = [
        Player("Zach Lavine", 1440.00, 2, 25, "Bulls", 1),
        Player("Nikola Vucevic", 1440.00, 3, 25, "Bulls", 2),
        Player("Patrick Williams", 1440.00, 2, 25, "Bulls", 3),
        Player("Thaddeus Young", 1440.00, 4, 25, "Bulls", 4),
        Player("Tomas Satoransky", 1440.00, 2, 25, "Bulls", 5)
    ]
    hawks_players = [
        Player("Zach Lavine", 1440.00, 2, 24, "Bulls", 1),
        Player("Nikola Vucevic", 1440.00, 3, 24, "Bulls", 2),
        Player("Patrick Williams", 1440.00, 2, 24, "Bulls", 3),
        Player("Thaddeus Young", 1440.00, 4, 24, "Bulls", 4),
        Player("Tomas Satoransky", 1440.00, 2, 24, "Bulls", 5)
    ]
    nets_players = [
        Player("Zach Lavine", 1680.00, 2, 29, "Bulls", 1),
        Player("Nikola Vucevic", 1680.00, 3, 29, "Bulls", 2),
        Player("Patrick Williams", 1680.00, 2, 29, "Bulls", 3),
        Player("Thaddeus Young", 1680.00, 4, 29, "Bulls", 4),
        Player("Tomas Satoransky", 1680.00, 2, 29, "Bulls", 5)
    ]
    teams = Teams([
        Team("Suns", Players(suns_players)),
        Team("Bulls", Players(bulls_players)),
        Team("Hawks", Players(hawks_players)),
        Team("Nets", Players(nets_players)),
    ])
    season = Season([], teams, 1, [])
    association = Association(teams, season)
    association.run()