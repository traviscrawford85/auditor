# Adapter for errordetail
from clio_sdk.models.errordetail import ErrordetailIn, ErrordetailOut, ErrordetailUpdate, ErrordetailDb
from clio_client.models.error_detail import ErrorDetail

def convert_sdk_to_errordetailout(src: ErrorDetail) -> ErrordetailOut:
    """Converts a clio_client model to clio_sdk model."""
    return ErrordetailOut(**src.model_dump())

def convert_errordetailin_to_sdk(src: ErrordetailIn) -> ErrorDetail:
    """Converts a clio_sdk model to clio_client model."""
    return ErrorDetail(**src.model_dump())
