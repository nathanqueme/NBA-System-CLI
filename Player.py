from Utils import Utils

class Player:
    def __init__(
        self, 
        name: str,
        credit: float,
        age: int,
        team: str,
        number: int
    ):
        self.name = name
        self.credit = credit
        self.age = age
        self.team = team
        self.number = number
        if credit < 1000:
            self.level = "Edge"
        elif credit < 1500:
            self.level = "Common"
        elif credit < 2000:
            self.level = "Core"
        else:
            self.level = "All Star"
 
    def get_number(self):
        return self.number
    
    def get_age(self):
        return self.age
