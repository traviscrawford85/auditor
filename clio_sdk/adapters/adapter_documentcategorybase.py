# Adapter for documentcategorybase
from clio_sdk.models.documentcategorybase import DocumentcategorybaseIn, DocumentcategorybaseOut, DocumentcategorybaseUpdate, DocumentcategorybaseDb
from clio_client.models import document_category

def convert_sdk_to_documentcategorybaseout(src: document_category) -> DocumentcategorybaseOut:
    return DocumentcategorybaseOut(**src.dict())

def convert_documentcategorybasein_to_sdk(src: DocumentcategorybaseIn) -> document_category:
    return document_category(**src.dict())
