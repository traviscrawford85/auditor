# Adapter for error
from clio_sdk.models.error import ErrorIn, ErrorOut, ErrorUpdate, ErrorDb
from clio_client.models import error

def convert_sdk_to_errorout(src: error) -> ErrorOut:
    return ErrorOut(**src.dict())

def convert_errorin_to_sdk(src: ErrorIn) -> error:
    return error(**src.dict())
