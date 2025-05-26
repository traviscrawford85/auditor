# Adapter for documentarchiveshow
from clio_sdk.models.documentarchiveshow import DocumentarchiveshowIn, DocumentarchiveshowOut, DocumentarchiveshowUpdate, DocumentarchiveshowDb
from clio_client.models import document_archive_show

def convert_sdk_to_documentarchiveshowout(src: document_archive_show) -> DocumentarchiveshowOut:
    return DocumentarchiveshowOut(**src.dict())

def convert_documentarchiveshowin_to_sdk(src: DocumentarchiveshowIn) -> document_archive_show:
    return document_archive_show(**src.dict())
