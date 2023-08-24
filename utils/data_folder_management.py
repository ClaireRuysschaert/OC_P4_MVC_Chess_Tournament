import os

def create_data_folder_if_not_exists():
    """
    Create a data folder at the root directory path if it doesn't exist.
    """
    root_folder_path = os.path.join(os.getcwd(), "data")
    if not os.path.isdir(root_folder_path):
        os.mkdir(root_folder_path)