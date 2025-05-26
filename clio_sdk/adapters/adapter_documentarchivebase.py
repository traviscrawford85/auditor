# Adapter for documentarchivebase
from clio_sdk.models.documentarchivebase import DocumentarchivebaseIn, DocumentarchivebaseOut, DocumentarchivebaseUpdate, DocumentarchivebaseDb
from clio_client.models import document_archive

def convert_sdk_to_documentarchivebaseout(src: document_archive) -> DocumentarchivebaseOut:
    return DocumentarchivebaseOut(**src.dict())

def convert_documentarchivebasein_to_sdk(src: DocumentarchivebaseIn) -> document_archive:
    return document_archive(**src.dict())
