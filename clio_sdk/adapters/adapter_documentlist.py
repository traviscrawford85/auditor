# Adapter for documentlist
from clio_sdk.models.documentlist import DocumentlistIn, DocumentlistOut, DocumentlistUpdate, DocumentlistDb
from clio_client.models import document_list

def convert_sdk_to_documentlistout(src: document_list) -> DocumentlistOut:
    return DocumentlistOut(**src.dict())

def convert_documentlistin_to_sdk(src: DocumentlistIn) -> document_list:
    return document_list(**src.dict())
