from functools import cache as functools_cache

from app.db.models import Aminoacid, DNABase, RNABase, Codon
from app.db.manager import Session


@functools_cache
def dna_to_rna(nucleotide: str) -> str:
    """Retrieve RNA base by given DNA base"""
    with Session() as session:
        rna_base = session.query(RNABase.nucleobase).\
            join(DNABase, DNABase.rna_base_id == RNABase.id).\
            filter(DNABase.nucleobase == nucleotide).one().nucleobase
        return rna_base


@functools_cache
def codon_to_aminoacid(codon: str) -> str:
    """Retrieve aminoacid by given codon"""
    with Session() as session:
        aminoacid = session.query(Aminoacid.letter_code).\
            join(Codon, Codon.aminoacid_id == Aminoacid.id).\
            filter(Codon.trinucleotide == codon).one().letter_code
        return aminoacid
