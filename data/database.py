from tinydb import TinyDB
import os

ROOT_FOLDER_NAME = "data"
player_database = TinyDB(os.path.join(ROOT_FOLDER_NAME, "players_data.json"))
match_database = TinyDB(os.path.join(ROOT_FOLDER_NAME, "match_data.json"))