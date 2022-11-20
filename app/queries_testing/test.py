from time import time

from app.gene_expression_functions import convert_dna_to_rna, convert_rna_to_protein
from app.gene_expression_functions_with_cache import convert_dna_to_rna as convert_dna_to_rna_cached
from app.gene_expression_functions_with_cache import convert_rna_to_protein as convert_rna_to_protein_cached


if __name__ == '__main__':
    N = 10
    cached_time = []
    not_cached_time = []

    for _ in range(N):
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

        cached_time.append(cache)
        not_cached_time.append(no_cache)

    cached_time_avg = sum(cached_time) / N
    not_cached_time_avg = sum(not_cached_time) / N

    # N = 10
    # Cache avg: 0.005142641067504883
    # No cache avg: 0.24462802410125734
    # N = 100
    # Cache avg: 0.00033627986907958985
    # No cache avg: 0.14937709093093873
    print(f"Cache avg: {cached_time_avg}")
    print(f"No cache avg: {not_cached_time_avg}")
