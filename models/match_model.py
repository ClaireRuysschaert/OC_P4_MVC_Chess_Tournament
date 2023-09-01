from typing import Dict, List, Tuple

from tinydb import Query

from data.database import matches_table
from utils.data_folder_management import create_data_folder_if_not_exists


class Match:
    def __init__(self, round_id: str, pair_players: Dict[str, List[Tuple]]):
        """Initialise les informations d'un match."""
        self.roud_id = round_id
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

    def match_data_to_json(self) -> Dict[str, str | list]:
        """Return match informations in dict/json format."""
        match_json_format = {
            "round_id": self.roud_id,
            "player_one": self.pair_players[0],
            "player_two": self.pair_players[1],
            "player_one_score": self.player_one_score,
            "player_two_score": self.player_two_score,
        }
        return match_json_format

    @staticmethod
    def create_match_to_db(match_json_format) -> int:
        """Create the new match to the database.
        These informations are saved in database.json in data folder."""
        create_data_folder_if_not_exists()
        match_id = matches_table.insert(match_json_format)
        return match_id

    @staticmethod
    def get_match_info_from_db(match_id: int | str) -> Dict[str, str | list]:
        """Get the informations of a match from the database."""
        match = matches_table.get(doc_id=str(match_id))
        return match

    @staticmethod
    def update_matchs_score_in_db(match, match_id: int) -> None:
        """Update the score of a match in the database."""
        matches_table.update(match, doc_ids=[match_id])

    @staticmethod
    def get_all_matches_from_round_id(round_id: int) -> List[Dict[str, str | list]]:
        """Get all the matches from a round id."""
        matches = matches_table.search(Query().round_id == round_id)
        return matches

    @classmethod
    def does_all_matches_have_been_played(cls, round_id: int) -> bool:
        """
        Check if all matches for a given round have been played.

        Args:
            round_id (int): The identifier of the round to check.

        Returns:
            bool: True if all matches have been played, False otherwise.
        """
        matches = cls.get_all_matches_from_round_id(round_id)
        total_matches = len(matches)
        matches_played = 0
        for match in matches:
            match_score_sum = match["player_one_score"] + match["player_two_score"]
            if int(match_score_sum) > 0:
                matches_played += 1
            else:
                print(f"Le match {match.doc_id} n'a pas encore été joué.")

        if matches_played == total_matches:
            return True
        else:
            return False
