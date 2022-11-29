from os.path import join as os_path_join

import app.config as config


def read_file(filename):
    filepath = os_path_join(config.INPUT_DIR, filename)
    with open(filepath, 'r') as file:
        return file.read().replace("\n", "")
