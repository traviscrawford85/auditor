# Adapter for multipartheaderbase
from clio_sdk.models.multipartheaderbase import MultipartheaderBaseIn, MultipartheaderbaseOut, MultipartheaderbaseUpdate, MultipartheaderbaseDb
from clio_client.models.multipart_header_base import MultipartHeaderBase

def convert_sdk_to_multipartheaderbaseout(src: MultipartHeaderBase) -> MultipartheaderbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return MultipartheaderbaseOut(**src.model_dump())

def convert_multipartheaderbasein_to_sdk(src: MultipartheaderBaseIn) -> MultipartHeaderBase:
    """Converts a clio_sdk model to clio_client model."""
    return MultipartHeaderBase(**src.model_dump())
