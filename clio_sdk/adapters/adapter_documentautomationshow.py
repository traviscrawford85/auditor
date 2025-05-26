# Adapter for documentautomationshow
from clio_sdk.models.documentautomationshow import DocumentautomationshowIn, DocumentautomationshowOut, DocumentautomationshowUpdate, DocumentautomationshowDb
from clio_client.models.document_automation_show import DocumentAutomationShow

def convert_sdk_to_documentautomationshowout(src: DocumentAutomationShow) -> DocumentautomationshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return DocumentautomationshowOut(**src.model_dump())

def convert_documentautomationshowin_to_sdk(src: DocumentautomationshowIn) -> DocumentAutomationShow:
    """Converts a clio_sdk model to clio_client model."""
    return DocumentAutomationShow(**src.model_dump())
