# Adapter for multipartbase
from clio_sdk.models.multipartbase import MultipartBaseIn, MultipartbaseOut, MultipartbaseUpdate, MultipartbaseDb
from clio_client.models.multipart import Multipart

def convert_sdk_to_multipartbaseout(src: Multipart) -> MultipartbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return MultipartbaseOut(**src.model_dump())

def convert_multipartbasein_to_sdk(src: MultipartBaseIn) -> Multipart:
    """Converts a clio_sdk model to clio_client model."""
    return Multipart(**src.model_dump())
