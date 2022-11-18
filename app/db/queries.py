from app.db.models import Aminoacid, DNABase, RNABase, RNATriplet
from app.db.manager import Session


def dna_to_rna(nucleotide: str) -> str:
    """Retrieve RNA base by given DNA base"""
    with Session() as session:
        rna_base = session.query(RNABase.base).\
            join(DNABase, DNABase.rna_id == RNABase.id).\
            filter(DNABase.base == nucleotide).one().base
        return rna_base


def codon_to_aminoacid(codon: str) -> str:
    """Retrieve aminoacid by given codon"""
    with Session() as session:
        aminoacid = session.query(Aminoacid.aminoacid).\
            join(RNATriplet, RNATriplet.aminoacid_id == Aminoacid.id).\
            filter(RNATriplet.triplet == codon).one().aminoacid
        return aminoacid
