from typing import Dict
from models.match_model import Match

def create_match(match_infos: Dict[str, str|list]) -> None:
    """Create a new match from match informations and save it to database."""
    
    new_match = Match(
        name = match_infos["name"],
        pair_players=match_infos["pair_players"]
    )
    
    match_json_format = new_match.match_data_to_json()
    
    new_match.create_match_to_db(match_json_format)
    


    #récupérer le score
    #modifier le dict en json
    #créer le match en db