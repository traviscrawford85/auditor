# Adapter for documentshow
from clio_sdk.models.documentshow import DocumentshowIn, DocumentshowOut, DocumentshowUpdate, DocumentshowDb
from clio_client.models import document_show

def convert_sdk_to_documentshowout(src: document_show) -> DocumentshowOut:
    return DocumentshowOut(**src.dict())

def convert_documentshowin_to_sdk(src: DocumentshowIn) -> document_show:
    return document_show(**src.dict())
