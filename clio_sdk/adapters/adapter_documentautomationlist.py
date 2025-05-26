# Adapter for documentautomationlist
from clio_sdk.models.documentautomationlist import DocumentautomationlistIn, DocumentautomationlistOut, DocumentautomationlistUpdate, DocumentautomationlistDb
from clio_client.models.document_automation_list import DocumentAutomationList

def convert_sdk_to_documentautomationlistout(src: DocumentAutomationList) -> DocumentautomationlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return DocumentautomationlistOut(**src.model_dump())

def convert_documentautomationlistin_to_sdk(src: DocumentautomationlistIn) -> DocumentAutomationList:
    """Converts a clio_sdk model to clio_client model."""
    return DocumentAutomationList(**src.model_dump())
