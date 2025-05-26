# Adapter for documentarchiveshow
from clio_sdk.models.documentarchiveshow import DocumentarchiveshowIn, DocumentarchiveshowOut, DocumentarchiveshowUpdate, DocumentarchiveshowDb
from clio_client.models.document_archive_show import DocumentArchiveShow

def convert_sdk_to_documentarchiveshowout(src: DocumentArchiveShow) -> DocumentarchiveshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return DocumentarchiveshowOut(**src.model_dump())

def convert_documentarchiveshowin_to_sdk(src: DocumentarchiveshowIn) -> DocumentArchiveShow:
    """Converts a clio_sdk model to clio_client model."""
    return DocumentArchiveShow(**src.model_dump())
