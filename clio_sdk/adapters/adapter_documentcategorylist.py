# Adapter for documentcategorylist
from clio_sdk.models.documentcategorylist import DocumentcategorylistIn, DocumentcategorylistOut, DocumentcategorylistUpdate, DocumentcategorylistDb
from clio_client.models.document_category_list import DocumentCategoryList

def convert_sdk_to_documentcategorylistout(src: DocumentCategoryList) -> DocumentcategorylistOut:
    """Converts a clio_client model to clio_sdk model."""
    return DocumentcategorylistOut(**src.model_dump())

def convert_documentcategorylistin_to_sdk(src: DocumentcategorylistIn) -> DocumentCategoryList:
    """Converts a clio_sdk model to clio_client model."""
    return DocumentCategoryList(**src.model_dump())
