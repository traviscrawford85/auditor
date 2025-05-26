# Adapter for documentautomationbase
from clio_sdk.models.documentautomationbase import DocumentautomationBaseIn, DocumentautomationbaseOut, DocumentautomationbaseUpdate, DocumentautomationbaseDb
from clio_client.models.document_automation import DocumentAutomation

def convert_sdk_to_documentautomationbaseout(src: DocumentAutomation) -> DocumentautomationbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return DocumentautomationbaseOut(**src.model_dump())

def convert_documentautomationbasein_to_sdk(src: DocumentautomationBaseIn) -> DocumentAutomation:
    """Converts a clio_sdk model to clio_client model."""
    return DocumentAutomation(**src.model_dump())
