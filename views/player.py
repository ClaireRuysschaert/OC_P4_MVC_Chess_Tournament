from typing import Dict
from controllers.player import create_player
from models.player_model import Player
from utils.input_validation import get_string_input, get_birthday_date_input

def display_player_creation_menu(player_ine: str) -> None:
    """Display the player creation menu."""

    print("""\nVous avez choisi de créer un joueur.\n""")
            
    player_info = get_new_player_info(player_ine)
    create_player(player_info)

def get_new_player_info(player_ine: str) -> Dict[str, int|str]:
    """Return new player informations from user input."""

    first_name = get_string_input("Prénom du joueur:\n> ")
    
    name = get_string_input("Nom du joueur:\n> ")

    birthdate = get_birthday_date_input("Date de naissance du joueur au format : jj/mm/aaaa\n> ")

    chess_national_identifier = player_ine

    print(f"{first_name} {name} a été ajouté(e) aux joueurs créés.")

    return {
        "first_name": first_name,
        "name": name,
        "birthdate": birthdate,
        "chess_national_identifier": chess_national_identifier,
        "final_score": 0,
        "rank": 0,
    }