from typing import Dict

from tabulate import tabulate

from controllers.player import create_player, get_players_from_alphabetic_order
from models.player_model import Player
from utils.input_validation import validate_birthday_date_input, validate_string_input


def display_player_creation_menu(player_ine: str) -> None:
    """Display the player creation menu."""

    if Player.does_player_exists_in_db(player_ine):
        print("\nErreur. Le joueur existe déjà dans la base de données!\n")
    else:
        print(
            "\nLe joueur n'existe pas dans la base de données,"
            "nous allons le créer.\n"
        )
        player_info = get_new_player_info(player_ine)
        create_player(player_info)


def get_new_player_info(player_ine: str) -> Dict[str, int | str]:
    """Return new player informations from user input."""

    first_name = validate_string_input("Prénom du joueur:\n> ")

    name = validate_string_input("Nom du joueur:\n> ")

    birthdate = validate_birthday_date_input(
        "Date de naissance du joueur au format : jj/mm/aaaa\n> "
    )

    chess_national_identifier = player_ine

    print(f"\n{first_name} {name} a été ajouté(e) aux joueurs créés.\n")

    return {
        "first_name": first_name,
        "name": name,
        "birthdate": birthdate,
        "chess_national_identifier": chess_national_identifier,
        "final_score": 0,
        "rank": 0,
    }


def report_display(user_input: int, tournament_id: int = None) -> None:
    if user_input == 1:  # Liste des joueurs par ordre alphabétique
        sorted_players = get_players_from_alphabetic_order()
        table = []
        keys_to_print = list(sorted_players[0].keys())[:4]
        for player in sorted_players:
            table.append([player[key] for key in keys_to_print])
        print("\nVoici la liste des joueurs par ordre alphabétique :")
        print(tabulate(table, headers=keys_to_print, tablefmt="pretty"))
