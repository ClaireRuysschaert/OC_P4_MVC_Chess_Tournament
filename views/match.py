from controllers.match import (
    create_match,
    does_match_belongs_to_round,
    update_matchs_score,
)
from models.match_model import Match
from utils.input_validation import validate_integer_input, validate_match_id_input, validate_yes_no_input


def display_match_creation_menu(round_id: str, player_pairs: list[list[str]]) -> None:
    """Display the match creation menu."""
    print(f"Les joueurs suivant vont jouer l'un contre l'autre :")
    for i, pair in enumerate(player_pairs, start=1):
        player1, player2 = pair
        print(f"Match {i} : joueur 1, INE = {player1} versus joueur 2, INE = {player2}")
        match_id = create_match(round_id, player_pairs[i - 1])
        print(f"Match créé avec succès ! ID : {match_id}.\n")


def get_match_winner(match_id: int) -> int:
    """
    Display the match play menu.
    Return match score that the user have entered.
    1 means player one have won the match.
    2 means player two have won the match.
    3 means it's a tie.
    """
    match = Match.get_match_info_from_db(match_id)
    match_winner = validate_integer_input(
        f"Qui a gagné le match {match_id} ? Si c'est : \n"
        f" - {match['player_one']}, tapez 1\n"
        f" - {match['player_two']}, tapez 2\n"
        " - Un match nul, tapez 3.\n",
        1,
        3,
    )
    return match_winner


def play_matches_and_update_scores(current_round_id: str) -> None:
    """
    Play matches and update scores in a tournament.

    This function allows the user to input match IDs, it verifies if match belongs to
    the current round, determine match winners, and update match scores accordingly.
    It continues the process until the user chooses to exit by entering "n".

    Returns:
        None
    """
    want_to_continue = True
    while want_to_continue:
        match_id = validate_match_id_input(
            "Veuillez entrer l'ID du match à jouer\n",
        )
        if not does_match_belongs_to_round(current_round_id, match_id):
            print("Ce match n'appartient pas au round en cours.")
            print("Veuillez entrer un ID de match valide.")
        else:
            match_winner = get_match_winner(match_id)
            update_matchs_score(match_id, match_winner)
        want_to_continue = validate_yes_no_input(
            "Si vous voulez continuer à jouer les matchs, tapez 'o'. Sinon, tapez 'n'.\n"
        )

def does_all_matchs_informations_correct(round_id: str) -> bool:
    """
    Prompt the user to verify if all matches informations are correct.
    Display matchs informations and ask the user if they are correct.    
    """
    print("Veuillez vérifier que les informations des matchs sont correctes.")
    print(f"Voici les informations des matchs du round {round_id}:")
    matches = Match.get_all_matches_from_round_id(round_id)
    for match in matches:
        print(
            f"Match {match.doc_id} : {match['player_one']} a {match['player_one_score']} point(s) et {match['player_two']} a {match['player_two_score']} point(s).\n"
        )
    
    correct_matchs_infos = validate_integer_input("Si les informations sont correctes, tapez 1. Sinon, tapez 2.\n", 1, 2)
    if correct_matchs_infos == 1:
        return True
    else:
        return False
    
    
def ask_round_data_confirmation(round_id: str) -> bool:
    """Ask the user to confirm scores of all matches of a round."""
    
    if does_all_matchs_informations_correct(round_id):
        print("Merci d'avoir vérifié les informations des matchs.")
    else:
        print("Veuillez renseigner les informations erronées.")
        play_matches_and_update_scores(round_id)
        ask_round_data_confirmation(round_id)
    