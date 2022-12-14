from app.db.models import Aminoacid, DNABase, RNABase, Codon
from app.db.manager import Base, Session, engine
from app.constants import TRANSLATION_STOP_SIGNAL


rna_bases = [
    RNABase(nucleobase="A"),
    RNABase(nucleobase="C"),
    RNABase(nucleobase="G"),
    RNABase(nucleobase="U"),
]

dna_bases = [
    DNABase(nucleobase="A", rna_base=rna_bases[0]),
    DNABase(nucleobase="C", rna_base=rna_bases[1]),
    DNABase(nucleobase="G", rna_base=rna_bases[2]),
    DNABase(nucleobase="T", rna_base=rna_bases[3]),
]

aminoacid_to_codons = {
    "A": ["GCU", "GCC", "GCA", "GCG", ],
    "C": ["UGU", "UGC", ],
    "D": ["GAU", "GAC", ],
    "E": ["GAA", "GAG", ],
    "F": ["UUU", "UUC", ],
    "G": ["GGU", "GGC", "GGA", "GGG", ],
    "H": ["CAU", "CAC", ],
    "I": ["AUU", "AUC", "AUA", ],
    "K": ["AAA", "AAG", ],
    "L": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG", ],
    "M": ["AUG", ],
    "N": ["AAU", "AAC", ],
    "P": ["CCU", "CCC", "CCA", "CCG", ],
    "Q": ["CAA", "CAG", ],
    "R": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG", ],
    "S": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC", ],
    "T": ["ACU", "ACC", "ACA", "ACG", ],
    "V": ["GUU", "GUC", "GUA", "GUG", ],
    "W": ["UGG", ],
    "Y": ["UAU", "UAC", ],
    TRANSLATION_STOP_SIGNAL: ["UAA", "UAG", "UGA", ],
}

aminoacids = []
codons = []

for aminoacid_letter in aminoacid_to_codons.keys():
    aminoacid = Aminoacid(letter_code=aminoacid_letter)
    aminoacids.append(aminoacid)

    codon_triplets = aminoacid_to_codons[aminoacid_letter]
    for triplet in codon_triplets:
        codon = Codon(trinucleotide=triplet, aminoacid=aminoacid)
        codons.append(codon)


def create_tables():
    """Creates tables from models.py"""
    Base.metadata.create_all(engine)


def fill_tables():
    """Fills tables with data"""
    data = rna_bases + dna_bases + aminoacids + codons
    with Session() as session:
        for item in data:
            session.add(item)
            session.commit()


def init_tables():
    """Creates and fills tables with data.
    Runs only once for DB initialization
    """
    create_tables()
    fill_tables()


if __name__ == "__main__":
    # run this script for DB initialization
    init_tables()
