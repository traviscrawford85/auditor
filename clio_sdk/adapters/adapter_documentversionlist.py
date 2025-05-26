# Adapter for documentversionlist
from clio_sdk.models.documentversionlist import DocumentversionlistIn, DocumentversionlistOut, DocumentversionlistUpdate, DocumentversionlistDb
from clio_client.models import document_version_list

def convert_sdk_to_documentversionlistout(src: document_version_list) -> DocumentversionlistOut:
    return DocumentversionlistOut(**src.dict())

def convert_documentversionlistin_to_sdk(src: DocumentversionlistIn) -> document_version_list:
    return document_version_list(**src.dict())
