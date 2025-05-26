# Adapter for documentshow
from clio_sdk.models.documentshow import DocumentshowIn, DocumentshowOut, DocumentshowUpdate, DocumentshowDb
from clio_client.models.document_show import DocumentShow

def convert_sdk_to_documentshowout(src: DocumentShow) -> DocumentshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return DocumentshowOut(**src.model_dump())

def convert_documentshowin_to_sdk(src: DocumentshowIn) -> DocumentShow:
    """Converts a clio_sdk model to clio_client model."""
    return DocumentShow(**src.model_dump())
