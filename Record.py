from Utils import Utils

class Record:
    def __init__(self,
        win_team: str,
        lose_team: str,
        game_number: int,
        round_number: int
    ):
        self.win_team = win_team
        self.lose_team = lose_team
        self.game_number = game_number
        self.round_number = round_number