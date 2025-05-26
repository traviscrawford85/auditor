# Adapter for documenttemplatelist
from clio_sdk.models.documenttemplatelist import DocumenttemplatelistIn, DocumenttemplatelistOut, DocumenttemplatelistUpdate, DocumenttemplatelistDb
from clio_client.models.document_template_list import DocumentTemplateList

def convert_sdk_to_documenttemplatelistout(src: DocumentTemplateList) -> DocumenttemplatelistOut:
    """Converts a clio_client model to clio_sdk model."""
    return DocumenttemplatelistOut(**src.model_dump())

def convert_documenttemplatelistin_to_sdk(src: DocumenttemplatelistIn) -> DocumentTemplateList:
    """Converts a clio_sdk model to clio_client model."""
    return DocumentTemplateList(**src.model_dump())
