from pydantic import validate_arguments

from app.db.queries import get_rna_base, get_aminoacid
from app.constants import CODON_LENGTH
from app.constants import DNA_CONSTRAINT, RNA_CONSTRAINT


@validate_arguments
def convert_dna_to_rna(dna_sequence: DNA_CONSTRAINT) -> str:
    """Converts DNA sequence into RNA"""
    rna_sequence = ""
    dna_sequence = dna_sequence.upper()
    for nucleotide in dna_sequence:
        rna_sequence += get_rna_base(nucleotide)

    return rna_sequence


@validate_arguments
def convert_rna_to_protein(rna_sequence: RNA_CONSTRAINT) -> str:
    """Converts RNA sequence into protein"""
    polypeptide = ""
    rna_sequence = rna_sequence.upper()

    for i in range(0, len(rna_sequence), CODON_LENGTH):
        codon = rna_sequence[i:i+CODON_LENGTH]
        if len(codon) == CODON_LENGTH:
            polypeptide += get_aminoacid(codon)

    return polypeptide
