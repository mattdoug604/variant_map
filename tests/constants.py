import os.path

CACHE_DIR = os.path.join(os.path.dirname(__file__), "data")
CANONICAL_TRANSCRIPT = os.path.join(CACHE_DIR, "canonical_transcript.txt")
CONTIG_ALIAS = os.path.join(CACHE_DIR, "contig_alias.tsv")
EXON_ALIAS = os.path.join(CACHE_DIR, "exon_alias.tsv")
GENE_ALIAS = os.path.join(CACHE_DIR, "gene_alias.tsv")
PROTEIN_ALIAS = os.path.join(CACHE_DIR, "protein_alias.tsv")
TRANSCRIPT_ALIAS = os.path.join(CACHE_DIR, "transcript_alias.tsv")
ENS69 = os.path.join(CACHE_DIR, "homo_sapiens", "GRCh37", "69")
TEST_ENS69_CDNA_FASTA = os.path.join(ENS69, "Homo_sapiens.GRCh37.69.cdna.all.fa.gz")
TEST_ENS69_DNA_FASTA = os.path.join(ENS69, "Homo_sapiens.GRCh37.69.dna.toplevel.fa.gz")
TEST_ENS69_GTF = os.path.join(ENS69, "Homo_sapiens.GRCh37.69.gtf.gz")
TEST_ENS69_NCRNA_FASTA = os.path.join(ENS69, "Homo_sapiens.GRCh37.69.ncrna.fa.gz")
TEST_ENS69_PEP_FASTA = os.path.join(ENS69, "Homo_sapiens.GRCh37.69.pep.all.fa.gz")
ENS100 = os.path.join(CACHE_DIR, "homo_sapiens", "GRCh38", "100")
TEST_ENS100_CDNA_FASTA = os.path.join(ENS100, "Homo_sapiens.GRCh38.cdna.all.fa.gz")
TEST_ENS100_DNA_FASTA = os.path.join(ENS100, "Homo_sapiens.GRCh38.dna.toplevel.fa.gz")
TEST_ENS100_GTF = os.path.join(ENS100, "Homo_sapiens.GRCh38.100.gtf.gz")
TEST_ENS100_NCRNA_FASTA = os.path.join(ENS100, "Homo_sapiens.GRCh38.ncrna.fa.gz")
TEST_ENS100_PEP_FASTA = os.path.join(ENS100, "Homo_sapiens.GRCh38.pep.all.fa.gz")
