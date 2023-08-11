import datetime
import random
from turtle import st
from typing import Dict, List
from models.round_model import Round
import os
from data.database import tournaments_table
class Tournament:
    def __init__(
        self, name: str, location: str, number_of_players: int, number_of_rounds: int = 4, start_time:str = None, description=""
    ):
        self.name = name
        self.location = location
        self.players = []
        self.number_of_players = number_of_players
        self.start_time = start_time
        self.end_time = ""
        self.number_of_rounds = number_of_rounds
        self.round_list = []
        self.description = description
    
    @staticmethod
    def get_time_now():
        return str(datetime.datetime.now().strftime("%d/%m/%Y, %Hh%M"))
    
    def __str__(self):
        return f"Tournoi {self.name} à {self.location} le {self.start_time}."


    def tournament_data_to_json(self) -> Dict[str, str|int]:
        """Return tournament informations in dict/json format."""
        tournament_json_format = {
            "name": self.name,
            "location": self.location,
            "number_of_players": self.number_of_players,
            "number_of_rounds": self.number_of_rounds,
            "start_time": self.get_time_now(),
            "end_time": self.end_time,
            "players": self.players,
            "round_list": self.round_list,
            "description": self.description,
        }
        return tournament_json_format
        
    @staticmethod
    def create_tournament_to_db(tournament_json_format) -> str:
        """Create the new tournament to the database.
        These informations are saved in database.json in data folder."""
        root_folder_path = os.path.join(os.getcwd(), "data")
        if not os.path.isdir(root_folder_path): 
            os.mkdir(root_folder_path)
        tournament_id = tournaments_table.insert(tournament_json_format)
        return tournament_id
    
    @staticmethod
    def get_tournaments_players_ine(tournament_id: int) -> list[str]:
        """Get the INEs of the players in a tournament from the database."""
        tournament = tournaments_table.get(doc_id=tournament_id)
        return tournament["players"]
    
    @classmethod
    def does_player_exists_in_tournament_list(cls, tournament_id, player_ine: str) -> bool:
        """Return True if the player exists in the tournament list."""
        if player_ine in cls.get_tournaments_players_ine(tournament_id):
            return True
        else:
            return False
    
    @staticmethod
    def get_tournaments_infos_from_db(tournament_id: int) -> Dict[str, str|int]:
        """Return the tournament informations from the database."""
        tournament_data = tournaments_table.get(doc_id=tournament_id)
        return tournament_data

    @classmethod
    def add_player_to_tournament(cls, tournament_id: int, player_ine: str) -> None:
        """Add a player ine to the players list of a tournament (retrieved by its id) in the database."""
        tournament_data = cls.get_tournaments_infos_from_db(tournament_id)
        tournament_data["players"].append(player_ine)
        tournaments_table.update(tournament_data, doc_ids=[tournament_id])
    
    
    
    
    
    # def create_rounds(self, round_number):
    #     pair_players = self.assign_players_pairs(current_round=round_number)
    #     round = Round("Round " + str(round_number), pair_players)
    #     self.round_list.append(round)

    # def assign_players_pairs(self, current_round_number):
    #     # First Round, players are shuffled randomly
    #     if current_round_number == 0:
    #         sorted_players = random.shuffle(self.players)
    #     # Other rounds, players are sorted by their scores
    #     else:
    #         sorted_players = sorted(
    #             self.players, key=lambda player: player.final_score, reverse=True
    #         )

    #         # If 2 final_scores are equal, assign competitors that haven't played together
    #         # for player in sorted_players:
    #         #     if player.final_score ==