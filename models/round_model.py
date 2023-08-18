import datetime
import os
from typing import Dict
from models.match_model import Match
from data.database import rounds_table
class Round:
    def __init__(self, name:str, start_time:str, end_time:str, matchs_list:list[Match], tournament_id:str, player_pairs:list[list[str]]):
        """Initialise les informations d'un round."""
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.matchs_list = matchs_list
        self.tournament_id = tournament_id
        self.player_pairs = player_pairs

    @staticmethod
    def get_time_now():
        return str(datetime.datetime.now().strftime("%d/%m/%Y, %Hh%M"))

    #TODO: à bouger dans le match model
    # def create_match(self) -> list[Match]:
    #     matchs = []
    #     for index, pair in enumerate(self.pair_players):
    #         matchs.append(Match(name=f"Match {index}", pair_players=pair))
    #     return matchs

    def get_round_results(self):
        print("Round over! Please enter match results.")
        self.end_time = self.get_time_now

        #TODO: à calculer de la match list ? 
        # for match in self.matchs:
        #     match.get_match_score()

    def __str__(self):
        return self.name
    
    def round_data_to_json(self) -> Dict[str, str|list]:
        """Return round informations in dict/json format."""
        round_json_format = {
            "name": self.name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "match_list": self.matchs_list,
            "tournament_id": self.tournament_id,
            "player_plairs": self.player_pairs,
        }
        return round_json_format
    
    @staticmethod
    def create_round_to_db(round_json_format) -> str:
        """Create the new round to the database.
        These informations are saved in database.json in data folder."""
        root_folder_path = os.path.join(os.getcwd(), "data")
        if not os.path.isdir(root_folder_path): 
            os.mkdir(root_folder_path)
        round_id = rounds_table.insert(round_json_format)
        return round_id
 