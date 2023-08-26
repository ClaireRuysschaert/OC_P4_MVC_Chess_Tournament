import random
from typing import List, Tuple

from models.player_model import Player
from models.round_model import Round
from models.tournament_model import Tournament


def assign_player_pairs(
    tournament_id: int, current_round_number: int
) -> list[list[str]]:
    """
    Assign player pairs for a tournament round.

    Args:
        tournament_id (int): The ID of the tournament.
        current_round_number (int): The current round number.

    Returns:
        list[list[str]]: List of player pairs for the round."""

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
        # Other rounds, players are sorted by their rank
        # If 2 ranks are equal, assign competitors that haven't played together
        all_players_in_db = Player.get_all_players_created_in_db()
        tournament_player_ine = Tournament.get_tournaments_players_ine(tournament_id)

        tournament_players = []

        # Filter and sort tournament players by rank
        for player in all_players_in_db:
            if player["chess_national_identifier"] in tournament_player_ine:
                tournament_players.append(player)

        tournament_players.sort(key=lambda player: player["rank"])
        players_that_dont_have_pairs = list(tournament_players)

        player_pairs = []

        player_index = 0

        while len(players_that_dont_have_pairs) != 0:
            player_one = players_that_dont_have_pairs[player_index]
            player_two = players_that_dont_have_pairs[player_index + 1]

            if player_one["rank"] < player_two["rank"]:
                player_pairs.append(
                    (
                        [
                            player_one["chess_national_identifier"],
                            player_two["chess_national_identifier"],
                        ]
                    )
                )
                players_that_dont_have_pairs.remove(player_one)
                players_that_dont_have_pairs.remove(player_two)

            if player_one["rank"] == player_two["rank"]:
                if (
                    player_two["chess_national_identifier"]
                    in player_one["met_competitors"]
                ):
                    print("player two in player one met competitors\n\n")
                    while (
                        player_two["chess_national_identifier"]
                        in player_one["met_competitors"]
                    ):
                        print("player three or more in player one met competitors\n\n")
                        player_index += 1
                        # Handle the case where player_one have already played with the remaining players
                        # Get the player with the closest rank from player one's rank
                        try:
                            player_two = players_that_dont_have_pairs[player_index + 1]
                        except IndexError:
                            player_two = players_that_dont_have_pairs[1]
                            break

                player_pairs.append(
                    (
                        [
                            player_one["chess_national_identifier"],
                            player_two["chess_national_identifier"],
                        ]
                    )
                )
                players_that_dont_have_pairs.remove(player_one)
                players_that_dont_have_pairs.remove(player_two)

            player_index = 0

        Player.update_met_competitors_list_in_db(
            player_one["chess_national_identifier"],
            player_two["chess_national_identifier"],
        )
        Player.update_met_competitors_list_in_db(
            player_two["chess_national_identifier"],
            player_one["chess_national_identifier"],
        )
        return player_pairs


def create_new_round(
    tournament_id: int, current_round_number: int
) -> Tuple[str, List[List[str]], int]:
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
