# Adapter for multipartheaderbase
from clio_sdk.models.multipartheaderbase import MultipartheaderbaseIn, MultipartheaderbaseOut, MultipartheaderbaseUpdate, MultipartheaderbaseDb
from clio_client.models import multipart_header_base

def convert_sdk_to_multipartheaderbaseout(src: multipart_header_base) -> MultipartheaderbaseOut:
    return MultipartheaderbaseOut(**src.dict())

def convert_multipartheaderbasein_to_sdk(src: MultipartheaderbaseIn) -> multipart_header_base:
    return multipart_header_base(**src.dict())
