from Team import Team
from Utils import Utils
from Game import Game
from Record import Record

class Session:
    def __init__(
        self,
        schedule: list[Game],
        curr_team_list: list[Team],
        round_number: int,
        records: list[Record]
    ):
        self.schedule = schedule
        self.curr_team_list = curr_team_list
        self.round_number = round_number
        self.records = records
