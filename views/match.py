
#TO DO : place to Round view!
from typing import Tuple


def all_players_created() -> bool:
    """Make sure that all the players are created by the user"""
    
    is_the_players_created = input("Avez-vous enregistré tous les joueurs participant au tournoi? (o/n)")
    
    if is_the_players_created == "n":
        print("Veuillez créer tous les joueurs participant au tournoi AVANT de créer un tour.")
        return False
    else:
        return True

def get_matchs_score(pair_players) -> None:
    """Get the match score by the user from pair players."""
    
    #Get the INE of each pair into pair_players list
    player_INE = []
    for pair in pair_players["pair_players"]:
        first_player_INE = pair[0]["chess_national_identifier"]
        second_player_INE = pair[1]["chess_national_identifier"]
        player_INE.append((first_player_INE, second_player_INE))

    #Ask to the user who have won the match for each pair
    
    # input = "Qui a gagné le premier match ? Si c'est : \n"
    #         f" - {player_INE}"
    
    
    
        # print(
        #     "Who have won the match ? If it's : \n"
        #     f" - {self.player_one}, type 1\n"
        #     f" - {self.player_two}, type 2\n"
        #     " - A tie, type 3."
        # )

        # match_winner = int(input())
        # if match_winner == 1:
        #     self.player_one_score += 1
        # if match_winner == 2:
        #     self.player_two_score += 1
        # if match_winner == 3:
        #     self.player_one_score += 0.5
        #     self.player_two_score += 0.5
        # else:
        #     print("Please a number between 1 and 3.")