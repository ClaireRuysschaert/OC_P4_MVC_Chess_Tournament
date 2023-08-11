import random
from typing import Dict, List, Tuple

from tinydb import Query

from data.database import players_table
from models.match_model import Match
from models.player_model import Player


def create_first_random_player_pairs() -> List[Tuple]:
    "Return first pair players from random mixing."
    
    Player = Query() # NOSONAR

    # Retrieve all players by their id
    all_players_created = players_table.search(Player.doc_id.all)

    # Save their INE in a list to be shuffled
    players_ine = [player["chess_national_identifier"] for player in all_players_created]
    random.shuffle(players_ine)

    # Create pair players
    pair_players = []

    for i in range(0, len(players_ine), 2):
        player_one = players_table.get(Player.chess_national_identifier == players_ine[i])
        player_two = players_table.get(Player.chess_national_identifier == players_ine[i+1])
        pair_players.append((player_one, player_two))
    
    return pair_players

def get_players_ine(pair_players: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    """Get the INE of each pair into pair_players list."""
    
    players_ine: List[Tuple[str, str]] = []
    for pair in pair_players:
        first_player_ine = pair[0]["chess_national_identifier"]
        second_player_ine = pair[1]["chess_national_identifier"]
        if first_player_ine and second_player_ine:
            players_ine.append((first_player_ine, second_player_ine))
        else:
            raise ValueError("Missing chess national identifier")
    
    return players_ine

def create_match(pair_players: List[Tuple[str, str]]) -> None:
    """Create a new match instance from player_pairs and save it to database."""
    # TODO: change the attributes to instanciate player_one and player_two + score
    try:
        new_match = Match(
            pair_players=pair_players
        )
        
        match_json_format = new_match.match_data_to_json()
        
        new_match.create_match_to_db(match_json_format)
    
    except Exception as e:
        print(e)

def update_scores(matchs_score):
    """Update the scores for each player in the matchs_score list into db."""
    
    for player_ine, score in matchs_score:
        # Get the player from the database using their INE
        Player = Query() # NOSONAR
        player = players_table.get(Player.chess_national_identifier == player_ine)
        
        # Update the player's score in the database
        player["final_score"] += score
        players_table.update({"final_score": player["final_score"]}, Player.chess_national_identifier == player_ine)
