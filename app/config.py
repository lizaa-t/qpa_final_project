import os


class Config(object):
    APP_DIR = os.getenv("APP_DIR")
    PROJECT_DIR = os.path.abspath(os.path.join(APP_DIR, os.pardir))

    DATA_DIR_NAME = "data"

    PLOT_DIR_NAME = "pic"
    PLOT_DIR = os.path.join(PROJECT_DIR, DATA_DIR_NAME, PLOT_DIR_NAME)

    INPUT_DIR_NAME = "input"
    INPUT_DIR = os.path.join(PROJECT_DIR, DATA_DIR_NAME, INPUT_DIR_NAME)

    LOGS_DIR_NAME = "logs"
    LOGS_DIR = os.path.join(PROJECT_DIR, DATA_DIR_NAME, LOGS_DIR_NAME)

    DB_DIALECT = "postgresql"
    DB_DRIVER = "pg8000"
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = "db"
    # DB_HOST = "localhost"
    DB_PORT = "5432"
    DB_NAME = "genomic_db"
    DB_URI = (f"{DB_DIALECT}+{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@"
              f"{DB_HOST}:{DB_PORT}/{DB_NAME}")
