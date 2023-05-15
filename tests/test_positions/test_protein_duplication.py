import pytest

from pyvariant.constants import DUPLICATION
from pyvariant.positions import CdnaDuplication, DnaDuplication, ProteinDuplication, RnaDuplication


@pytest.fixture()
def variant():
    return ProteinDuplication(
        contig_id="4",
        start=501,
        start_offset=0,
        end=501,
        end_offset=0,
        strand="+",
        gene_id="ENSG00000157404",
        gene_name="KIT",
        transcript_id="ENST00000288135",
        transcript_name="KIT-001",
        protein_id="ENSP00000288135",
        refseq="S",
        altseq="SS",
    )


def test_str(variant):
    assert str(variant) == "ENSP00000288135:p.S501dup"


def test_type(variant):
    assert not variant.is_cdna
    assert not variant.is_dna
    assert not variant.is_exon
    assert variant.is_protein
    assert not variant.is_rna


def test_variant_type(variant):
    assert variant.variant_type == DUPLICATION
    assert not variant.is_deletion
    assert not variant.is_delins
    assert variant.is_duplication
    assert not variant.is_frameshift
    assert not variant.is_fusion
    assert not variant.is_insertion
    assert not variant.is_substitution


def test_to_cdna(ensembl69, variant):
    expected = CdnaDuplication(
        contig_id="4",
        start=1501,
        start_offset=0,
        end=1503,
        end_offset=0,
        strand="+",
        gene_id="ENSG00000157404",
        gene_name="KIT",
        transcript_id="ENST00000288135",
        transcript_name="KIT-001",
        protein_id="ENSP00000288135",
        refseq="TCT",
        altseq="TCTTCT",
    )
    result = ensembl69.to_cdna(variant)
    assert expected in result
    assert len(result) == 36


def test_to_dna(ensembl69, variant):
    expected = DnaDuplication(
        contig_id="4",
        start=55592177,
        start_offset=0,
        end=55592179,
        end_offset=0,
        strand="+",
        refseq="TCT",
        altseq="TCTTCT",
    )
    result = ensembl69.to_dna(variant)
    assert expected in result
    assert len(result) == 36


def test_to_protein(ensembl69, variant):
    expected = [
        ProteinDuplication(
            contig_id="4",
            start=501,
            start_offset=0,
            end=501,
            end_offset=0,
            strand="+",
            gene_id="ENSG00000157404",
            gene_name="KIT",
            transcript_id="ENST00000288135",
            transcript_name="KIT-001",
            protein_id="ENSP00000288135",
            refseq="S",
            altseq="SS",
        )
    ]
    assert ensembl69.to_protein(variant) == expected


def test_to_rna(ensembl69, variant):
    expected = RnaDuplication(
        contig_id="4",
        start=1598,
        start_offset=0,
        end=1600,
        end_offset=0,
        strand="+",
        gene_id="ENSG00000157404",
        gene_name="KIT",
        transcript_id="ENST00000288135",
        transcript_name="KIT-001",
        refseq="TCT",
        altseq="TCTTCT",
    )
    result = ensembl69.to_rna(variant)
    assert expected in result
    assert len(result) == 36
