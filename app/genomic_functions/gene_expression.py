from app.db.queries import convert_to_rna_base, convert_to_aminoacid
from app.constants import CODON_LENGTH


def convert_dna_to_rna(dna_sequence: str) -> str:
    """Converts DNA sequence into RNA"""
    rna_sequence = ""
    dna_sequence = dna_sequence.upper()
    for nucleotide in dna_sequence:
        rna_sequence += convert_to_rna_base(nucleotide)

    return rna_sequence


def convert_rna_to_protein(rna_sequence: str) -> str:
    """Converts RNA sequence into protein"""
    polypeptide = ""
    rna_sequence = rna_sequence.upper()

    for i in range(0, len(rna_sequence), CODON_LENGTH):
        codon = rna_sequence[i:i+CODON_LENGTH]
        if len(codon) == CODON_LENGTH:
            polypeptide += convert_to_aminoacid(codon)

    return polypeptide
