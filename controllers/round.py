import random
from typing import Dict

from models.player_model import Player
from models.round_model import Round
from models.tournament_model import Tournament


def assign_player_pairs(
    tournament_id: int, current_round_number: int
) -> list[list[str]]:
    """Assign players pairs for the round."""

    if current_round_number == 0:
        players = Tournament.get_tournaments_players_ine(tournament_id)
        random.shuffle(players)
        # create a list of pairs of players from the list of players
        player_pairs = []

        for player in range(0, len(players), 2):
            player_pairs.append([players[player], players[player + 1]])
            # Update met_competitors list from players table
            Player.update_met_competitors_list_in_db(
                players[player], players[player + 1]
            )
            Player.update_met_competitors_list_in_db(
                players[player + 1], players[player]
            )
        return player_pairs
    else:
        # Other rounds, players are sorted by their scores
        # If 2 final_scores are equal, assign competitors that haven't played together
        pass


def create_new_round(
    tournament_id: int, current_round_number: int
) -> (str, list[list[str]]):
    """
    Create a new round instance from round_info and save it to database.
    """
    player_pairs = assign_player_pairs(tournament_id, current_round_number)

    round_number_to_create = current_round_number + 1

    round = Round(
        name="Round " + str(round_number_to_create),
        start_time=Round.get_time_now(),
        end_time="",
        matchs_list=[],
        tournament_id=tournament_id,
        player_pairs=player_pairs,
    )

    round_json_format = round.round_data_to_json()
    round_id = round.create_round_to_db(round_json_format)
    Tournament.update_round_list_to_tournament(tournament_id, round_id)
    new_round_number = current_round_number + 1
    return round_id, player_pairs, new_round_number
