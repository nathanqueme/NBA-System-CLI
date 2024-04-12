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
        self.level = self._get_level(credit)
 
    def get_number(self):
        return self.number
    
    def get_age(self):
        return self.age
    
    def update_credit(self, credit):
        self.credit = credit
        self.level = self._get_level(credit)
        
    def _get_level(self, credit):
        if credit < 1000.00:
           return "Edge"
        elif credit < 1500.00:
            return "Common"
        elif credit < 2000.00:
            return "Core"
        else:
            return "All Star"