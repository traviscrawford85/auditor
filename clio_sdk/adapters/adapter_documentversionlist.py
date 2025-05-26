# Adapter for documentversionlist
from clio_sdk.models.documentversionlist import DocumentversionlistIn, DocumentversionlistOut, DocumentversionlistUpdate, DocumentversionlistDb
from clio_client.models.document_version_list import DocumentVersionList

def convert_sdk_to_documentversionlistout(src: DocumentVersionList) -> DocumentversionlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return DocumentversionlistOut(**src.model_dump())

def convert_documentversionlistin_to_sdk(src: DocumentversionlistIn) -> DocumentVersionList:
    """Converts a clio_sdk model to clio_client model."""
    return DocumentVersionList(**src.model_dump())
