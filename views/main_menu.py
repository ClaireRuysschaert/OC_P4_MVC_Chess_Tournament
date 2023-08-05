import sys 
from pathlib import Path

project_path = str(Path(__file__).parent.parent)
sys.path.insert(0, project_path)

from views.player import get_new_player_info
from controllers.player import create_player 
from views.match import all_players_created, get_matchs_score
from controllers.match import create_first_random_player_pairs, create_match

def main_menu_display() -> None:
    """First users entry point where all the functionalities are listed."""
    
    while True:
        user_input = input("Que voulez vous faire ?\n"
                        "1 - Créer un tournoi\n"
                        "2 - Charger un tournoi\n"
                        "3 - Créer des joueurs\n"
                        #afficher tous les joueurs créés
                        "4 - Afficher les rapports\n"
                        "5 - Jouer un tournoi\n"
                        "6 - Créer un match\n"
                        "7 - Jouer un match\n"
                        "q - Quitter\n> ")
    
        # 1 - Créer un tournoi
        if user_input == "1":
            print("créer un tournoi avec le controller et une vue.")
        
        # 2 - Charger un tournoi
        elif user_input == "2":
            print("charger un tournoi avec le controller et une vue.")
        
        # 3 - Créer des joueurs
        elif user_input == "3":
            user_input = input("Entrez le nombre de joueurs à créer\n")
            
            for _ in range(int(user_input)):
                player_info = get_new_player_info()
                create_player(player_info) 
                
        
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
            if all_players_created():
                pair_players = create_first_random_player_pairs()
                create_match(pair_players)
                
                print("Place aux matchs! Les joueurs suivant vont jouer l'un contre l'autre : \n")
                for pair in pair_players["pair_players"]:
                    first_player = pair[0]["chess_national_identifier"]
                    second_player = pair[1]["chess_national_identifier"]
                    print(f"{first_player} versus {second_player}\n")
            
        # 7 - Jouer un match
        elif user_input == "7":
            pass
        #match_infos = get_matchs_score(pair_players)
            # couleur
            # récup résultats    
            
        # Quitter
        else:
            quit()
    
main_menu_display()
