from models.player_model import Player
from models.tournament_model import Tournament
from utils.input_validation import (
    validate_chess_national_identifier_input,
    validate_integer_input,
    validate_number_of_players_input,
    validate_string_input,
    validate_yes_no_input,
)
from views.player import display_player_creation_menu
from tabulate import tabulate


def get_tournament_info_from_user() -> dict:
    """Get the tournament informations from the user."""

    tournament_name = validate_string_input("\nEntrez le nom du tournoi : \n")
    tournament_location = validate_string_input("\nEntrez le lieu du tournoi : \n")
    tournament_number_of_players = validate_number_of_players_input(
        "\nEntrez le nombre de joueurs du tournoi :\n",
    )
    tournament_description = validate_string_input(
        "\nEntrez une description du tournoi :\n"
    )
    print("\n\nLe nombre de tours est généralement de 4.\n")
    tournament_number_of_rounds = validate_integer_input(
        "Entrez le nombre de tours du tournoi : \n", 4, 8
    )

    tournament_info = {
        "tournament_name": tournament_name,
        "tournament_location": tournament_location,
        "tournament_number_of_players": tournament_number_of_players,
        "tournament_description": tournament_description,
        "tournament_number_of_rounds": tournament_number_of_rounds,
    }

    return tournament_info


def create_add_players_to_tournament(tournament_id: int) -> bool:
    """
    Add players to a tournament in the database.

    This function guides the user through the process of adding players to a tournament.
    It checks if the desired number of players has been added and allows the user to
    input player information or select from existing players in the database.
    """

    print("Nous allons maintenant ajouter les joueurs participant au tournoi.\n")

    tournament_number_of_players = Tournament.get_tournaments_infos_from_db(
        tournament_id
    )["number_of_players"]
    players_ine_list = Tournament.get_tournaments_infos_from_db(tournament_id)[
        "players"
    ]

    while int(tournament_number_of_players) != len(players_ine_list):
        print(
            int(tournament_number_of_players) - len(players_ine_list),
            "joueur(s) restant(s) à ajouter au tournoi.\n",
        )
        want_to_add_player = validate_yes_no_input(
            "Voulez vous ajouter un joueur au tournoi ? (o/n)\n"
        )
        if not want_to_add_player:
            print("\nVous avez choisi de ne pas ajouter de joueur au tournoi.")
            break
        else:
            player_ine = validate_chess_national_identifier_input(
                "\nVeuillez entrer l'identifiant national d'échec du joueur :\n>"
            )

            if Tournament.does_player_exists_in_tournament_list(
                tournament_id, player_ine
            ):
                print("\nLe joueur est déjà inscrit dans le tournoi!")
                print("\nVeuillez entrer un autre identifiant.")
            elif Player.does_player_exists_in_db(player_ine):
                print("\nLe joueur existe dans la base de données!")
                is_player_to_add = validate_yes_no_input(
                    "\nVoulez vous bien l'ajouter au tournoi ? (o/n)\n"
                )
                if is_player_to_add:
                    Tournament.add_player_to_tournament(tournament_id, player_ine)
                    players_ine_list = Tournament.get_tournaments_infos_from_db(
                        tournament_id
                    )["players"]
                    print("\nLe joueur a été ajouté au tournoi.")
                else:
                    print("\nLe joueur n'a pas été ajouté au tournoi.")
            else:
                print("\nLe joueur n'existe pas dans la base de données!")
                is_player_to_create = validate_yes_no_input(
                    "\nVoulez vous bien le créer ? (o/n)\n"
                )
                if is_player_to_create:
                    display_player_creation_menu(player_ine)
                    Tournament.add_player_to_tournament(tournament_id, player_ine)
                    players_ine_list = Tournament.get_tournaments_infos_from_db(
                        tournament_id
                    )["players"]
                    print("\nLe joueur a été créé et ajouté au tournoi.")
                else:
                    print("\nLe joueur n'a pas été créé ni ajouté au tournoi.")

    if int(tournament_number_of_players) == len(players_ine_list):
        print("\nTous les joueurs ont été ajoutés au tournoi.")
        print("\nVoici la liste finale des ine des joueurs du tournoi :")
        # Pretty print the list of players
        table = []
        for player in players_ine_list:
            table.append([player])
        print(
            tabulate(
                table,
                headers=["INE des joueurs du tournoi"],
                tablefmt="double_outline",
                colalign=("center",),
            )
        )

    return want_to_add_player


def display_and_verify_tournament_info(tournament_id: int) -> bool:
    """
    This function displays the details of the tournament, including its name,
    location and start time.
    Check if the number of players registered to the tournament is equal to
    the number of players expected.
    If not, it calls the function create_add_players_to_tournament() to add
    the missing players.
    """
    tournament = Tournament.get_tournaments_infos_from_db(tournament_id)
    print(
        f"\nVous avez décidé de charger le tournoi {tournament['name']} à "
        f"{tournament['location']} qui a débuté le {tournament['start_time']}."
    )
    number_of_players = tournament["number_of_players"]
    players_registered_tournament = len(tournament["players"])

    while number_of_players != players_registered_tournament:
        print(
            "\nLe nombre de joueurs ajouté au tournoi n'est pas"
            " égal au nombre de joueurs attendu."
        )
        print(
            f"\nVoici le nombre de joueurs déjà inscrits au tournoi "
            f": {players_registered_tournament}"
        )
        want_to_continue = create_add_players_to_tournament(tournament_id)
        if not want_to_continue:
            break
        else:
            tournament = Tournament.get_tournaments_infos_from_db(tournament_id)
            number_of_players = tournament["number_of_players"]
            players_registered_tournament = len(tournament["players"])

    try:
        return want_to_continue
    except UnboundLocalError:
        return True


def display_all_tournaments() -> None:
    """Display all tournaments from database."""
    all_tournaments = Tournament.get_all_tournaments_from_db()
    table = []
    for tournament in all_tournaments:
        table.append([tournament[key] for key in tournament.keys()])
    print("\nVoici la liste de tous les tournois :")
    print(
        tabulate(
            table,
            headers=tournament.keys(),
            tablefmt="fancy_grid",
            maxcolwidths=[12, 12, 12, 12, 12, 12, 12, 12],
        )
    )


def display_tournament_name_and_dates(tournament_id) -> None:
    """Display the name and dates of a tournament."""
    tournament = Tournament.get_tournaments_infos_from_db(tournament_id)
    print("\nVoici le nom et les dates du tournoi :\n")
    print(f"Nom : {tournament['name']}")
    print(f"Date de début : {tournament['start_time']}")
    print(f"Date de fin : {tournament['end_time']}\n")
