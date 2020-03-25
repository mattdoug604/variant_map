from .cache import Ensembl
from .util import is_ensembl_id


ENSEMBL = Ensembl()


def get_transcripts(feature, feature_type):
    transcripts = []
    for transcript_id in _get_transcript_ids(feature, feature_type):
        transcripts.append(ENSEMBL.data.transcript_by_id(transcript_id))
    return transcripts


def _get_transcript_ids(feature, feature_type):
    if is_ensembl_id(feature):
        transcript_ids = _get_transcript_ids_by_id(feature, feature_type)
    else:
        transcript_ids = _get_transcript_ids_by_name(feature, feature_type)

    if not transcript_ids:
        raise ValueError(f"'{feature}' did not match any transcript ID")

    if not isinstance(transcript_ids, list):
        transcript_ids = [transcript_ids]

    return sorted(transcript_ids)


def _get_transcript_ids_by_id(feature, feature_type):
    if feature_type == "cds":
        return feature
    elif feature_type == "exon":
        # NOTE: with `pyensembl==1.8.5` calling `transcript_ids_of_exon_ids` does not
        # match anything. As a workaround, we can map the exon to its gene then return 
        # all transcripts of that gene that contain the exon.
        gene_id = ENSEMBL.data.exon_by_id(feature).gene_id
        return transcripts_with_exon(gene_id, "gene", feature)
    elif feature_type == "gene":
        return ENSEMBL.data.transcript_ids_of_gene_id(feature)
    elif feature_type == "protein":
        return ENSEMBL.data.transcript_id_of_protein_id(feature)
    elif feature_type == "transcript":
        return feature
    else:
        raise TypeError(f"Cannot get transcript IDs from {feature_type}")


def _get_transcript_ids_by_name(feature, feature_type):
    if feature_type == "cds":
        return ENSEMBL.data.transcript_ids_of_transcript_name(feature)
    elif feature_type == "exon":
        raise NotImplementedError(f"Cannot get transcript IDs for {feature_type} name")
    elif feature_type == "gene":
        return ENSEMBL.data.transcript_ids_of_gene_name(feature)
    elif feature_type == "protein":
        raise NotImplementedError(f"Cannot get transcript IDs for {feature_type} name")
    elif feature_type == "transcript":
        return ENSEMBL.data.transcript_ids_of_transcript_name(feature)
    else:
        raise TypeError(f"Cannot get transcript IDs from {feature_type}")


def transcripts_with_exon(feature, feature_type, exon_id):
    """Check if the given transcript contains the exon."""
    transcripts_with_exon = []
    for transcript in get_transcripts(feature, feature_type):
        if exon_id in [i.exon_id for i in transcript.exons]:
            transcripts_with_exon.append(transcript.transcript_id)
    return transcripts_with_exon
