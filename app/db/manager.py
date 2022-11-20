from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

import app.config as config


engine = create_engine(config.DB_URI)
Session = sessionmaker(bind=engine)
Base = declarative_base()
