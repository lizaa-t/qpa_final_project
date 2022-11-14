from data.db.models import Aminoacid, DNABase, RNABase, RNATriplet, STOP_SIGNAL
from data.db.manager import Base, Session, engine


rna_bases = [
    RNABase(base="A"),
    RNABase(base="C"),
    RNABase(base="G"),
    RNABase(base="U"),
]

dna_bases = [
    DNABase(base="A", rna=rna_bases[0]),
    DNABase(base="C", rna=rna_bases[1]),
    DNABase(base="G", rna=rna_bases[2]),
    DNABase(base="T", rna=rna_bases[3]),
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
    STOP_SIGNAL: ["UAA", "UAG", "UGA", ],
}

aminoacids = []
rna_triplets = []

for aminoacid in aminoacid_to_codons.keys():
    amino = Aminoacid(aminoacid=aminoacid)
    aminoacids.append(amino)

    codons = aminoacid_to_codons[aminoacid]
    for codon in codons:
        triplet = RNATriplet(triplet=codon, aminoacid=amino)
        rna_triplets.append(triplet)


def create_tables():
    Base.metadata.create_all(engine)


def fill_tables():
    data = rna_bases + dna_bases + aminoacids + rna_triplets
    with Session() as session:
        for item in data:
            session.add(item)
            session.commit()


def init_tables():
    create_tables()
    fill_tables()


if __name__ == "__main__":
    init_tables()
