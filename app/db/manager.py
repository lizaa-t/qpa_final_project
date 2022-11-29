from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import Config


engine = create_engine(Config.DB_URI)
Session = sessionmaker(bind=engine)
Base = declarative_base()
