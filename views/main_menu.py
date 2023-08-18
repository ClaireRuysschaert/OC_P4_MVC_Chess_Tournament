import sys
from pathlib import Path
project_path = str(Path(__file__).parent.parent)
sys.path.insert(0, project_path)

from controllers.match import create_first_random_player_pairs, get_players_ine, create_match
from controllers.tournament import create_new_tournament
from controllers.round import create_new_round
from utils.input_validation import get_integer_input, get_chess_national_identifier_input
from views.match import get_matchs_score
from views.player import display_player_creation_menu
from views.tournament import get_tournament_info, check_all_players_created, create_add_players_to_tournament
from models.tournament_model import Tournament

def main_menu_display() -> None:  # NOSONAR
    """First users entry point where all the functionalities are listed."""
    
    while True:
        user_input = get_integer_input("\nQuelle action voulez vous réaliser ?\n\n"
                        "1 - Créer un tournoi\n"
                        "2 - Charger et jouer un tournoi\n"
                        "3 - Créer des joueurs\n"
                        "4 - Afficher les rapports\n"
                        "5 - Jouer un tournoi\n"
                        "6 - Créer un match\n"
                        "7 - Jouer un match\n"
                        "0 - Quitter\n\n> ", 0, 7)
    
        # 1 - Créer un tournoi
        if user_input == 1:
            # Récupérer les informations préliminaires du tournoi et les sauvegarder
            tournament_info = get_tournament_info()
            tournament_id = create_new_tournament(tournament_info)
            print(f"\nTournoi créé avec succès ! ID : {tournament_id}.")
            print("Veuillez vous le noter si vous voulez charger les informations de ce tournoi.\n")
            # Vérifier si les joueurs proposés par l'utilisateur sont à 
            # créer ou/et à ajouter au tournoi
            create_add_players_to_tournament(tournament_id)
            
        
        # 2 - Charger et jouer un tournoi
        elif user_input == 2:
            #TODO: charger le tournoi
            tournament_id = get_integer_input("Veuillez entrer l'ID du tournement à charger:\n", 1, 1000)
            tournament = Tournament.get_tournament_id_from_db(tournament_id)
            current_round_number = Tournament.get_current_round_number(tournament)
            create_new_round(tournament_id, current_round_number)
        
        # 3 - Créer un joueur
        elif user_input == 3:
            print("\nVous avez choisi de créer un joueur.\n")
            player_ine = get_chess_national_identifier_input("Veuillez entrer l'identifiant national d'échec du joueur à créer:\n>")
            display_player_creation_menu(player_ine)     
        
        # 4 - Afficher des rapports
        elif user_input == 4: 
            print("to be continued...")
            #afficher les résultats
            #mettre à jour le classement 
            
        # 5 - Jouer un tournoi
        elif user_input == 5:
            print("Créer un tournoi avec un controller.")
        
        # 6 - Créer le premier match
        elif user_input == 6:
            pair_players = create_first_random_player_pairs()
            if check_all_players_created():
                create_match(pair_players)
                
                print("Place aux matchs! Les joueurs suivant vont jouer l'un contre l'autre : \n")
                for pair in pair_players:
                    first_player = pair[0]["chess_national_identifier"]
                    second_player = pair[1]["chess_national_identifier"]
                    print(f"{first_player} versus {second_player}\n")
            
        # 7 - Jouer le premier round
        elif user_input == 7:
            pair_players = create_first_random_player_pairs()
            players_ine = get_players_ine(pair_players)
            scores_list = get_matchs_score(players_ine)
            print(scores_list)
            
        # Quitter
        else:
            quit()
    
main_menu_display()
