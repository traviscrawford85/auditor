# Adapter for documentautomationshow
from clio_sdk.models.documentautomationshow import DocumentautomationshowIn, DocumentautomationshowOut, DocumentautomationshowUpdate, DocumentautomationshowDb
from clio_client.models import document_automation_show

def convert_sdk_to_documentautomationshowout(src: document_automation_show) -> DocumentautomationshowOut:
    return DocumentautomationshowOut(**src.dict())

def convert_documentautomationshowin_to_sdk(src: DocumentautomationshowIn) -> document_automation_show:
    return document_automation_show(**src.dict())
