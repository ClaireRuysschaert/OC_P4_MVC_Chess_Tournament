from datetime import datetime
from models.tournament_model import Tournament
from models.match_model import Match

def validate_integer_input(prompt: str, min_value: int, max_value: int) -> int:
    """
    Prompt the user for an integer input within a specified range (min/max_values) and validate the input.
    If the input is valid, the function returns the integer. 
    If not, an error message is displayed, and the user is prompted again.
    """
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            if min_value <= value <= max_value:
                return value
            else:
                print(f"\nVeuillez enter un numéro entre {min_value} and {max_value}.\n")
        except ValueError:
            print("\nERREUR /!\ ")
            print("Veuillez entrer un numéro valide.\n")

def validate_string_input(prompt:str) -> str:
    """
    Prompt the user for a non-empty string input without spaces and validate the input.
    If the input is valid, the function returns the string without the spaces. 
    If not, an error message is displayed, and the user is prompted again.
    """
    while True:
        user_input = input(prompt)
        cleaned_input = user_input.strip()
        if cleaned_input:
            return cleaned_input
        else:
            print("Veuillez entrer un texte non vide.\n")          
           
def validate_chess_national_identifier_input(prompt: str) -> str:
    """
    Prompt the user for a chess national identifier and validate its format.
    The chess national identifier should consist of 2 letters followed by 5 digits.
    If the input is valid, the function returns the string without the spaces. 
    If not, an error message is displayed, and the user is prompted again.
    """
    while True:
        user_input = input(prompt)
        cleaned_input = user_input.strip()
        try:
            if len(cleaned_input) == 7 and cleaned_input[:2].isalpha() and cleaned_input[2:].isdigit():
                return user_input
            else:
                raise ValueError
        except ValueError:
            print("Veuillez entrer un numéro d'identifiant valide.\n")
            print("Il doit être composé de 2 lettres suivies de 5 chiffres.\n")
            print("Exemple : AB12345")

def validate_birthday_date_input(prompt: str) -> str:
    """
    Prompt the user for a birthday date in the French format (jj/mm/aaaa) and validate the input.
    If the input is valid, the function returns the formatted date. 
    If not, an error message is displayed, and the user is prompted again.
    """
    while True:
        user_input = input(prompt)
        cleaned_input = user_input.strip()
        try:
            datetime.strptime(cleaned_input, "%d/%m/%Y")
            return cleaned_input
        except ValueError:
            print("Veuillez entrer une date de naissance valide au format jj/mm/aaaa.\n")
            
def validate_yes_no_input(prompt: str) -> bool:
    """
    Prompt the user for a yes/no answer in the French format (o/n) and validate the input.
    If the input is valid, the function returns True for 'o' (yes) and False for 'n' (no). 
    If not, an error message is displayed, and the user is prompted again.
    """
    while True:
        user_input = input(prompt)
        cleaned_input = user_input.strip()
        if cleaned_input.lower() == 'o':
            return True
        elif cleaned_input.lower() == 'n':
            return False
        else:
            print("Veuillez répondre par 'o' (oui) ou 'n' (non).\n")

def validate_tournament_id_input(prompt: str) -> int:
    """
    Prompt the user for a tournament id and validate the input.
    If the input is valid, the function returns the tournament id (int). 
    If not, an error message is displayed, and the user is prompted again.
    """
    while True:
        user_input = input(prompt)
        tournament = Tournament.get_tournaments_infos_from_db(user_input)
        if tournament: 
            return int(user_input)
        else:
            print("\nLe numéro de tournoi n'existe pas.")
            print("Veuillez entrer un numéro de tournoi valide.\n")

def validate_match_id_input(prompt: str) -> int:
    """
    Prompt the user for a match id and validate the input.
    If the input is valid, the function returns the match id (int). 
    If not, an error message is displayed, and the user is prompted again.
    """
    while True:
        user_input = input(prompt)
        match = Match.get_match_info_from_db(user_input)
        if match: 
            return int(user_input)
        else:
            print("\nLe numéro de match n'existe pas.")
            print("Veuillez entrer un numéro de match valide.\n")