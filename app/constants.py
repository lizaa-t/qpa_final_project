from pydantic import constr


TRANSLATION_STOP_SIGNAL = "."
CODON_LENGTH = 3

DNA_BASES = ("A", "C", "G", "T")
RNA_BASES = ("A", "C", "G", "U")

# determines string consisting only from DNA_BASES: as a whole, ignoring case
DNA_CONSTRAINT = constr(regex=f"(?i)^[{', '.join(DNA_BASES)}]+$")
# same for RNA
RNA_CONSTRAINT = constr(regex=f"(?i)^[{', '.join(RNA_BASES)}]+$")
