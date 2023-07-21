#from models.match_model import Match
from typing import Dict
from tinydb import Query
from data.database import player_database

def get_new_match_info() -> Dict[str, str|list]:
    "Return new match informations from user input."
    
    name = input("""Nom du match:\n> """)
    player_one_INE = input("""Identifiant national d'échec du premier joueur:\n> """)
    player_two_INE = input("""Identifiant national d'échec du second joueur:\n> """)
    
    Player = Query()
    player_one = player_database.search(Player.chess_national_identifier == player_one_INE)   
    player_two = player_database.search(Player.chess_national_identifier == player_two_INE)
    pair_players = [player_one, player_two]
    
    print(f"Le match {name} a été sauvegardé avec succès.")
    
    return {
        "name": name,
        "pair_players": pair_players
    }