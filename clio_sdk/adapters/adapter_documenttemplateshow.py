# Adapter for documenttemplateshow
from clio_sdk.models.documenttemplateshow import DocumenttemplateshowIn, DocumenttemplateshowOut, DocumenttemplateshowUpdate, DocumenttemplateshowDb
from clio_client.models import document_template_show

def convert_sdk_to_documenttemplateshowout(src: document_template_show) -> DocumenttemplateshowOut:
    return DocumenttemplateshowOut(**src.dict())

def convert_documenttemplateshowin_to_sdk(src: DocumenttemplateshowIn) -> document_template_show:
    return document_template_show(**src.dict())
