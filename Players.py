from Player import Player
from Utils import Utils

class Players:
    def __init__(self, players: list[Player]):
        self.players = players
        
    def get_players(self):
        return self.players