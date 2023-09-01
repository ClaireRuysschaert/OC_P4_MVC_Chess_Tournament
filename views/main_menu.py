import sys
from pathlib import Path

# Adds the project path to the system's path. This allows
# to import modules from the project.
project_path = str(Path(__file__).parent.parent)
sys.path.insert(0, project_path)

from controllers.match import update_players_score, update_ranking  # noqa: E402
from controllers.round import create_new_round  # noqa: E402
from controllers.tournament import (  # noqa: E402
    create_new_tournament,
    get_current_round_id,
    get_current_round_number,
)
from models.match_model import Match  # noqa: E402
from models.tournament_model import Tournament  # noqa: E402
from utils.input_validation import (  # noqa: E402
    validate_chess_national_identifier_input,
    validate_integer_input,
    validate_tournament_id_input,
    validate_yes_no_input,
)
from views.match import (  # noqa: E402
    ask_round_data_confirmation,
    display_match_creation_menu,
    play_matches_and_update_scores,
)
from views.player import display_player_creation_menu  # noqa: E402
from views.tournament import (  # noqa: E402
    create_add_players_to_tournament,
    display_and_verify_tournament_info,
    get_tournament_info_from_user,
)


def main_menu_display() -> None:
    """First users entry point where all the functionalities are listed."""

    while True:
        user_input = validate_integer_input(
            "\nQuelle action voulez vous réaliser ?\n\n"
            "1 - Créer un tournoi\n"
            "2 - Charger et jouer un tournoi\n"
            "3 - Créer des joueurs\n"
            "4 - Afficher les rapports\n"
            "0 - Quitter\n\n> ",
            0,
            4,
        )

        # 1 - Créer un tournoi
        if user_input == 1:
            # Récupérer les informations préliminaires du tournoi et les sauvegarder
            tournament_info = get_tournament_info_from_user()
            tournament_id = create_new_tournament(tournament_info)
            print(f"\nTournoi créé avec succès ! ID : {tournament_id}.")
            print(
                "Veuillez vous le noter si vous voulez charger les informations"
                "de ce tournoi.\n"
            )
            # Vérifier si les joueurs proposés par l'utilisateur sont à
            # créer ou/et à ajouter au tournoi
            create_add_players_to_tournament(tournament_id)

        # 2 - Charger et jouer un tournoi
        elif user_input == 2:
            tournament_id = validate_tournament_id_input(
                "Veuillez entrer l'ID du tournoi à charger:\n"
            )
            if not display_and_verify_tournament_info(tournament_id):
                break
            else:
                current_round_number = get_current_round_number(tournament_id)
                tournament_number_of_round = Tournament.get_tournaments_infos_from_db(
                    tournament_id
                )["number_of_rounds"]
                # Tant que le current_round_number est inférieur au nombre de round du
                # tournoi attendu -> on veut pouvoir créer un nouveau round
                while (
                    current_round_number < tournament_number_of_round
                    or not Match.does_all_matches_have_been_played(
                        get_current_round_id(tournament_id)
                    )
                    is True
                ):
                    if (
                        current_round_number == 0
                        or Match.does_all_matches_have_been_played(
                            get_current_round_id(tournament_id)
                        )
                        is True
                    ):
                        (
                            current_round_id,
                            player_pairs,
                            new_round_number,
                        ) = create_new_round(tournament_id, current_round_number)
                        print(
                            f"\nVoici les concurrents des matchs du round"
                            f" {new_round_number} !"
                        )
                        display_match_creation_menu(current_round_id, player_pairs)
                        print(
                            f"\nMaintenant, place aux matchs du round {new_round_number} !"
                        )
                    want_to_play = validate_yes_no_input(
                        "Si vous voulez jouer les matchs, tapez 'o'. Sinon, tapez 'n'.\n>"
                    )
                    if want_to_play:
                        current_round_id = get_current_round_id(tournament_id)
                        match_id = Match.does_all_matches_have_been_played(
                            current_round_id
                        )
                        print(
                            f"Le(s) match(s) {', '.join(match_id)} n'a(ont) pas été joué(s)."
                        )
                        play_matches_and_update_scores(current_round_id)
                        if Match.does_all_matches_have_been_played(current_round_id):
                            ask_round_data_confirmation(current_round_id)
                            update_players_score(current_round_id)
                            update_ranking(tournament_id)
                            current_round_number = get_current_round_number(
                                tournament_id
                            )
                    else:
                        print("A bientôt !")
                        break

                if (
                    current_round_number == tournament_number_of_round
                    and Match.does_all_matches_have_been_played(
                        get_current_round_id(tournament_id)
                    )
                    is True
                ):
                    print("Le tournoi est terminé !")

        # 3 - Créer un joueur
        elif user_input == 3:
            print("\nVous avez choisi de créer un joueur.\n")
            player_ine = validate_chess_national_identifier_input(
                "Veuillez entrer l'identifiant national d'échec du joueur à créer:\n>"
            )
            display_player_creation_menu(player_ine)

        # 4 - Afficher des rapports
        elif user_input == 4:
            print("to be continued...")
            # afficher les résultats
            # mettre à jour le classement

        # Quitter
        else:
            quit()


main_menu_display()
