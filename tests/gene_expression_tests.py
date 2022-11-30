import unittest
from unittest.mock import patch

from parameterized import parameterized

from mock_db import mock_query_dna_to_rna, mock_query_rna_to_protein
from app.genomic_functions.gene_expression import convert_dna_to_rna
from app.genomic_functions.gene_expression import convert_rna_to_protein


@patch("app.genomic_functions.gene_expression.convert_to_rna_base",
       new=mock_query_dna_to_rna)
class TestDnaToRna(unittest.TestCase):
    @parameterized.expand([
        ("ATTTGGCTACTAACAATCTA", "AUUUGGCUACUAACAAUCUA", ),
        ("CCCGTCCTTGATTGGCTTGAAGAGAAGTTT", "CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU", ),
        ("GCTAACTAAC", "GCUAACUAAC", ),
    ])
    def test_correct_input(self, data, expected):
        actual = convert_dna_to_rna(data)
        self.assertEqual(actual, expected, f"Should be {expected}")

    @parameterized.expand([
        ("ABCDEFGHIJKLMNOP", ),
        ("AUUUGGCUACUAACAAUCUA", ),
        ("12345...", ),
    ])
    def test_wrong_letters(self, data):
        with self.assertRaises(Exception):
            convert_dna_to_rna(data)

    def test_empty_string(self):
        data = ""
        expected = ""
        actual = convert_dna_to_rna(data)
        self.assertEqual(actual, expected, f"Should be {expected}")

    def test_none_input(self):
        data = None
        with self.assertRaises(Exception):
            convert_dna_to_rna(data)

    @parameterized.expand([
        ("atttggctactaacaatcta", "AUUUGGCUACUAACAAUCUA"),
        ("AtttGGCTACTAACAATCTA", "AUUUGGCUACUAACAAUCUA"),
    ])
    def test_wrong_case(self, data, expected):
        actual = convert_dna_to_rna(data)
        self.assertEqual(actual, expected, f"Should be {expected}")

    # string spaces?
    # string \n and so on?


@patch("app.genomic_functions.gene_expression.convert_to_aminoacid",
       new=mock_query_rna_to_protein)
class TestRnaToProtein(unittest.TestCase):
    @parameterized.expand([
        ("CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU", "PVLDWLEEKF", ),
        ("GCUAACUAACAUCUUUGGCACUGUU", "AN.HLWHC", ),
        ("UAUGAAAAACUCAAA", "YEKLK", ),
    ])
    def test_correct_input(self, data, expected):
        actual = convert_rna_to_protein(data)
        self.assertEqual(actual, expected, f"Should be {expected}")

    @parameterized.expand([
        ("GCUAACUAAC", "AN", ),
        ("GCUAACUAACAUCUUUGGCACUGUU", "ANHLWHC", ),
    ])
    def test_for_stop_signal(self, data, expected):
        actual = convert_rna_to_protein(data)
        self.assertNotEqual(actual, expected, f"Should be {expected}")

    @parameterized.expand([
        ("ABCDEFGHIJKLMNOP", ),
        ("GCTAACTAAC", ),
        ("12345...", ),
    ])
    def test_wrong_letters(self, data):
        with self.assertRaises(Exception):
            convert_rna_to_protein(data)

    def test_empty_string(self):
        data = ""
        expected = ""
        actual = convert_rna_to_protein(data)
        self.assertEqual(actual, expected, f"Should be {expected}")

    def test_none_input(self):
        data = None
        with self.assertRaises(Exception):
            convert_rna_to_protein(data)

    @parameterized.expand([
        ("cccguccuugauuggcuugaagagaaguuu", "PVLDWLEEKF"),
        ("CCCguccuugauuGGcuugaagagaaguuu", "PVLDWLEEKF"),
    ])
    def test_wrong_case(self, data, expected):
        actual = convert_rna_to_protein(data)
        self.assertEqual(actual, expected, f"Should be {expected}")

    # string spaces?
    # string \n and so on?
    # codon


if __name__ == "__main__":
    unittest.main()
