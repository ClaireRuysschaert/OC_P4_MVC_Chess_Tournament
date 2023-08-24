import sys
from pathlib import Path

project_path = str(Path(__file__).parent.parent)
sys.path.insert(0, project_path)

from controllers.round import create_new_round
from controllers.tournament import create_new_tournament
from models.tournament_model import Tournament
from models.match_model import Match
from utils.input_validation import (
    validate_chess_national_identifier_input,
    validate_integer_input, validate_tournament_id_input
)
from views.match import display_match_creation_menu, play_matches_and_update_scores
from views.player import display_player_creation_menu
from views.tournament import create_add_players_to_tournament, get_tournament_info


def main_menu_display() -> None:  # NOSONAR
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
            tournament_info = get_tournament_info()
            tournament_id = create_new_tournament(tournament_info)
            print(f"\nTournoi créé avec succès ! ID : {tournament_id}.")
            print(
                "Veuillez vous le noter si vous voulez charger les informations de ce tournoi.\n"
            )
            # Vérifier si les joueurs proposés par l'utilisateur sont à
            # créer ou/et à ajouter au tournoi
            create_add_players_to_tournament(tournament_id)

        # 2 - Charger et jouer un tournoi
        elif user_input == 2:
            tournament_id = validate_tournament_id_input(
                "Veuillez entrer l'ID du tournement à charger:\n")
            tournament = Tournament.get_tournaments_infos_from_db(tournament_id)
            print(f"Vous avez décidé de charger le tournoi {tournament['name']}.")
            
            # number of players must be equal to len of players list
            if tournament["number_of_players"] != len(tournament["players"]):
                print("\nLe nombre de joueurs ajouté au tournoi n'est pas égal au nombre de joueurs attendu.")
                print(f"\nVoici la liste des joueurs déjà inscrits :{tournament['players']}")
                create_add_players_to_tournament(tournament_id)
        
            
            # TODO: On ne veut pas forcément créer un round! Faire une condition, si le round n'existe pas, on le crée
            # Si le Round n'a pas toutes les informations de scores, on reste sur l'existant!
            current_round_number = Tournament.get_current_round_number(tournament)
            round_id, player_pairs = create_new_round(
                tournament_id, current_round_number
            )
            print(
                f"\nVoici les concurrents des matchs du round {current_round_number+1} !"
            )
            display_match_creation_menu(round_id, player_pairs)
            print(f"\nMaintenant, place aux matchs du round {current_round_number+1} !")
            play_matches_and_update_scores()
            
            all_matches_played = Match.does_all_matches_have_been_played(int(round_id))
            while not all_matches_played:
                print("\nTous les matchs n'ont pas encore été joués. Veuillez renseigner les informations manquantes.")
                play_matches_and_update_scores()
                all_matches_played = Match.does_all_matches_have_been_played(int(round_id))
            # TODO: le round id peut ne pas correspondre au round en cours (Round 1 mais id dans la db = 2)
            # Faire une pour vérifier si on doit créer un match, si oui, enumerate pour récupérer le match "en cours"
            print(f"\nTous les matchs du round en cours ont été joués !")
            
            # TODO: 7 - Créer le round suivant


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
