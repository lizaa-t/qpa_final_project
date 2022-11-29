from os.path import join as os_path_join

from app.config import Config


def read_file(filename):
    filepath = os_path_join(Config.INPUT_DIR, filename)
    with open(filepath, 'r') as file:
        return file.read().replace("\n", "")
