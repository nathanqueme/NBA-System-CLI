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


# | Player Name          | Credit         | Level        | Age   | No    | Team      |
# +----------------------+----------------+--------------+-------+-------+-----------+
# | Devin Booker         | 2500.00        | All Star     | 26    | 1     | Suns      |
# | Chris Paul           | 1500.00        | Core         | 37    | 3     | Suns      |
# | Deandre Ayton        | 2000.00        | All Star     | 24    | 22    | Suns      |
# | Kevin Durant         | 3000.00        | All Star     | 34    | 35    | Suns      |
# | Terrence Ross        | 1000.00        | Common       | 32    | 8     | Suns      |
    suns_players = [
        Player("Devin Booker", 2500.00, 26, "Suns", 1),
        Player("Chris Paul", 1500.00, 37, "Suns", 3),
        Player("Deandre Ayton", 2000.00, 24, "Suns", 22),
        Player("Kevin Durant", 3000.00, 34, "Suns", 35),
        Player("Terrence Ross", 1000.00, 32, "Suns", 8)
    ]
    
# | Player Name          | Credit         | Level        | Age   | No    | Team      |
# +----------------------+----------------+--------------+-------+-------+-----------+
# | Andre Drummond       | 1500.00        | Core         | 29    | 3     | Bulls     |
# | Zach LaVine          | 3000.00        | All Star     | 28    | 8     | Bulls     |
# | Dalen Terry          | 900.00         | Edge         | 20    | 25    | Bulls     |
# | Terry Taylor         | 1000.00        | Common       | 23    | 32    | Bulls     |
# | Carlik Jones         | 800.00         | Edge         | 25    | 22    | Bulls     |
    bulls_players = [ 
        Player("Andre Drummond", 1500.00, 29, "Bulls", 3),
        Player("Zach LaVine", 3000.00, 28, "Bulls", 8),
        Player("Dalen Terry", 900.00, 20, "Bulls", 25),
        Player("Terry Taylor", 1000.00, 23, "Bulls", 32),
        Player("Carlik Jones", 800.00, 25, "Bulls", 22)
    ]
    
# | Player Name          | Credit         | Level        | Age   | No    | Team      |
# +----------------------+----------------+--------------+-------+-------+-----------+
# | Trae Young           | 2200.00        | All Star     | 24    | 11    | Hawks     |
# | John Collins         | 2000.00        | All Star     | 25    | 20    | Hawks     |
# | Aaron Holiday        | 800.00         | Edge         | 26    | 3     | Hawks     |
# | Jalen Johnson        | 1000.00        | Common       | 21    | 1     | Hawks     |
# | Trent Forrest        | 1200.00        | Common       | 24    | 2     | Hawks     |
    hawks_players = [
        Player("Trae Young", 2200.00, 24, "Hawks", 11),
        Player("John Collins", 2000.00, 25, "Hawks", 20),
        Player("Aaron Holiday", 800.00, 26, "Hawks", 3),
        Player("Jalen Johnson", 1000.00, 21, "Hawks", 1),
        Player("Trent Forrest", 1200.00, 24, "Hawks", 2)
    ]
# | Player Name          | Credit         | Level        | Age   | No    | Team      |
# +----------------------+----------------+--------------+-------+-------+-----------+
# | Mikal Bridges        | 2400.00        | All Star     | 26    | 1     | Nets      |
# | Ben Simmons          | 2000.00        | All Star     | 26    | 10    | Nets      |
# | Patty Mills          | 900.00         | Edge         | 34    | 8     | Nets      |
# | Joe Harris           | 1200.00        | Common       | 31    | 12    | Nets      |
# | Seth Curry           | 1900.00        | Core         | 32    | 30    | Nets      |
    nets_players = [
        Player("Mikal Bridges", 2400.00, 26, "Nets", 1),
        Player("Ben Simmons", 2000.00, 26, "Nets", 10),
        Player("Patty Mills", 900.00, 34, "Nets", 8),
        Player("Joe Harris", 1200.00, 31, "Nets", 12),
        Player("Seth Curry", 1900.00, 32, "Nets", 30)
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