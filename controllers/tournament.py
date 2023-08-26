from models.tournament_model import Tournament


def create_new_tournament(tournament_info: dict) -> str:
    """Create a new tournament instance from tournament_info and save it to database."""

    tournament = Tournament(
        name=tournament_info["tournament_name"],
        location=tournament_info["tournament_location"],
        number_of_players=tournament_info["tournament_number_of_players"],
        description=tournament_info["tournament_description"],
        number_of_rounds=tournament_info["tournament_number_of_rounds"],
    )

    tournament_json_format = tournament.tournament_data_to_json()

    tournament_id = tournament.create_tournament_to_db(tournament_json_format)
    return tournament_id


def get_current_round_number(tournament_id: int) -> int:
    """Return the current round number of a tournament.
    It correspond to the length of the round_list attribute of the tournament.
    This attribute is updated at each round creation."""
    tournament = Tournament.get_tournaments_infos_from_db(tournament_id)
    current_round_number = len(tournament["round_list"])
    return current_round_number

def get_current_round_id(tournament_id: int) -> int:
    """Return the current round id of a tournament.
    It correspond to the last element of the round_list attribute of the tournament.
    This attribute is updated at each round creation."""
    tournament = Tournament.get_tournaments_infos_from_db(tournament_id)
    current_round_id = tournament["round_list"][-1]
    return current_round_id
