from typing import Dict

from models.player_model import Player
from models.tournament_model import Tournament


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


def clean_players_after_tournament(tournament_id: str) -> None:
    """Clean player information for participants of the tournament
    after its conclusion."""
    tournament_players_ine = Tournament.get_tournaments_players_ine(tournament_id)
    for player_ine in tournament_players_ine:
        Player.clean_players_after_tournament_in_db(player_ine)
    print("Les joueurs ont été nettoyés.")


def get_players_from_alphabetic_order() -> list[dict[str, str | int]]:
    """Return all players from database in alphabetic order."""
    players = Player.get_all_players_created_in_db()
    players.sort(key=lambda player: player["name"])
    return players
