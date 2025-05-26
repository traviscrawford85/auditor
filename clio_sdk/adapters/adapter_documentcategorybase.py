# Adapter for documentcategorybase
from clio_sdk.models.documentcategorybase import DocumentcategoryBaseIn, DocumentcategorybaseOut, DocumentcategorybaseUpdate, DocumentcategorybaseDb
from clio_client.models.document_category import DocumentCategory

def convert_sdk_to_documentcategorybaseout(src: DocumentCategory) -> DocumentcategorybaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return DocumentcategorybaseOut(**src.model_dump())

def convert_documentcategorybasein_to_sdk(src: DocumentcategoryBaseIn) -> DocumentCategory:
    """Converts a clio_sdk model to clio_client model."""
    return DocumentCategory(**src.model_dump())
