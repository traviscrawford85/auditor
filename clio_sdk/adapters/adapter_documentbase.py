# Adapter for documentbase
from clio_sdk.models.documentbase import DocumentbaseIn, DocumentbaseOut, DocumentbaseUpdate, DocumentbaseDb
from clio_client.models import document

def convert_sdk_to_documentbaseout(src: document) -> DocumentbaseOut:
    return DocumentbaseOut(**src.dict())

def convert_documentbasein_to_sdk(src: DocumentbaseIn) -> document:
    return document(**src.dict())
