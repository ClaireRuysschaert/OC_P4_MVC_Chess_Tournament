from controllers.match import create_match, update_matchs_score
from models.match_model import Match
from utils.input_validation import (validate_integer_input,
                                    validate_match_id_input)


def display_match_creation_menu(round_id: str, player_pairs: list[list[str]]) -> None:
    """Display the match creation menu."""
    print(f"Les joueurs suivant vont jouer l'un contre l'autre :")
    for i, pair in enumerate(player_pairs, start=1):
        player1, player2 = pair
        print(f"Match {i} : joueur 1, INE = {player1} versus joueur 2, INE = {player2}")
        match_id = create_match(round_id, player_pairs[i - 1])
        print(f"Match créé avec succès ! ID : {match_id}.")


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


def play_matches_and_update_scores() -> None:
    """
    Play matches and update scores in a tournament.

    This function allows the user to input match IDs, determine match winners,
    and update match scores accordingly. It continues the process until the user
    chooses to exit by entering match ID '0'.

    Returns:
        None
    """
    match_id = validate_match_id_input(
        "Veuillez entrer l'ID du match à jouer:\n",
    )
    while match_id != 0:
        match_winner = get_match_winner(match_id)
        update_matchs_score(match_id, match_winner)
        match_id = validate_match_id_input(
            "Veuillez entrer l'ID du match à jouer (0 pour quitter):\n",
        )
