# Adapter for documentcategoryshow
from clio_sdk.models.documentcategoryshow import DocumentcategoryshowIn, DocumentcategoryshowOut, DocumentcategoryshowUpdate, DocumentcategoryshowDb
from clio_client.models import document_category_show

def convert_sdk_to_documentcategoryshowout(src: document_category_show) -> DocumentcategoryshowOut:
    return DocumentcategoryshowOut(**src.dict())

def convert_documentcategoryshowin_to_sdk(src: DocumentcategoryshowIn) -> document_category_show:
    return document_category_show(**src.dict())
