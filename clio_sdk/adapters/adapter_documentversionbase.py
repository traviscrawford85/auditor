# Adapter for documentversionbase
from clio_sdk.models.documentversionbase import DocumentversionBaseIn, DocumentversionbaseOut, DocumentversionbaseUpdate, DocumentversionbaseDb
from clio_client.models.document_version import DocumentVersion

def convert_sdk_to_documentversionbaseout(src: DocumentVersion) -> DocumentversionbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return DocumentversionbaseOut(**src.model_dump())

def convert_documentversionbasein_to_sdk(src: DocumentversionBaseIn) -> DocumentVersion:
    """Converts a clio_sdk model to clio_client model."""
    return DocumentVersion(**src.model_dump())
