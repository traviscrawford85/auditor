# Adapter for error
from clio_sdk.models.error import ErrorIn, ErrorOut, ErrorUpdate, ErrorDb
from clio_client.models.error import Error

def convert_sdk_to_errorout(src: Error) -> ErrorOut:
    """Converts a clio_client model to clio_sdk model."""
    return ErrorOut(**src.model_dump())

def convert_errorin_to_sdk(src: ErrorIn) -> Error:
    """Converts a clio_sdk model to clio_client model."""
    return Error(**src.model_dump())
