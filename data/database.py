import os

from tinydb import TinyDB

ROOT_FOLDER_NAME = "data"
database = TinyDB(os.path.join(ROOT_FOLDER_NAME, "database.json"))

# Create tables for players, matches, rounds and tournaments
players_table = database.table("players")
matches_table = database.table("matches")
rounds_table = database.table("rounds")
tournaments_table = database.table("tournaments")
