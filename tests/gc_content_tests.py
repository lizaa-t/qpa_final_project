import os
import shutil
import unittest
from unittest.mock import patch
from math import isclose as math_is_close
from itertools import zip_longest

from parameterized import parameterized

from app.genomic_functions.gc_content import calculate_gc_content
from app.genomic_functions.gc_content import plot_gc_content


class TestGcCalculation(unittest.TestCase):
    @parameterized.expand([
        ("ATTTGGCTACTAACAATCTA", 5, [20.0, 60.0, 20.0, 20.0], ),
    ])
    def test_calculation(self, sequence, step, expected):
        actual = calculate_gc_content(sequence, step)
        compare_floats = all(
            math_is_close(a, b)
            for a, b in zip_longest(actual, expected, fillvalue=0)
        )
        self.assertTrue(compare_floats, f"Should be {expected}. Got {actual}")

    def test_empty_sequence(self):
        sequence = ""
        expected = []
        actual = calculate_gc_content(sequence)
        self.assertEqual(actual, expected)

    def test_none_input(self):
        sequence = None
        with self.assertRaises(Exception):
            calculate_gc_content(sequence)

    @parameterized.expand([
        ("ATTTGGCTACTAACAATCTA", 5, 4, ),
        ("ATTTGGCTACTAACAATCTATT", 5, 5, ),
    ])
    def test_input_bining(self, sequence, step, expected):
        actual = len(calculate_gc_content(sequence, step))
        self.assertEqual(actual,
                         expected,
                         f"Num of bins should be {expected}. Got {actual}")


CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
TEMP_FILES_DIR = os.path.join(CURRENT_DIR, "temp_files")


@patch("app.genomic_functions.gc_content.Config.PLOT_DIR",
       new=TEMP_FILES_DIR)
class TestGcPlot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.mkdir(TEMP_FILES_DIR)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(TEMP_FILES_DIR)

    def test_default_filename(self):
        default_filename = "gc_ratio_plot.png"

        calculated = [20.0, 60.0, 20.0, 20.0]
        step = 5

        plot_gc_content(calculated, step)
        self.assertTrue(
            os.path.exists(os.path.join(TEMP_FILES_DIR, default_filename))
        )

    def test_custom_filename(self):
        custom_name = "plot"
        custom_format = "jpeg"
        custom_filename = f"{custom_name}.{custom_format}"

        calculated = [20.0, 60.0, 20.0, 20.0]
        step = 5

        plot_gc_content(calculated, step, custom_format, custom_name)
        self.assertTrue(
            os.path.exists(os.path.join(TEMP_FILES_DIR, custom_filename))
        )


if __name__ == "__main__":
    unittest.main()
