import datetime
from typing import Dict

from data.database import rounds_table
from models.match_model import Match
from utils.data_folder_management import create_data_folder_if_not_exists


class Round:
    def __init__(
        self,
        name: str,
        start_time: str,
        end_time: str,
        matchs_list: list[Match],
        tournament_id: str,
        player_pairs: list[list[str]],
    ):
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

    def get_round_results(self):
        print("Round over! Please enter match results.")
        self.end_time = self.get_time_now()

    def __str__(self):
        return self.name

    def round_data_to_json(self) -> Dict[str, str | list]:
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
        create_data_folder_if_not_exists()
        round_id = rounds_table.insert(round_json_format)
        return round_id

    @staticmethod
    def update_round_match_list(round_id: str, match_id: int) -> None:
        """Update the match list of the round in the database."""
        round = rounds_table.get(doc_id=str(round_id))
        round["match_list"].append(match_id)
        rounds_table.update(round, doc_ids=[int(round_id)])

    @staticmethod
    def get_round_infos_from_db(round_id: str) -> Dict[str, str | list]:
        """Get the round informations from the database."""
        round = rounds_table.get(doc_id=str(round_id))
        return round

    @staticmethod
    def update_round_end_time(round_id: str) -> None:
        """Update the end time of the round in the database."""
        round = rounds_table.get(doc_id=str(round_id))
        round["end_time"] = Round.get_time_now()
        rounds_table.update(round, doc_ids=[int(round_id)])
