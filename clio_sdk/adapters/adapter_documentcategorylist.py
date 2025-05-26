# Adapter for documentcategorylist
from clio_sdk.models.documentcategorylist import DocumentcategorylistIn, DocumentcategorylistOut, DocumentcategorylistUpdate, DocumentcategorylistDb
from clio_client.models import document_category_list

def convert_sdk_to_documentcategorylistout(src: document_category_list) -> DocumentcategorylistOut:
    return DocumentcategorylistOut(**src.dict())

def convert_documentcategorylistin_to_sdk(src: DocumentcategorylistIn) -> document_category_list:
    return document_category_list(**src.dict())
