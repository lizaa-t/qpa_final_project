from os.path import join as os_path_join

from app.config import Config


def read_file(filename: str) -> str:
    """Returns genomic sequence from file as a string.
    Supports simple .txt files and .FASTA ones
    """
    filepath = os_path_join(Config.INPUT_DIR, filename)
    with open(filepath, 'r') as file:
        sequence = ""
        for line in file:
            if line.startswith(">") or line.startswith(";"):
                continue
            sequence += line.strip()
        return sequence
