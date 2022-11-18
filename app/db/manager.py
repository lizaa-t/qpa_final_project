from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine(
    "sqlite:////home/liza/PycharmProjects/qpa_final_project/app/db/qpa_final_project.db",
    echo=True,
)
Session = sessionmaker(bind=engine)
Base = declarative_base()
