from os.path import join as os_path_join
from typing import Literal
from collections import Counter

import matplotlib.pyplot as plt


def calculate_gc_ratio(dna_sequence: str, step: int = 100) -> list[float]:
    """Calculates G-C content metric for DNA subsequences with a given step"""
    gc_metric = []

    for i in range(0, len(dna_sequence), step):
        subsequence = dna_sequence[i:i+step]
        base_frequency = Counter(subsequence)
        gc_ratio = (base_frequency["G"] + base_frequency["C"]) / len(subsequence) * 100
        gc_metric.append(gc_ratio)

    return gc_metric


def plot_gc_ratio(gc_metric: list[float],
                  step: int,
                  file_format: Literal["png", "jpeg"] = "png",
                  filename: str = "gc_ratio_plot") -> None:
    """Plots graphic for G-C content metric and saves it as a file"""
    x_values = [i + step for i in range(0, len(gc_metric)*step, step)]

    figure, axis_x = plt.subplots()
    axis_x.set(xlim=(0, x_values[-1]), xticks=x_values)
    axis_x.stackplot(x_values, gc_metric)

    plt.savefig(os_path_join("pic", f"{filename}.{file_format}"))
