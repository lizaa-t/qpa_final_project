from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.manager import Base


class DNABase(Base):
    __tablename__ = "dna_bases"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    nucleobase = Column(String(1))
    rna_base = relationship("RNABase", back_populates="dna_base")
    rna_base_id = Column(Integer, ForeignKey("rna_bases.id"))

    def __str__(self):
        return f"DNABase(id={self.id}, base={self.nucleobase})"


class RNABase(Base):
    __tablename__ = "rna_bases"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    nucleobase = Column(String(1))
    dna_base = relationship("DNABase", back_populates="rna_base")

    def __str__(self):
        return f"RNABase(id={self.id}, base={self.nucleobase})"


class Codon(Base):
    __tablename__ = "rna_triplets"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    trinucleotide = Column(String(3))
    aminoacid = relationship("Aminoacid", back_populates="codon")
    aminoacid_id = Column(Integer, ForeignKey("aminoacids.id"))

    def __str__(self):
        return f"Codon(id={self.id}, triplet={self.trinucleotide})"


class Aminoacid(Base):
    __tablename__ = "aminoacids"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    letter_code = Column(String(1))
    codon = relationship("Codon", back_populates="aminoacid")

    def __str__(self):
        return f"Aminoacid(id={self.id}, aminoacid={self.letter_code})"
