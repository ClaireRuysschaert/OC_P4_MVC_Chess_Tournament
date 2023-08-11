from typing import Dict
from models.player_model import Player
import random
from data.database import matches_table
import os
from typing import Dict, List, Tuple
class Match:
    def __init__(self, pair_players: Dict[str, List[Tuple]]):
        """Initialise les informations d'un match."""
        self.pair_players = pair_players
        self.player_one = pair_players[0]
        self.player_two = pair_players[1]
        self.player_one_score = 0
        self.player_two_score = 0

    def __str__(self):
        """Tuple with 2 lists of 2 elements : players and score"""
        return (
            [self.player_one, self.player_one_score],
            [self.player_two, self.player_two_score],
        )

    def match_data_to_json(self) -> Dict[str, str|list]:
        """Return match informations in dict/json format."""
        match_json_format = {
            "player_one": self.pair_players[0],
            "player_two": self.pair_players[1],
            "player_one_score": self.player_one_score,
            "player_two_score": self.player_two_score,
        }
        return match_json_format
    
    @staticmethod
    def create_match_to_db(match_json_format) -> None:
        """Create the new match to the database.
        These informations are saved in database.json in data folder."""
        root_folder_path = os.path.join(os.getcwd(), "data")
        if not os.path.isdir(root_folder_path): 
            os.mkdir(root_folder_path)
        matches_table.insert(match_json_format)

    
        