import os
from typing import Dict, List

from tinydb import Query
from data.database import players_table
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
        These informations are saved in database.json in data folder."""
        
        root_folder_path = os.path.join(os.getcwd(), "data")
        if not os.path.isdir(root_folder_path): 
            os.mkdir(root_folder_path)
        players_table.insert(player_json_format)

    @staticmethod
    def get_all_players_created_in_db() -> List[Dict[str, str|int]]:
        """Get all the players created in the database by their id."""
        player_query = Query() # NOSONAR
        # Retrieve all players by their id
        all_players_created = players_table.search(player_query.doc_id.all)
        return all_players_created
    
    @classmethod
    def get_all_players_ine_in_db(cls) -> List[str]:
        """Get all the players ine created in the database."""
        ine_list = []
        for player in cls.get_all_players_created_in_db():
            ine_list.append(player["chess_national_identifier"])
        return ine_list
    
    @classmethod
    def does_player_exists_in_db(cls, player_ine: str) -> bool:
        """Return True if the player exists in the database."""
        if player_ine in cls.get_all_players_ine_in_db():
            return True
        else:
            return False

    @staticmethod
    def update_met_competitors_list_in_db(player_ine: str, competitor_ine: str) -> None:
        """Add the competitor id in the met_competitors list of a player in the database."""
        player_query = Query()
        player = players_table.get(player_query.chess_national_identifier == player_ine)
        player["met_competitors"].append(competitor_ine)
        players_table.update(player, doc_ids=[player.doc_id])
