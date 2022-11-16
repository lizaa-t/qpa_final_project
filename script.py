from collections import Counter

from data.db.queries import dna_to_rna, codon_to_aminoacid
from data.db.models import CODON_LENGTH


def convert_dna_to_rna(dna_sequence: str) -> str:
    """Converts DNA sequence into RNA"""
    rna_sequence = ""
    dna_sequence = dna_sequence.upper()

    for nucleotide in dna_sequence:
        rna_sequence += dna_to_rna(nucleotide)

    return rna_sequence


def convert_rna_to_protein(rna_sequence: str) -> str:
    """Converts RNA sequence into protein"""
    protein = ""
    rna_sequence = rna_sequence.upper()

    for i in range(0, len(rna_sequence), CODON_LENGTH):
        codon = rna_sequence[i:i+CODON_LENGTH]
        if len(codon) == CODON_LENGTH:
            protein += codon_to_aminoacid(codon)

    return protein


def calculate_gc_ratio(dna_sequence: str, step: int = 100) -> list[float]:
    """Calculates G-C content metric for DNA subsequences with a given step"""
    gc_metric = []

    for i in range(0, len(dna_sequence), step):
        subsequence = dna_sequence[i:i+step]
        base_frequency = Counter(subsequence)
        gc_ratio = (base_frequency["G"] + base_frequency["C"]) / len(subsequence) * 100
        gc_metric.append(gc_ratio)

    return gc_metric
