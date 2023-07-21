import datetime
import random
from models.round_model import Round


class Tournament:
    def __init__(
        self, name: str, place: str, players: list, number_of_rounds=4, description=""
    ):
        self.name = name
        self.place = place
        self.players = players
        self.start_time = self.get_time_now
        self.end_time = ""
        self.number_of_rounds = number_of_rounds
        self.round_list = []
        self.description = description

    def get_time_now(self):
        return datetime.datetime.now().strftime("%d %B %Y at %Hh%M")

    def __str__(self):
        return self.name

    def create_rounds(self, round_number):
        pair_players = self.assign_players_pairs(current_round=round_number)
        round = Round("Round " + str(round_number), pair_players)
        self.round_list.append(round)

    def assign_players_pairs(self, current_round_number):
        # First Round, players are shuffled randomly
        if current_round_number == 0:
            sorted_players = random.shuffle(self.players)
        # Other rounds, players are sorted by their scores
        else:
            sorted_players = sorted(
                self.players, key=lambda player: player.final_score, reverse=True
            )

            # If 2 final_scores are equal, assign competitors that haven't played together
            # for player in sorted_players:
            #     if player.final_score ==