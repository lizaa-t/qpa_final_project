from unittest.mock import Mock


STOP_SIGNAL = "."

dna_to_rna_base = {"A": "A", "C": "C", "G": "G", "T": "U", }

codon_to_aminoacid = {
    "UUU": "F",
    "CUU": "L",
    "AUU": "I",
    "GUU": "V",
    "UUC": "F",
    "CUC": "L",
    "AUC": "I",
    "GUC": "V",
    "UUA": "L",
    "CUA": "L",
    "AUA": "I",
    "GUA": "V",
    "UUG": "L",
    "CUG": "L",
    "AUG": "M",
    "GUG": "V",
    "UCU": "S",
    "CCU": "P",
    "ACU": "T",
    "GCU": "A",
    "UCC": "S",
    "CCC": "P",
    "ACC": "T",
    "GCC": "A",
    "UCA": "S",
    "CCA": "P",
    "ACA": "T",
    "GCA": "A",
    "UCG": "S",
    "CCG": "P",
    "ACG": "T",
    "GCG": "A",
    "UAU": "Y",
    "CAU": "H",
    "AAU": "N",
    "GAU": "D",
    "UAC": "Y",
    "CAC": "H",
    "AAC": "N",
    "GAC": "D",
    "UAA": STOP_SIGNAL,
    "CAA": "Q",
    "AAA": "K",
    "GAA": "E",
    "UAG": STOP_SIGNAL,
    "CAG": "Q",
    "AAG": "K",
    "GAG": "E",
    "UGU": "C",
    "CGU": "R",
    "AGU": "S",
    "GGU": "G",
    "UGC": "C",
    "CGC": "R",
    "AGC": "S",
    "GGC": "G",
    "UGA": STOP_SIGNAL,
    "CGA": "R",
    "AGA": "R",
    "GGA": "G",
    "UGG": "W",
    "CGG": "R",
    "AGG": "R",
    "GGG": "G",
}

mock_db = {
    "dna_to_rna_table": dna_to_rna_base,
    "rna_to_protein_table": codon_to_aminoacid,
}

mock_query_dna_to_rna = Mock(
    side_effect=lambda x: mock_db["dna_to_rna_table"][x]
)
mock_query_rna_to_protein = Mock(
    side_effect=lambda x: mock_db["rna_to_protein_table"][x]
)
