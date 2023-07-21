import os
from typing import Dict
from data.database import player_database
class Player:
    
    players = []
    
    def __init__(
        self,
        first_name: str,
        name: str,
        birthdate: str,
        tournament_score=0,
        final_score=0,
        rank=0,
        chess_national_identifier="",
    ):
        """Initialise les informations du joueur."""
        self.first_name = first_name
        self.name = name
        self.birthdate = birthdate
        self.ine = chess_national_identifier
        self.tournament_score = tournament_score
        self.final_score = final_score
        self.rank = rank
        self.met_competitors = []

    def __str__(self):
        return f"Player {self.first_name} {self.name} ranking is {self.rank} with {self.final_score} points."

    def player_data_to_json(self) -> Dict[str, str|int]:
        """Return player informations in dict/json format."""
        player_json_format = {
            "first_name": self.first_name,
            "name": self.name,
            "birthdate": self.birthdate,
            "chess_national_identifier": self.ine, 
            "tournament_score": self.tournament_score, 
            "final_score": self.final_score, 
            "rank": self.rank, 
            "met_competitors" : self.met_competitors
        }
        return player_json_format

    @staticmethod
    def create_player_to_db(player_json_format) -> None:
        """Create the new player to the database.
        These informations are saved in players_data.json in data folder."""
        
        root_folder_path = os.path.join(os.getcwd(), "data")
        if not os.path.isdir(root_folder_path): 
            os.mkdir(root_folder_path)
        player_database.insert(player_json_format)
