import pytest

from ensembl_map.utils import (
    collapse_seq_change,
    expand_nt,
    expand_pep,
    format_hgvs_position,
    is_deletion,
    is_delins,
    is_duplication,
    is_frameshift,
    is_insertion,
    is_substitution,
    reverse_complement,
    reverse_translate,
    split_by_codon,
    split_insertion,
    split_seq_change,
    strip_version,
)


def test_collapse_seq_change():
    assert collapse_seq_change("GGT", "GTT") == ("G", "T", 1, 1)  # substitution
    assert collapse_seq_change("GTT", "CTT") == ("G", "C", 0, 2)  # substitution
    assert collapse_seq_change("TTG", "TTA") == ("G", "A", 2, 0)  # substitution
    assert collapse_seq_change("ATG", "A") == ("TG", "", 1, 0)  # deletion
    assert collapse_seq_change("ATTTA", "AA") == ("TTT", "", 1, 1)  # deletion
    assert collapse_seq_change("AATTTC", "AAC") == ("TTT", "", 2, 1)  # deletion
    assert collapse_seq_change("CTTTAA", "CA") == ("TTTA", "", 1, 1)  # deletion
    assert collapse_seq_change("A", "AA") == ("A", "AA", 0, 0)  # duplication
    assert collapse_seq_change("ATG", "ATGATG") == ("ATG", "ATGATG", 0, 0)  # duplication
    assert collapse_seq_change("TCT", "AGCTCT") == ("TCT", "AGCTCT", 0, 0)  # amino acid duplication
    assert collapse_seq_change("AA", "ATTTA") == ("AA", "ATTTA", 0, 0)  # insertion
    assert collapse_seq_change("AAC", "AATTTC") == ("AC", "ATTTC", 1, 0)  # insertion
    assert collapse_seq_change("CAA", "CTTTAA") == ("CA", "CTTTA", 0, 1)  # insertion
    assert collapse_seq_change("GGT", "GTG") == ("GT", "TG", 1, 0)  # delins
    assert collapse_seq_change("ATCG", "ATT") == ("CG", "T", 2, 0)  # delins
    assert collapse_seq_change("ATCG", "TTG") == ("ATC", "TT", 0, 1)  # delins
    assert collapse_seq_change("ATG", "ATG") == ("ATG", "ATG", 0, 0)  # synonymous


def test_split_seq_change():
    assert split_seq_change("AATTTC", "AAGC") == ("TTT", "G", "AA", "C")
    assert split_seq_change("ATTTC", "AC") == ("TTT", "", "A", "C")
    assert split_seq_change("CGAA", "CTTTAA") == ("G", "TTT", "C", "AA")
    assert split_seq_change("ATTTC", "AC") == ("TTT", "", "A", "C")
    assert split_seq_change("ATG", "GTA") == ("ATG", "GTA", "", "")
    assert split_seq_change("GCTGGT", "GCTACTGGT") == ("", "ACT", "GCT", "GGT")


def test_expand_nt():
    assert list(expand_nt("A")) == ["A"]
    assert list(expand_nt("R")) == ["A", "G"]
    assert list(expand_nt("N")) == ["A", "C", "G", "T"]


def test_expand_pep():
    assert list(expand_pep("A")) == ["A"]
    assert list(expand_pep("Z")) == ["E", "Q"]
    assert len(list(expand_pep("X"))) == 20  # all amino acids except '*'


def test_format_hgvs_position():
    assert format_hgvs_position(5, 0) == "5"
    assert format_hgvs_position(5, 1) == "5+1"
    assert format_hgvs_position(5, -1) == "5-1"
    assert format_hgvs_position(1, 1) == "+1"
    assert format_hgvs_position(1, -1) == "-1"
    assert format_hgvs_position(5, 0, is_3_prime_utr=True) == "*5"
    assert format_hgvs_position(5, 1, is_3_prime_utr=True) == "*5+1"
    assert format_hgvs_position(5, -1, is_3_prime_utr=True) == "*5-1"
    assert format_hgvs_position(1, 1, is_3_prime_utr=True) == "*1+1"
    assert format_hgvs_position(1, -1, is_3_prime_utr=True) == "*1-1"


def test_is_deletion():
    assert is_deletion("AGT", "")
    assert is_deletion("A", "")
    assert not is_deletion("AGT", "AG")
    assert not is_deletion("", "")


def test_is_delins():
    assert is_delins("AGT", "AAA")
    assert is_delins("AGT", "C")
    assert is_delins("AGT", "AGTAG")
    assert not is_delins("AGT", "AGTAGT")  # duplication
    assert not is_delins("AG", "ACCCG")  # insertion
    assert not is_delins("A", "G")  # substitution
    assert not is_delins("", "")


def test_is_duplication():
    assert is_duplication("ATG", "ATGATG")
    assert is_duplication("A", "AA")
    assert not is_duplication("ATG", "ATGAT")
    assert not is_duplication("ATG", "ATGAATG")


def test_is_frameshift():
    assert is_frameshift("AAA", "A")
    assert is_frameshift("AAA", "AA")
    assert not is_frameshift("AAA", "AAA")


def test_is_insertion():
    assert is_insertion("GT", "GAT")
    assert is_insertion("GGGTTT", "GGGAAATTT")
    assert not is_insertion("GT", "GAA")
    assert not is_insertion("GT", "G")
    assert not is_insertion("GT", "T")
    assert not is_insertion("", "")


def test_is_substitution():
    assert is_substitution("A", "G")
    assert not is_substitution("A", "")
    assert not is_substitution("AGT", "AAA")  # delins
    assert not is_substitution("", "")


def test_reverse_complement():
    assert reverse_complement("AGCT") == "AGCT"
    assert reverse_complement("AACC") == "GGTT"


def test_reverse_translate():
    assert list(reverse_translate("A")) == ["GCA", "GCC", "GCG", "GCT"]
    assert list(reverse_translate("CQ")) == ["TGCCAA", "TGCCAG", "TGTCAA", "TGTCAG"]
    assert list(reverse_translate("B")) == ["GAC", "GAT", "AAC", "AAT"]


def test_split_by_codon():
    assert list(split_by_codon("ABC")) == ["ABC"]
    assert list(split_by_codon("ABCDEF")) == ["ABC", "DEF"]
    with pytest.raises(ValueError):
        # Error raised when iterable is not divisible by 3
        list(split_by_codon("ABCD"))


def test_split_insertion():
    assert split_insertion("GT", "GAT") == ("G", "A", "T")
    assert split_insertion("GGGTTT", "GGGAAATTT") == ("GGG", "AAA", "TTT")
    assert split_insertion("GT", "GAA") is None
    assert split_insertion("GT", "G") is None
    assert split_insertion("GT", "T") is None
    assert split_insertion("", "") is None


def test_strip_version():
    assert strip_version("NM_000546.5") == "NM_000546"
    assert strip_version("NM_000546") == "NM_000546"
