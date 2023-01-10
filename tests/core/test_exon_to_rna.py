import pytest

from ensembl_map.core import ExonMappablePosition, RnaMappablePosition


def test_negative_strand(ensembl100):
    position = ExonMappablePosition(
        _data=ensembl100,
        contig_id="5",
        start=2,
        start_offset=0,
        end=2,
        end_offset=0,
        strand="-",
        gene_id="ENSG00000164362",
        gene_name="TERT",
        transcript_id="ENST00000310581",
        transcript_name="TERT-201",
        exon_id="ENSE00001197112",
    )
    expected = RnaMappablePosition(
        _data=ensembl100,
        contig_id="5",
        start=299,
        start_offset=0,
        end=1652,
        end_offset=0,
        strand="-",
        gene_id="ENSG00000164362",
        gene_name="TERT",
        transcript_id="ENST00000310581",
        transcript_name="TERT-201",
    )
    assert position.to_rna() == [expected]


def test_positive_strand(ensembl100):
    position = ExonMappablePosition(
        _data=ensembl100,
        contig_id="13",
        start=3,
        start_offset=0,
        end=3,
        end_offset=0,
        strand="+",
        gene_id="ENSG00000139618",
        gene_name="BRCA2",
        transcript_id="ENST00000380152",
        transcript_name="BRCA2-201",
        exon_id="ENSE00003666217",
    )
    expected = RnaMappablePosition(
        _data=ensembl100,
        contig_id="13",
        start=301,
        start_offset=0,
        end=549,
        end_offset=0,
        strand="+",
        gene_id="ENSG00000139618",
        gene_name="BRCA2",
        transcript_id="ENST00000380152",
        transcript_name="BRCA2-201",
    )
    assert position.to_rna() == [expected]


def test_offset_error(ensembl100):
    position = ExonMappablePosition(
        _data=ensembl100,
        contig_id="5",
        start=1,
        start_offset=1,
        end=1,
        end_offset=1,
        strand="-",
        gene_id="ENSG00000164362",
        gene_name="TERT",
        transcript_id="ENST00000310581",
        transcript_name="TERT-201",
        exon_id="ENSE00001197112",
    )
    with pytest.raises(AssertionError):
        position.to_rna()