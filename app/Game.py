from Team import Team

class Game:
    def __init__(self, term: int):
        self.teams: list[Team] = []
        self.results: list[Team] = []
        self.term = term
        
    def add_team(self, team: Team):
        self.teams.append(team)
        
    def is_full(self):
        return len(self.teams) == 2
    
    def play(self):
        first_team = self.teams[0]
        second_team = self.teams[1]
        first_team_avg = first_team.average_credit()
        second_team_avg = second_team.average_credit()

        if first_team_avg > second_team_avg:
            winning_team_idx = 0
            losing_team_idx = 1
        elif first_team_avg < second_team_avg:
            winning_team_idx = 1
            losing_team_idx = 0
        else:
            # Draw
            winning_team_idx = 0 if first_team.name < second_team.name else 1
            losing_team_idx = 1 if winning_team_idx == 0 else 0
            
        diff = abs(first_team_avg - second_team_avg)
        for player in self.teams[winning_team_idx].players.players:
            player.update_credit(player.credit + diff / 5)
        for player in self.teams[losing_team_idx].players.players:
            player.update_credit(player.credit - diff / 5)

        self.results.append(self.teams[winning_team_idx])
        self.results.append(self.teams[losing_team_idx])
        