from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (
    Base,
    # Aminoacid, DNABase, RNABase, RNATriplet,
)


sqlite_engine = create_engine("sqlite:///qpa_final_project.db", echo=True)


class DBManager:
    def __init__(self, engine, base_class):
        self.engine = engine
        self.base_class = base_class
        self.session_class = sessionmaker(bind=self.engine)

    def create_tables(self):
        self.base_class.metadata.create_all(self.engine)

    def init_tables(self):
        pass

    def truncate_tables(self):
        pass


# db_manager = DBManager(sqlite_engine, Base)
# db_manager.create_tables()


# Base.metadata.create_all(sqlite_engine)
# Session = sessionmaker(bind=sqlite_engine)

# dna = DNABase(
#     base='T',
#     rna=RNABase(base='U')
# )

# triplet = RNATriplet(
#     triplet='GAG',
#     aminoacid=Aminoacid(aminoacid='E')
# )

# with Session() as session:
#     session.add(dna)
#     session.commit()

# with Session() as session:
#     session.add(triplet)
#     session.commit()

# with Session() as session:
#     for dna in session.query(DNABase).all():
#         print("\n\n", dna, "->", dna.rna, "\n\n")

# with Session() as session:
#     for t in session.query(RNATriplet).all():
#         print("\n\n", t, "->", t.aminoacid, "\n\n")

# with Session() as session:
#     session.query(DNABase).delete()
#     session.query(RNABase).delete()
#     session.commit()

# with Session() as session:
#     session.query(RNATriplet).delete()
#     session.query(Aminoacid).delete()
#     session.commit()

# with Session() as session:
#     print(len(session.query(DNABase).all()))
#     print(len(session.query(RNABase).all()))
#     print(len(session.query(RNATriplet).all()))
#     print(len(session.query(Aminoacid).all()))
