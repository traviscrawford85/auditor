# Adapter for documentarchivebase
from clio_sdk.models.documentarchivebase import DocumentarchiveBaseIn, DocumentarchivebaseOut, DocumentarchivebaseUpdate, DocumentarchivebaseDb
from clio_client.models.document_archive import DocumentArchive

def convert_sdk_to_documentarchivebaseout(src: DocumentArchive) -> DocumentarchivebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return DocumentarchivebaseOut(**src.model_dump())

def convert_documentarchivebasein_to_sdk(src: DocumentarchiveBaseIn) -> DocumentArchive:
    """Converts a clio_sdk model to clio_client model."""
    return DocumentArchive(**src.model_dump())
