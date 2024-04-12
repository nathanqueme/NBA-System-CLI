from Player import Player
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
        Utils.playerHeader()
        for player in self.players.get_players():
            print(Utils.PlayerFormat(
                name=player.name,
                credit=player.credit,
                level=player.level,
                No=player.number,
                age=player.age
            ))
        Utils.playerTableEnd()
    
    def add_player(self):
        name = input("Please enter the player's name: ").strip()
        credit = float(input( "Please enter the player's credit: ").strip())
        age = int(input("Please enter the player's age: ").strip())
        number = int(input("Please enter the player's No: ").strip())
        while number in [player.number for player in self.players.get_players()]:
            match = [player for player in self.players.get_players() if player.number == number][0]
            number = int(input(f"This No has been occupied by: {match.name}. Please re-enter the No: "))
        self.players.players.append(Player(name, credit, age, self.name, number))
        print(f"Player {name} added!")

    def update_player(self):
        original_name = input("Please enter the player's name: ").strip()
        if original_name.lower() not in [player.name.lower() for player in self.players.get_players()]:
            print("Player does not exist.")
            return
        name = input("Please enter the name: ").strip()
        credit = float(input( "Please enter the credit: ").strip())
        age = int(input("Please enter the age: ").strip())
        number = int(input("Please enter the No: ").strip())
        while number in [player.number for player in self.players.get_players()]:
            match = [player for player in self.players.get_players() if player.number == number][0]
            number = int(input(f"This No has been occupied by: {match.name}. Please re-enter the No: ").strip())
        if original_name.lower() in [player.name.lower() for player in self.players.get_players()]:
            idx = [player.name.lower() for player in self.players.get_players()].index(original_name.lower())
            self.players.players.pop(idx)
            self.players.players.append(Player(name, credit, age, self.name, number))
            print("Player information updated.")
    
    def delete_player(self):
        name = input("Please enter the player's name: ")
        names = [player.name for player in self.players.get_players()]
        if name in names:
            self.players.players.pop(names.index(name))
            print("Player deleted.")
        else:
            print("Player does not exist.")
    
    def get_number_of_players(self):
        return len(self.players.get_players())
    
    def get_avg_player_credit(self):
        players_arr = self.players.get_players()
        if players_arr == []:
            return 0
        return sum(player.credit for player in players_arr) / len(players_arr)
    
    def get_avg_age(self):
        players_arr = self.players.get_players()
        if players_arr == []:
            return 0
        return sum(player.age for player in players_arr) / len(players_arr)
    
    def average_credit(self):
        players = self.players.get_players()
        return sum([pl.credit for pl in players]) / len(players)
