from tinydb import TinyDB
import os

ROOT_FOLDER_NAME = "data"
database = TinyDB(os.path.join(ROOT_FOLDER_NAME, "players_and_match_data.json"))

# Create tables for players and matches
players_table = database.table('players')
matches_table = database.table('matches')
