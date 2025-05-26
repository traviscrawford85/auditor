# Adapter for documenttemplatebase
from clio_sdk.models.documenttemplatebase import DocumenttemplatebaseIn, DocumenttemplatebaseOut, DocumenttemplatebaseUpdate, DocumenttemplatebaseDb
from clio_client.models import document_template

def convert_sdk_to_documenttemplatebaseout(src: document_template) -> DocumenttemplatebaseOut:
    return DocumenttemplatebaseOut(**src.dict())

def convert_documenttemplatebasein_to_sdk(src: DocumenttemplatebaseIn) -> document_template:
    return document_template(**src.dict())
