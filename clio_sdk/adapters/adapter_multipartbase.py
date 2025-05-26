# Adapter for multipartbase
from clio_sdk.models.multipartbase import MultipartbaseIn, MultipartbaseOut, MultipartbaseUpdate, MultipartbaseDb
from clio_client.models import multipart

def convert_sdk_to_multipartbaseout(src: multipart) -> MultipartbaseOut:
    return MultipartbaseOut(**src.dict())

def convert_multipartbasein_to_sdk(src: MultipartbaseIn) -> multipart:
    return multipart(**src.dict())
