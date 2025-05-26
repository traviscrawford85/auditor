# Adapter for documentautomationlist
from clio_sdk.models.documentautomationlist import DocumentautomationlistIn, DocumentautomationlistOut, DocumentautomationlistUpdate, DocumentautomationlistDb
from clio_client.models import document_automation_list

def convert_sdk_to_documentautomationlistout(src: document_automation_list) -> DocumentautomationlistOut:
    return DocumentautomationlistOut(**src.dict())

def convert_documentautomationlistin_to_sdk(src: DocumentautomationlistIn) -> document_automation_list:
    return document_automation_list(**src.dict())
