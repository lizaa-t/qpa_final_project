from time import time

from app.gene_expression_functions import convert_dna_to_rna, convert_rna_to_protein
from app.gene_expression_functions_with_cache import convert_dna_to_rna as convert_dna_to_rna_cached
from app.gene_expression_functions_with_cache import convert_rna_to_protein as convert_rna_to_protein_cached


if __name__ == '__main__':
    start = time()
    assert convert_dna_to_rna('ATTTGGCTACTAACAATCTA') == 'AUUUGGCUACUAACAAUCUA'
    assert convert_dna_to_rna('GTTGTAATGGCCTACATTA') == 'GUUGUAAUGGCCUACAUUA'
    assert convert_dna_to_rna('CAGGTGGTGTTGTTCAGTT') == 'CAGGUGGUGUUGUUCAGUU'
    assert convert_dna_to_rna('GCTAACTAAC') == 'GCUAACUAAC'
    assert convert_dna_to_rna('GCTAACTAACATCTTTGGCACTGTT') == 'GCUAACUAACAUCUUUGGCACUGUU'
    assert convert_dna_to_rna('TATGAAAAACTCAAA') == 'UAUGAAAAACUCAAA'
    assert convert_dna_to_rna('CCCGTCCTTGATTGGCTTGAAGAGAAGTTT') == 'CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU'

    assert convert_rna_to_protein('AUUUGGCUACUAACAAUCUA') == 'IWLLTI'
    assert convert_rna_to_protein('GUUGUAAUGGCCUACAUUA') == 'VVMAYI'
    assert convert_rna_to_protein('CAGGUGGUGUUGUUCAGUU') == 'QVVLFS'
    assert convert_rna_to_protein('UAUGAAAAACUCAAA') == 'YEKLK'
    assert convert_rna_to_protein('CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU') == 'PVLDWLEEKF'
    assert convert_rna_to_protein('GCUAACUAAC') == 'AN.'
    assert convert_rna_to_protein('GCUAACUAACAUCUUUGGCACUGUU') == 'AN.HLWHC'
    end = time()
    no_cache = end - start

    start = time()
    assert convert_dna_to_rna_cached('ATTTGGCTACTAACAATCTA') == 'AUUUGGCUACUAACAAUCUA'
    assert convert_dna_to_rna_cached('GTTGTAATGGCCTACATTA') == 'GUUGUAAUGGCCUACAUUA'
    assert convert_dna_to_rna_cached('CAGGTGGTGTTGTTCAGTT') == 'CAGGUGGUGUUGUUCAGUU'
    assert convert_dna_to_rna_cached('GCTAACTAAC') == 'GCUAACUAAC'
    assert convert_dna_to_rna_cached('GCTAACTAACATCTTTGGCACTGTT') == 'GCUAACUAACAUCUUUGGCACUGUU'
    assert convert_dna_to_rna_cached('TATGAAAAACTCAAA') == 'UAUGAAAAACUCAAA'
    assert convert_dna_to_rna_cached('CCCGTCCTTGATTGGCTTGAAGAGAAGTTT') == 'CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU'

    assert convert_rna_to_protein_cached('AUUUGGCUACUAACAAUCUA') == 'IWLLTI'
    assert convert_rna_to_protein_cached('GUUGUAAUGGCCUACAUUA') == 'VVMAYI'
    assert convert_rna_to_protein_cached('CAGGUGGUGUUGUUCAGUU') == 'QVVLFS'
    assert convert_rna_to_protein_cached('UAUGAAAAACUCAAA') == 'YEKLK'
    assert convert_rna_to_protein_cached('CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU') == 'PVLDWLEEKF'
    assert convert_rna_to_protein_cached('GCUAACUAAC') == 'AN.'
    assert convert_rna_to_protein_cached('GCUAACUAACAUCUUUGGCACUGUU') == 'AN.HLWHC'
    end = time()
    cache = end - start

    print(f"Cache: {cache}")
    print(f"No cache: {no_cache}")

    # Cache: 0.08845710754394531
    # No cache: 0.45664429664611816

    # Cache: 0.049990177154541016
    # No cache: 0.2432999610900879

    # Cache: 0.05466890335083008
    # No cache: 0.21412992477416992
