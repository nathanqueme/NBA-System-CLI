from Players import Players
from Team import Team
from Utils import Utils

class Teams:
    def __init__(self):
        self.teams: list[Team] = []
        
    def add_team(self, team: Team):
        self.teams.append(team)
        
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
            self.add_new_team()
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
    
    # Python:
    # teamsHeader( )defines the output format of the header: +-----------+--------------------+-----------------------+-------------+ | Team Name | Number of Players | Average Player Credit | Average Age | +-----------+--------------------+-----------------------+-------------+
    # teamsTabkeEnd( )defines the output format of the end of the table.
    # To print the team’s information following the pre-defined format, you can use the following
    # code: print(Utils.teamsFormat(name,NoofPlayer,AvgCredit,AvgAge)) Note:
    # def teamsFormat(name,numofplayer,avgcredit,avgage):
    # return "| %-*s | %-*s | %-*s | %-*s |" %(20,name,19,numofplayer,21,"{:.2f}".format(avgcredit),12,"{:.2f}".format(avgage))
    # defines the space for the string.
    # To demonstrate the information of the team, such as the information of suns, the whole code may look like this:
    # Utils.teamsHeader() print(Utils.teamsFormat(name,NoofPlayer,AvgCredit,AvgAge)) Utils.teamTableEnd()


    def display_teams(self):
        Utils.teamsHeader()
        for team in self.teams:
            print(Utils.teamsFormat(
                name=team.name, 
                numofplayer=team.get_number_of_players(), 
                avgcredit=team.get_avg_player_credit(),
                avgage=team.get_avg_age()))
        Utils.teamTableEnd()
    
    def display_players(self):
        Utils.DisplayPlayerFromAllTeamsHeader()
        for team in self.teams:
            for player in team.players.get_players():
                print(Utils.DisplayPlayerFromAllTeamsFormat(
                    player.name,
                    player.credit,
                    player.level,
                    player.number,
                    player.age,
                    player.team
                ))
            Utils.DisplayPlayerFromAllTeamsEnd()
    
    def add_new_team(self):
        team_name = input("Please enter the name of the team: ").strip()
        while team_name in [team.name for team in self.teams]:
            team_name = input(f"Team {team_name} already exists! Please enter a new name: ")
        print(f"Team {team_name} added!")
        self.teams.append(Team(team_name, Players([])))
    
    def manage_team(self):
        team_name = input("Please enter the team's name that you want to manage: ").strip()
        if team_name not in [team.name for team in self.teams]:
            print("Team does not exist!")
            return
        team = [team for team in self.teams if team.name == team_name][0]
        team.run()
    
    def delete_team(self):
        team_name = input("Please enter the team's name that you want to delete: ").strip()
        team_names = [team.name for team in self.teams]
        if team_name in team_names:
            self.teams.pop(team_names.index(team_name))
            print("Team deleted.")
        else:
            print(f"The team {team_name} has been deleted.")
    
    def display_players_by_level(self):
        levels = ["Edge", "Common", "Core", "All Star"]
        level = input("Please enter the player's level that you want to view: ")  
        while level not in levels:
            level = input("No such level! Please re-enter the level: ")
        Utils.DisplayPlayerFromAllTeamsHeader()
        for team in self.teams:
            for player in team.players.get_players():
                if player.level == level:
                    print(Utils.DisplayPlayerFromAllTeamsFormat(
                        player.name,
                        player.credit,
                        player.level,
                        player.number,
                        player.age,
                        player.team
                    ))
        Utils.DisplayPlayerFromAllTeamsEnd()
        
    
    