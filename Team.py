from Utils import Utils
from Players import Players

class Team:
    def __init__(self,
        name: str,
        players: Players
    ):
        self.name = name
        self.players = players