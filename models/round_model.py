import datetime
from models.match_model import Match

class Round:
    def __init__(self):
        """Initialise les informations d'un round."""
        self.start_time = self.get_time_now()
        self.end_time = ""
        self.matchs = self.create_match()

    def get_time_now(self):
        return datetime.datetime.now().strftime("%d %B %Y at %Hh%M")

    def create_match(self) -> list[Match]:
        matchs = []
        for index, pair in enumerate(self.pair_players):
            matchs.append(Match(name=f"Match {index}", pair_players=pair))
        return matchs

    def get_round_results(self):
        print("Round over! Please enter match results.")
        self.end_time = self.get_time_now

        for match in self.matchs:
            match.get_match_score()

    def __str__(self):
        return self.name