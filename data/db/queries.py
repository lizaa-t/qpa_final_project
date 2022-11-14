from models import Aminoacid, DNABase, RNABase, RNATriplet, STOP_SIGNAL
from manager import Session


def dna_to_rna(nucleotide: str) -> str:
    with Session() as session:
        rna_base = session.query(RNABase.base).\
            join(DNABase, DNABase.rna_id == RNABase.id).\
            filter(DNABase.base == nucleotide).one().base
        return rna_base


if __name__ == "__main__":
    dna_to_rna("A")
    dna_to_rna("C")
    dna_to_rna("G")
    dna_to_rna("T")
