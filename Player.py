from Utils import Utils

class Player:
    def __init__(
        self, 
        name: str,
        credit: float,
        level: str,
        age: int,
        team: str,
        number: int
    ):
        self.name = name
        self.credit = credit
        self.level = level
        self.age = age
        self.team = team
        self.number = number
 