from models import Aminoacid, DNABase, RNABase, RNATriplet, STOP_SIGNAL
from manager import Session


def dna_to_rna(nucleotide: str) -> str:
    with Session() as session:
        rna_base = session.query(RNABase.base).\
            join(DNABase, DNABase.rna_id == RNABase.id).\
            filter(DNABase.base == nucleotide).one().base
        return rna_base


def codon_to_aminoacid(codon: str) -> str:
    with Session() as session:
        aminoacid = session.query(Aminoacid.aminoacid).\
            join(RNATriplet, RNATriplet.aminoacid_id == Aminoacid.id).\
            filter(RNATriplet.triplet == codon).one().aminoacid
        return aminoacid
