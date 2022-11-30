import unittest
from unittest.mock import patch

from parameterized import parameterized

from mock_db import mock_query_dna_to_rna, mock_query_rna_to_protein
from app.genomic_functions.gene_expression import convert_dna_to_rna
from app.genomic_functions.gene_expression import convert_rna_to_protein


@patch("app.genomic_functions.gene_expression.convert_to_rna_base",
       new=mock_query_dna_to_rna)
class TestDnaToRna(unittest.TestCase):
    """Test Case for DNA to RNA converting
    from app.genomic_functions.gene_expression.convert_dna_to_rna
    """
    @parameterized.expand([
        ("ATTTGGCTACTAACAATCTA", "AUUUGGCUACUAACAAUCUA", ),
        ("CCCGTCCTTGATTGGCTTGAAGAGAAGTTT", "CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU", ),
        ("GCTAACTAAC", "GCUAACUAAC", ),
    ])
    def test_correct_input(self, data, expected):
        """Tests whether DNA is correctly converted"""
        actual = convert_dna_to_rna(data)
        self.assertEqual(actual, expected, f"Should be {expected}")

    @parameterized.expand([
        ("ABCDEFGHIJKLMNOP", ),
        ("AUUUGGCUACUAACAAUCUA", ),
        ("12345...", ),
    ])
    def test_wrong_letters(self, data):
        """Tests output for incorrect input"""
        with self.assertRaises(Exception):
            convert_dna_to_rna(data)

    def test_empty_string(self):
        """Tests output for empty string"""
        data = ""
        expected = ""
        actual = convert_dna_to_rna(data)
        self.assertEqual(actual, expected, f"Should be {expected}")

    def test_none_input(self):
        """Tests output for None input"""
        data = None
        with self.assertRaises(Exception):
            convert_dna_to_rna(data)

    @parameterized.expand([
        ("atttggctactaacaatcta", "AUUUGGCUACUAACAAUCUA"),
        ("AtttGGCTACTAACAATCTA", "AUUUGGCUACUAACAAUCUA"),
    ])
    def test_wrong_case(self, data, expected):
        """Tests if letter case affects output"""
        actual = convert_dna_to_rna(data)
        self.assertEqual(actual, expected, f"Should be {expected}")


@patch("app.genomic_functions.gene_expression.convert_to_aminoacid",
       new=mock_query_rna_to_protein)
class TestRnaToProtein(unittest.TestCase):
    """Test Case for RNA to protein converting
    from app.genomic_functions.gene_expression.convert_rna_to_protein
    """
    @parameterized.expand([
        ("CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU", "PVLDWLEEKF", ),
        ("GCUAACUAACAUCUUUGGCACUGUU", "AN.HLWHC", ),
        ("UAUGAAAAACUCAAA", "YEKLK", ),
    ])
    def test_correct_input(self, data, expected):
        """Tests whether RNA is correctly converted"""
        actual = convert_rna_to_protein(data)
        self.assertEqual(actual, expected, f"Should be {expected}")

    @parameterized.expand([
        ("GCUAACUAAC", "AN", ),
        ("GCUAACUAACAUCUUUGGCACUGUU", "ANHLWHC", ),
    ])
    def test_for_stop_signal(self, data, expected):
        """Tests whether stop signal is treated correctly"""
        actual = convert_rna_to_protein(data)
        self.assertNotEqual(actual, expected, f"Should be {expected}")

    @parameterized.expand([
        ("ABCDEFGHIJKLMNOP", ),
        ("GCTAACTAAC", ),
        ("12345...", ),
    ])
    def test_wrong_letters(self, data):
        """Tests output for incorrect input"""
        with self.assertRaises(Exception):
            convert_rna_to_protein(data)

    def test_empty_string(self):
        """Tests output for empty string"""
        data = ""
        expected = ""
        actual = convert_rna_to_protein(data)
        self.assertEqual(actual, expected, f"Should be {expected}")

    def test_none_input(self):
        """Tests output for None input"""
        data = None
        with self.assertRaises(Exception):
            convert_rna_to_protein(data)

    @parameterized.expand([
        ("cccguccuugauuggcuugaagagaaguuu", "PVLDWLEEKF"),
        ("CCCguccuugauuGGcuugaagagaaguuu", "PVLDWLEEKF"),
    ])
    def test_wrong_case(self, data, expected):
        """Tests if letter case affects output"""
        actual = convert_rna_to_protein(data)
        self.assertEqual(actual, expected, f"Should be {expected}")


if __name__ == "__main__":
    unittest.main()
