from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.manager import Base

STOP_SIGNAL = "."
CODON_LENGTH = 3


class DNABase(Base):
    __tablename__ = "dna_bases"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    base = Column(String(1))
    rna = relationship("RNABase", back_populates="dna")
    rna_id = Column(Integer, ForeignKey("rna_bases.id"))

    def __str__(self):
        return f"DNABase(id={self.id}, base={self.base})"


class RNABase(Base):
    __tablename__ = "rna_bases"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    base = Column(String(1))
    dna = relationship("DNABase", back_populates="rna")

    def __str__(self):
        return f"RNABase(id={self.id}, base={self.base})"


class RNATriplet(Base):
    __tablename__ = "rna_triplets"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    triplet = Column(String(3))
    aminoacid = relationship("Aminoacid", back_populates="rna_triplet")
    aminoacid_id = Column(Integer, ForeignKey("aminoacids.id"))

    def __str__(self):
        return f"RNATriplet(id={self.id}, triplet={self.triplet})"


class Aminoacid(Base):
    __tablename__ = "aminoacids"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    aminoacid = Column(String(1))
    rna_triplet = relationship("RNATriplet", back_populates="aminoacid")

    def __str__(self):
        return f"Aminoacid(id={self.id}, aminoacid={self.aminoacid})"
