# Adapter for documentlist
from clio_sdk.models.documentlist import DocumentlistIn, DocumentlistOut, DocumentlistUpdate, DocumentlistDb
from clio_client.models.document_list import DocumentList

def convert_sdk_to_documentlistout(src: DocumentList) -> DocumentlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return DocumentlistOut(**src.model_dump())

def convert_documentlistin_to_sdk(src: DocumentlistIn) -> DocumentList:
    """Converts a clio_sdk model to clio_client model."""
    return DocumentList(**src.model_dump())
