from typing import Dict

from models.player_model import Player


def create_player(player_info: Dict[str, int | str]) -> None:
    """Create a new player from player informations and save it to database."""

    player = Player(
        first_name=player_info["first_name"],
        name=player_info["name"],
        birthdate=player_info["birthdate"],
        chess_national_identifier=player_info["chess_national_identifier"],
        final_score=player_info["final_score"],
        rank=player_info["rank"],
    )

    player_json_format = player.player_data_to_json()

    player.create_player_to_db(player_json_format)
