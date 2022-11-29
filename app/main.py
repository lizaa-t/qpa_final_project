import argparse

from app.genomic_functions.gene_expression import convert_dna_to_rna
from app.genomic_functions.gene_expression import convert_rna_to_protein
from app.genomic_functions.gc_content import calculate_gc_content
from app.genomic_functions.gc_content import plot_gc_content


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("input", metavar="INPUT", type=str,
                        help="The input DNA data")
arg_parser.add_argument("step", nargs="?", type=int, default=100,
                        help="The step for gc-content calculating")
arg_parser.add_argument("filename", nargs="?", type=str,
                        default="gc_ratio_plot",
                        help="The filename of a gc-content plot")


if __name__ == "__main__":
    args = arg_parser.parse_args()

    dna_sequence = args.input
    step = args.step
    filename = args.filename

    rna = convert_dna_to_rna(dna_sequence)
    protein = convert_rna_to_protein(rna)

    dna_gc = calculate_gc_content(dna_sequence, step)
    plot_gc_content(dna_gc, step, filename=filename)
