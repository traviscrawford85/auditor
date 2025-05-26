# Adapter for documenttemplatelist
from clio_sdk.models.documenttemplatelist import DocumenttemplatelistIn, DocumenttemplatelistOut, DocumenttemplatelistUpdate, DocumenttemplatelistDb
from clio_client.models import document_template_list

def convert_sdk_to_documenttemplatelistout(src: document_template_list) -> DocumenttemplatelistOut:
    return DocumenttemplatelistOut(**src.dict())

def convert_documenttemplatelistin_to_sdk(src: DocumenttemplatelistIn) -> document_template_list:
    return document_template_list(**src.dict())
