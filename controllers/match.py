from typing import Dict, List, Tuple
from models.match_model import Match
import random
from tinydb import Query
from data.database import players_table

def create_first_random_player_pairs() -> List[Tuple]:
    "Return first pair players from random mixing."
    
    Player = Query()

    # Retrieve all players by their id
    all_players_created = players_table.search(Player.doc_id.all)

    # Save their INE in a list to be shuffled
    players_INE = [player["chess_national_identifier"] for player in all_players_created]
    random.shuffle(players_INE)

    # Create pair players
    pair_players = []

    for i in range(0, len(players_INE), 2):
        player_one = players_table.get(Player.chess_national_identifier == players_INE[i])
        player_two = players_table.get(Player.chess_national_identifier == players_INE[i+1])
        pair_players.append((player_one, player_two))
    
    return {
        "pair_players": pair_players
    }



def create_match(pair_players:Tuple[object]) -> None:
    """Create a new match instance from player_pairs and save it to database."""
    
    new_match = Match(
        pair_players=pair_players["pair_players"]
    )
    
    match_json_format = new_match.match_data_to_json()
    
    new_match.create_match_to_db(match_json_format)
    


    #récupérer le score
    #modifier le dict en json
    #créer le match en db