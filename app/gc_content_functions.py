from os.path import join as os_path_join
from typing import Literal, Union
from collections import Counter

import matplotlib.pyplot as plt
from pydantic import validate_arguments

from app.constants import DNA_CONSTRAINT, RNA_CONSTRAINT
import app.config as config
from app.utils import custom_exception


@custom_exception
@validate_arguments
def calculate_gc_content(genomic_data: Union[DNA_CONSTRAINT, RNA_CONSTRAINT],
                         step: int = 100) -> list[float]:
    """Calculates G-C content metric for DNA subsequences with a given step"""
    gc_per_fragment = []

    for i in range(0, len(genomic_data), step):
        fragment = genomic_data[i:i+step]
        bases_frequency = Counter(fragment)
        gc_ratio = ((bases_frequency["G"] + bases_frequency["C"])
                    / len(fragment) * 100)
        gc_per_fragment.append(gc_ratio)

    return gc_per_fragment


def plot_gc_content(gc_per_fragment: list[float],
                    step: int,
                    file_format: Literal["png", "jpeg"] = "png",
                    filename: str = "gc_ratio_plot") -> None:
    """Plots graphic for G-C content metric and saves it as a file"""
    sequence_length = len(gc_per_fragment) * step
    fragment_start_position = [pos for pos in range(0, sequence_length, step)]

    figure, axis_x = plt.subplots()
    axis_x.set(title="GC-content (per fragment)",
               xlabel="Fragment start position",
               ylabel="GC-ratio, %",)
    axis_x.plot(fragment_start_position, gc_per_fragment)

    plt.savefig(os_path_join(config.SAVE_DIR, f"{filename}.{file_format}"))
