from typing import List, Tuple
from utils.input_validation import get_integer_input
def get_matchs_score(players_ine: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    """Get the match score by the user from pair players."""
    
    matchs_score: List[Tuple[str, float]] = []
    for player_ine in players_ine:
        #Ask to the user who have won the match for each pair
        winner_or_tie = get_integer_input(f"Qui a gagné le match ? Si c'est : \n"
        f" - {player_ine[0]}, tapez 1\n"
        f" - {player_ine[1]}, tapez 2\n"
        " - Un match nul, tapez 3.", 1, 3)
        
        # Save the score of each player in matchs_score list
        if winner_or_tie == 1:
            matchs_score.append((player_ine[0], 1))
            matchs_score.append((player_ine[1], 0))
        elif winner_or_tie == 2:
            matchs_score.append((player_ine[0], 0))
            matchs_score.append((player_ine[1], 1))
        elif winner_or_tie == 3:
            matchs_score.append((player_ine[0], 0.5))
            matchs_score.append((player_ine[1], 0.5))
        else:
            raise ValueError("Please a number between 1 and 3.")

    return matchs_score