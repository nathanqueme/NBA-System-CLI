from Players import Players
from Utils import Utils

class Team:
    def __init__(self,
        name: str,
        players: Players
    ):
        self.name = name
        self.players = players
        
    def run(self):
        option = ''
        while option.lower() != 'r':
            option = self.handle_option()
    
    def handle_option(self):
        choice = self.read_choice()
        if choice == "1":
            self.display_players()
        elif choice == "2":
            self.add_player()
        elif choice == "3":
            self.update_player()
        elif choice == "4":
            self.delete_player()
        return choice
    
    def read_choice(self):
        print(
            f"Welcome to the {self.name} 's Page! Please make a selection from the menu:\n"
            "1. Display team's players.\n"
            "2. Add a new player.\n"
            "3. Update an existing player.\n"
            "4. Delete an existing player.\n"
            "R. Return to previous menu."
        )
        return input("Enter a choice: ")
    
    def display_players(self):
        pass
    
    def add_player(self):
        pass
    
    def update_player(self):
        pass
    
    def delete_player(self):
        pass
    
    def get_number_of_players(self):
        return len(self.players.get_players())
    
    def get_avg_player_credit(self):
        players_arr = self.players.get_players()
        return sum(player.credit for player in players_arr) / len(players_arr)
    
    def get_avg_age(self):
        players_arr = self.players.get_players()
        return sum(player.age for player in players_arr) / len(players_arr)
    