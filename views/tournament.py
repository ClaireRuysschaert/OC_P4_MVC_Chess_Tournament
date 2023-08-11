from models.player_model import Player
from models.tournament_model import Tournament
from views.player import display_player_creation_menu

def get_tournament_info() -> dict:
    """Get the tournament informations from the user."""

    tournament_name = input("\nEntrez le nom du tournoi : \n")
    tournament_location = input("\nEntrez le lieu du tournoi : \n")
    tournament_number_of_players = input(
        "\nEntrez le nombre de joueurs du tournoi :\n"
    )
    tournament_description = input("\nEntrez une description du tournoi :\n")
    print("\n\nLe nombre de tours est fixé à 4.\n")
    tournament_number_of_rounds = input(
        "Entrez le nombre de tours du tournoi : \n"
    )

    tournament_info = {
        "tournament_name": tournament_name,
        "tournament_location": tournament_location,
        "tournament_number_of_players": tournament_number_of_players,
        "tournament_description": tournament_description,
        "tournament_number_of_rounds": tournament_number_of_rounds,
    }

    return tournament_info


def check_all_players_created() -> bool:
    """Return True if the user have already created all the player."""

    print("Vérification des joueurs créés...")
    players_in_db = Player.get_all_players_created_in_db()
    for player in players_in_db:
        print(
            player["first_name"],
            player["name"],
            player["chess_national_identifier"],
        )
    is_the_players_created = input(
        "Avez-vous enregistré tous les joueurs participant au tournoi? (o/n)"
    )
    while is_the_players_created not in ["o", "n"]:
        is_the_players_created = input("Veuillez répondre par o ou n")
    if is_the_players_created == "n":
        return False
    else:
        return True

def create_add_players_to_tournament(tournament_id: int) -> None:
    """Add players to a tournament in the database."""

    print("Nous allons maintenant ajouter les joueurs participant au tournoi.\n")

    tournament_number_of_players = Tournament.get_tournaments_infos_from_db(tournament_id)["number_of_players"]
    players_list = Tournament.get_tournaments_infos_from_db(tournament_id)["players"]
    
    while int(tournament_number_of_players) != len(players_list):
    #for _ in range(int(tournament_number_of_players)+2):
        player_ine = input("\nVeuillez entrer l'identifiant national d'échec du joueur :\n>")
        if Tournament.does_player_exists_in_tournament_list(tournament_id, player_ine):
            print("\nLe joueur est déjà inscrit dans le tournoi!")
            print("\nVeuillez entrer un autre identifiant.")
        elif Player.does_player_exists_in_db(player_ine):
            print("\nLe joueur existe dans la base de données!")
            is_player_to_add = input("\nVoulez vous bien l'ajouter au tournoi ? (o/n)\n")
            if is_player_to_add == "o":
                Tournament.add_player_to_tournament(tournament_id, player_ine)
                print("\nLe joueur a été ajouté au tournoi.")
            else:
                print("\nLe joueur n'a pas été ajouté au tournoi.")     
        else:
            print("\nLe joueur n'existe pas dans la base de données!")
            is_player_to_create = input("\nVoulez vous bien le créer ? (o/n)\n")
            if is_player_to_create == "o":
                display_player_creation_menu(player_ine)
                Tournament.add_player_to_tournament(tournament_id, player_ine)
                print("\nLe joueur a été créé et ajouté au tournoi.")
            else:
                print("\nLe joueur n'a pas été créé ni ajouté au tournoi.")
