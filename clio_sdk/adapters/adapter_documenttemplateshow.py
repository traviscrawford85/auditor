# Adapter for documenttemplateshow
from clio_sdk.models.documenttemplateshow import DocumenttemplateshowIn, DocumenttemplateshowOut, DocumenttemplateshowUpdate, DocumenttemplateshowDb
from clio_client.models.document_template_show import DocumentTemplateShow

def convert_sdk_to_documenttemplateshowout(src: DocumentTemplateShow) -> DocumenttemplateshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return DocumenttemplateshowOut(**src.model_dump())

def convert_documenttemplateshowin_to_sdk(src: DocumenttemplateshowIn) -> DocumentTemplateShow:
    """Converts a clio_sdk model to clio_client model."""
    return DocumentTemplateShow(**src.model_dump())
