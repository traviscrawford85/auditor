# Adapter for documentbase
from clio_sdk.models.documentbase import DocumentBaseIn, DocumentbaseOut, DocumentbaseUpdate, DocumentbaseDb
from clio_client.models.document import Document

def convert_sdk_to_documentbaseout(src: Document) -> DocumentbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return DocumentbaseOut(**src.model_dump())

def convert_documentbasein_to_sdk(src: DocumentBaseIn) -> Document:
    """Converts a clio_sdk model to clio_client model."""
    return Document(**src.model_dump())
