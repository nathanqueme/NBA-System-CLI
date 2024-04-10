from Team import Team

class Game:
    def __init__(self, teams: list[Team], results: list[Team]):
        self.teams = teams
        self.results = results