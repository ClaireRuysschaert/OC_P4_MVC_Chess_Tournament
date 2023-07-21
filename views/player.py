from typing import Dict

def get_new_player_info() -> Dict[str, int|str]:
    """Return new player informations from user input."""

    first_name = input("""Prénom du joueur:\n> """)
    
    name = input("""Nom du joueur:\n> """)

    birthdate = input("""Date de naissance du joueur:\n> """)

    chess_national_identifier = input("""Identifiant national d'échecs:\n> """)

    print(f"{first_name} {name} a été ajouté(e) aux joueurs créés.")

    return {
        "first_name": first_name,
        "name": name,
        "birthdate": birthdate,
        "chess_national_identifier": chess_national_identifier,
        "final_score": 0,
        "rank": 0,
    }