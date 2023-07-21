from models.player_model import Player
import random

class Match:
    def __init__(self, name: str, pair_players: list[Player]):
        """Initialise les informations d'un match."""
        self.name = name
        self.player_one = pair_players[0]
        self.player_two = pair_players[1]
        self.player_one_color = ""
        self.player_two_color = ""
        self.player_one_score = 0
        self.player_two_score = 0

    def __repr__(self):
        """Tuple with 2 lists of 2 elements : players and score"""
        return (
            [self.player_one, self.player_one_score],
            [self.player_two, self.player_two_score],
        )

    def set_chess_piece_color(self):
        """Randomly assign color chess piece for players."""
        colors = ["white", "black"]
        random.shuffle(colors)
        self.player_one_color = colors[0]
        self.player_two_color = colors[1]

    def get_match_score(self):
        self.set_chess_piece_color()

        # Change with the view later
        print(
            "Who have won the match ? If it's : \n"
            f" - {self.player_one}, type 1\n"
            f" - {self.player_two}, type 2\n"
            " - A tie, type 3."
        )

        match_winner = int(input())
        if match_winner == 1:
            self.player_one_score += 1
        if match_winner == 2:
            self.player_two_score += 1
        if match_winner == 3:
            self.player_one_score += 0.5
            self.player_two_score += 0.5
        else:
            print("Please a number between 1 and 3.")

        # MAJ match score in player's tournament score
        self.player_one.tournament_score += self.player_one_score
        self.player_two.tournament_score += self.player_two_score
