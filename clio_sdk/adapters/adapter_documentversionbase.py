# Adapter for documentversionbase
from clio_sdk.models.documentversionbase import DocumentversionbaseIn, DocumentversionbaseOut, DocumentversionbaseUpdate, DocumentversionbaseDb
from clio_client.models import document_version

def convert_sdk_to_documentversionbaseout(src: document_version) -> DocumentversionbaseOut:
    return DocumentversionbaseOut(**src.dict())

def convert_documentversionbasein_to_sdk(src: DocumentversionbaseIn) -> document_version:
    return document_version(**src.dict())
