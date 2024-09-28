from Player import Player

class Players:
    def __init__(self):
        self.players: list[Player] = []
    
    def add_player(self, player: Player):
        self.players.append(player)
    
    def get_players(self):
        return self.players