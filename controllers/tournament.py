from models.tournament_model import Tournament

def create_new_tournament(tournament_info: dict) -> str:
    """Create a new tournament instance from tournament_info and save it to database."""

    tournament = Tournament(
        name = tournament_info["tournament_name"],
        location = tournament_info["tournament_location"],
        number_of_players = tournament_info["tournament_number_of_players"],
        description = tournament_info["tournament_description"],
        number_of_rounds = tournament_info["tournament_number_of_rounds"],
    )
    
    tournament_json_format = tournament.tournament_data_to_json()
    
    tournament_id = tournament.create_tournament_to_db(tournament_json_format)
    return tournament_id