import argparse
import logging
from os.path import join as os_path_join

from app.genomic_functions.gene_expression import convert_dna_to_rna
from app.genomic_functions.gene_expression import convert_rna_to_protein
from app.genomic_functions.gc_content import calculate_gc_content
from app.genomic_functions.gc_content import plot_gc_content
from app.file_reader import read_file
from app.config import Config


arg_parser = argparse.ArgumentParser()

arg_parser.add_argument(
    "input", metavar="INPUT", type=str,
    help="the input DNA sequence: as a string itself or as a filename. "
         "If filename is provided, must also provide '--file' option"
)
arg_parser.add_argument(
    "--step", type=int, default=100,
    help="the step for gc-content calculating (default: 100)"
)
arg_parser.add_argument(
    "--plot_filename", type=str, default="gc_ratio_plot",
    help="the filename of a gc-content plot (default: 'gc_ratio_plot')"
)
arg_parser.add_argument(
    "--file", action="store_true",
    help="specifies that DNA sequence must be read from <input> file"
)


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler(
    os_path_join(Config.LOGS_DIR, "app.log"),
    mode="a",
)
handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
handler.setFormatter(formatter)
logger.addHandler(handler)


if __name__ == "__main__":
    args = arg_parser.parse_args()
    logger.info("Start the app")
    logger.info(f"Call {arg_parser.prog} with arguments {vars(args)}")

    dna_sequence = read_file(args.input) if args.file else args.input
    step = args.step
    plot_filename = args.plot_filename

    rna = convert_dna_to_rna(dna_sequence)
    logger.info(f"Call convert_dna_to_rna({dna_sequence})")
    logger.info(f"Return: {rna}")

    protein = convert_rna_to_protein(rna)
    logger.info(f"Call convert_rna_to_protein({rna})")
    logger.info(f"Return: {protein}")

    dna_gc = calculate_gc_content(dna_sequence, step)
    logger.info(f"Call calculate_gc_content({dna_sequence}, {step})")
    logger.info(f"Return: {dna_gc}")

    plot_gc_content(dna_gc, step, filename=plot_filename)
    logger.info(
        f"Call plot_gc_content({dna_gc}, {step}, filename={plot_filename})"
    )
    logger.info("Return: None")
    logger.info(f"Check output file in {Config.PLOT_DIR}")

    logger.info("Stop the app")
