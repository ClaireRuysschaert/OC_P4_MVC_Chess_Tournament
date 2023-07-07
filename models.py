import random
import datetime

class Player:
    def __init__(
        self,
        first_name: str,
        name: str,
        birthdate: str,
        tournament_score=0,
        final_score=0,
        rank=0,
        chess_national_identifier="",
    ):
        """Initialise les informations du joueur."""
        self.first_name = first_name
        self.name = name
        self.birthdate = birthdate
        self.ine = chess_national_identifier
        self.tournament_score = tournament_score
        self.final_score = final_score
        self.rank = rank
        self.met_competitors = []

    def __str__(self):
        return f"Player {self.first_name} {self.name} ranking is {self.rank} with {self.final_score} points."


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


class Round:
    def __init__(self, name:str, pair_players: list):
        """Initialise les informations d'un round."""
        self.name = name
        self.pair_players = pair_players
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


class Tournament():
    def __init__(self, name:str, place:str, players:list, number_of_rounds=4, description=""):
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
            sorted_players = sorted(self.players, key=lambda player: player.final_score, reverse=True)

            # If 2 final_scores are equal, assign competitors that haven't played together
            # for player in sorted_players:
            #     if player.final_score == 
