import argparse

from app.genomic_functions.gene_expression import convert_dna_to_rna
from app.genomic_functions.gene_expression import convert_rna_to_protein
from app.genomic_functions.gc_content import calculate_gc_content
from app.genomic_functions.gc_content import plot_gc_content
from app.file_reader import read_file


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("input", metavar="INPUT", type=str,
                        help="the input DNA sequence; "
                             "itself as a string or as a filename")
arg_parser.add_argument("step", nargs="?", type=int, default=100,
                        help="the step for gc-content calculating")
arg_parser.add_argument("plot_filename", nargs="?", type=str,
                        default="gc_ratio_plot",
                        help="the filename of a gc-content plot")
arg_parser.add_argument("--file", action="store_true",
                        help="DNA sequence must be read from input file "
                             "<input>")


if __name__ == "__main__":
    args = arg_parser.parse_args()

    dna_sequence = read_file(args.input) if args.file else args.input
    step = args.step
    plot_filename = args.plot_filename

    rna = convert_dna_to_rna(dna_sequence)
    protein = convert_rna_to_protein(rna)

    dna_gc = calculate_gc_content(dna_sequence, step)
    plot_gc_content(dna_gc, step, filename=plot_filename)
