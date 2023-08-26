from typing import List, Tuple

from models.match_model import Match
from models.player_model import Player
from models.round_model import Round
from models.tournament_model import Tournament


def create_match(round_id: str, pair_players: List[Tuple[str, str]]) -> int:
    """Create a new match instance from round_id and player_pairs and save it to database."""
    new_match = Match(round_id=round_id, pair_players=pair_players)

    match_json_format = new_match.match_data_to_json()

    match_id = new_match.create_match_to_db(match_json_format)
    Round.update_round_match_list(round_id, match_id)
    return match_id


def update_matchs_score(match_id: int, match_winner: int) -> None:
    """
    Update the scores of a match based on the result.

    Args:
        match_id (int): The ID of the match to update.
        match_winner (int): The result of the match:
            - 1: Player one wins.
            - 2: Player two wins.
            - 3 : It's a tie.
    """

    match = Match.get_match_info_from_db(match_id)

    if match_winner == 1:
        match["player_one_score"] = 1
        match["player_two_score"] = 0
    elif match_winner == 2:
        match["player_two_score"] = 1
        match["player_one_score"] = 0
    else:
        match["player_one_score"] = 0.5
        match["player_two_score"] = 0.5

    Match.update_matchs_score_in_db(match, match_id)
    print("Les scores du match ont été mis à jour.")

    match_updated = Match.get_match_info_from_db(match_id)
    Player.update_player_final_score_in_db(
        match_updated["player_one"], match_updated["player_one_score"]
    )
    Player.update_player_final_score_in_db(
        match_updated["player_two"], match_updated["player_two_score"]
    )
    print("Les scores des joueurs ont été mis à jour.")


def update_ranking(tournament_id: int) -> None:
    """Update the ranking of all players in the database."""
    all_players = Player.get_all_players_created_in_db()
    all_players.sort(key=lambda player: player["final_score"], reverse=True)
    tournament_player = Tournament.get_tournaments_players_ine(tournament_id)
    current_rank = 0
    current_score = 0

    for index, player in enumerate(all_players):
        if player["chess_national_identifier"] in tournament_player:
            if player["final_score"] != current_score:
                current_rank = index + 1
                current_score = player["final_score"]
            player["rank"] = current_rank
            Player.update_player_rank_in_db(
                player["chess_national_identifier"], player["rank"]
            )

    print("Le classement des joueurs a été mis à jour.")
    print("Voici le classement des joueurs :")

    for player in all_players:
        if player["chess_national_identifier"] in tournament_player:
            print(
                f"{player['rank']} - {player['first_name']} {player['name']} : {float(player['final_score'])} points."
            )

def does_match_belongs_to_round(current_round_id: str, match_id: int) -> bool:
    """Check if a match belongs to the current round."""
    match = Match.get_match_info_from_db(match_id)
    if match["round_id"] == current_round_id:
        return True
    else:
        return False