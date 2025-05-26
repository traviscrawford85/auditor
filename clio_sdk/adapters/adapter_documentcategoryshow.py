# Adapter for documentcategoryshow
from clio_sdk.models.documentcategoryshow import DocumentcategoryshowIn, DocumentcategoryshowOut, DocumentcategoryshowUpdate, DocumentcategoryshowDb
from clio_client.models.document_category_show import DocumentCategoryShow

def convert_sdk_to_documentcategoryshowout(src: DocumentCategoryShow) -> DocumentcategoryshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return DocumentcategoryshowOut(**src.model_dump())

def convert_documentcategoryshowin_to_sdk(src: DocumentcategoryshowIn) -> DocumentCategoryShow:
    """Converts a clio_sdk model to clio_client model."""
    return DocumentCategoryShow(**src.model_dump())
