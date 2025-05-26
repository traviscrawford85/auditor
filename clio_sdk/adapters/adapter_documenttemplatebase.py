# Adapter for documenttemplatebase
from clio_sdk.models.documenttemplatebase import DocumenttemplateBaseIn, DocumenttemplatebaseOut, DocumenttemplatebaseUpdate, DocumenttemplatebaseDb
from clio_client.models.document_template import DocumentTemplate

def convert_sdk_to_documenttemplatebaseout(src: DocumentTemplate) -> DocumenttemplatebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return DocumenttemplatebaseOut(**src.model_dump())

def convert_documenttemplatebasein_to_sdk(src: DocumenttemplateBaseIn) -> DocumentTemplate:
    """Converts a clio_sdk model to clio_client model."""
    return DocumentTemplate(**src.model_dump())
