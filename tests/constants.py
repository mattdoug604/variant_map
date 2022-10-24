import os.path

CACHE_DIR = os.path.join(os.path.dirname(__file__), "cache")

CANONICAL_TRANSCRIPT = os.path.join(CACHE_DIR, "canonical_transcript.txt")
CONTIG_ALIAS = os.path.join(CACHE_DIR, "contig_alias.tsv")
EXON_ALIAS = os.path.join(CACHE_DIR, "exon_alias.tsv")
GENE_ALIAS = os.path.join(CACHE_DIR, "gene_alias.tsv")
PROTEIN_ALIAS = os.path.join(CACHE_DIR, "protein_alias.tsv")
TRANSCRIPT_ALIAS = os.path.join(CACHE_DIR, "transcript_alias.tsv")
ENS100 = os.path.join(CACHE_DIR, "homo_sapiens", "GRCh38", "100")

TEST_CDNA_FASTA = os.path.join(ENS100, "Homo_sapiens.GRCh38.cdna.all.fa.gz")
TEST_DNA_FASTA = os.path.join(ENS100, "Homo_sapiens.GRCh38.dna.toplevel.fa.gz")
TEST_GTF = os.path.join(ENS100, "Homo_sapiens.GRCh38.100.gtf.gz")
TEST_NCRNA_FASTA = os.path.join(ENS100, "Homo_sapiens.GRCh38.ncrna.fa.gz")
TEST_PEP_FASTA = os.path.join(ENS100, "Homo_sapiens.GRCh38.pep.all.fa.gz")
