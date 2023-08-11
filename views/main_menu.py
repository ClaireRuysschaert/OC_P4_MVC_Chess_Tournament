import sys
from pathlib import Path

project_path = str(Path(__file__).parent.parent)
sys.path.insert(0, project_path)

from controllers.match import create_first_random_player_pairs, get_players_ine, create_match
from controllers.tournament import create_new_tournament
from views.match import get_matchs_score
from views.player import display_player_creation_menu
from views.tournament import get_tournament_info, check_all_players_created, create_add_players_to_tournament


def main_menu_display() -> None:  # NOSONAR
    """First users entry point where all the functionalities are listed."""
    
    while True:
        user_input = input("Que voulez vous faire ?\n\n"
                        "1 - Créer un tournoi\n"
                        "2 - Charger un tournoi\n"
                        "3 - Créer des joueurs\n"
                        #afficher tous les joueurs créés
                        "4 - Afficher les rapports\n"
                        "5 - Jouer un tournoi\n"
                        "6 - Créer un match\n"
                        "7 - Jouer un match\n"
                        "q - Quitter\n\n> ")
    
        # 1 - Créer un tournoi
        if user_input == "1":
            # Récupérer les informations préliminaires du tournoi et les sauvegarder
            tournament_info = get_tournament_info()
            tournament_id = create_new_tournament(tournament_info)
            print(f"\nTournoi créé avec succès ! ID : {tournament_id}\n")
            # Vérifier si les joueurs proposés par l'utilisateur sont à 
            # créer ou/et à ajouter au tournoi
            create_add_players_to_tournament(tournament_id)
            #TODO: afficher les joueurs du tournoi
            #TODO: créer le round 1
            
        
        # 2 - Charger un tournoi
        elif user_input == "2":
            print("charger un tournoi avec le controller et une vue.")
        
        # 3 - Créer des joueurs
        elif user_input == "3":
            display_player_creation_menu()     
        
        # 4 - Afficher des rapports
        elif user_input == "4": 
            print("to be continued...")
            #afficher les résultats
            #mettre à jour le classement 
            
        # 5 - Jouer un tournoi
        elif user_input == "5":
            print("Créer un tournoi avec un controller.")
        
        # 6 - Créer le premier round
        elif user_input == "6":
            pair_players = create_first_random_player_pairs()
            if check_all_players_created():
                create_match(pair_players)
                
                print("Place aux matchs! Les joueurs suivant vont jouer l'un contre l'autre : \n")
                for pair in pair_players:
                    first_player = pair[0]["chess_national_identifier"]
                    second_player = pair[1]["chess_national_identifier"]
                    print(f"{first_player} versus {second_player}\n")
            
        # 7 - Jouer le premier round
        elif user_input == "7":
            pair_players = create_first_random_player_pairs()
            players_ine = get_players_ine(pair_players)
            scores_list = get_matchs_score(players_ine)
            print(scores_list)
            
        # Quitter
        else:
            quit()
    
main_menu_display()
