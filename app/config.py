import os

APP_DIR = os.getenv("APP_DIR")
PROJECT_DIR = os.path.abspath(os.path.join(APP_DIR, os.pardir))

SAVE_DIR_NAME = "pic"
SAVE_DIR = os.path.join(PROJECT_DIR, SAVE_DIR_NAME)

DB_URI = f"sqlite:///{APP_DIR}/db/qpa_final_project.db"
