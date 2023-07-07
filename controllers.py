import json
import os

def save_player_to_json(dict_to_save):
    ROOT_FOLDER_NAME = "players_data"
    root_folder_path = os.path.join(os.getcwd(), ROOT_FOLDER_NAME)
    if not os.path.isdir(root_folder_path):
        os.mkdir(root_folder_path)
    
    with open(os.path.join(ROOT_FOLDER_NAME, "player_json_file"), "w") as pjf:
        json.dump(dict_to_save, pjf, indent=4)