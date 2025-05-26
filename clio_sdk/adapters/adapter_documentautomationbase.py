# Adapter for documentautomationbase
from clio_sdk.models.documentautomationbase import DocumentautomationbaseIn, DocumentautomationbaseOut, DocumentautomationbaseUpdate, DocumentautomationbaseDb
from clio_client.models import document_automation

def convert_sdk_to_documentautomationbaseout(src: document_automation) -> DocumentautomationbaseOut:
    return DocumentautomationbaseOut(**src.dict())

def convert_documentautomationbasein_to_sdk(src: DocumentautomationbaseIn) -> document_automation:
    return document_automation(**src.dict())
